from django.urls import path
from . import views

urlpatterns = [
    # path("", views.invoice_home_view, name="invoice_home"),
    path("", views.create_invoice, name="create_invoice"),
    path("<int:pk>/", views.invoice_details, name="invoice_details"),
    path("list/", views.InvoiceListView.as_view(), name="invoice_list"),
]
