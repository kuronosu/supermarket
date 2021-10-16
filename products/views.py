from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from products.models import Product


@require_http_methods(["GET"])
def search_product_view(request):
    name: str = request.GET.get('name', None)
    if name is None:
        return JsonResponse({'products': [], 'count': 0})
    queryset = Product.objects.filter(name__icontains=name.strip()).values()
    return JsonResponse({'products': list(queryset), 'count': len(queryset)})
