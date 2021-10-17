import json
from django.db import transaction
from django.utils import timezone
from django.http.response import JsonResponse
from django.views.generic.list import ListView
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods

from billing.models import Invoice, Item
from billing.utils import validate_invoice_data


@require_safe
def invoice_details(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    total = 0
    items = []
    for item in invoice.items.all():
        ammount = item.sale_price * item.quantity
        total += ammount
        items.append({
            "quantity": item.quantity,
            "name": item.product.name,
            "price": item.sale_price,
            "ammount": ammount})
    discount = 0
    sub_total = total
    if invoice.discount_code:
        discount = total * 0.3
        total = total * 0.7
    return render(request, 'invoice_details.html',
                  {"invoice": invoice,
                   "item_list": items,
                   "total": total,
                   "sub_total": sub_total,
                   "discount": discount})


@login_required
@require_http_methods(['POST', 'GET'])
def create_invoice(request):
    if request.method == 'GET':
        return render(request, 'create_invoice.html')
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return JsonResponse({"errors": ["Invalid request body"]}, status=201)
    invoice_data, errors = validate_invoice_data(data)
    if len(errors) > 0:
        return JsonResponse({"errors": errors}, status=400)
    with transaction.atomic():
        try:
            invoice = Invoice(
                client_name=invoice_data["client_name"], client_email=invoice_data["client_email"])
            if "discount_code" in invoice_data:
                invoice.discount_code = invoice_data["discount_code"]
                invoice.discount_code.used = True
                invoice.discount_code.save()
            invoice.clean_fields()
            for item in invoice_data["items"]:
                item.invoice = invoice
                item.clean_fields(["invoice"])
            invoice.save()
            Item.objects.bulk_create(invoice_data["items"])
        except ValidationError as e:
            return JsonResponse({"errors": [f"{key}: {', '.join(value)}" for key, value in e]}, status=400)
        except Exception as e:
            return JsonResponse({"errors": ["Unexpected error"]}, status=400)
    return JsonResponse({"invoice": invoice.pk}, status=201)


class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 100
    template_name = "invoice_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
