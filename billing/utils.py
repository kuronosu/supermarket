from billing.models import DiscountCode,  Item
from products.models import Product


def validate_product_dict(product):
    return not (not isinstance(product, dict) or
                "id" not in product or
                "quantity" not in product or
                not isinstance(product["id"], int) or
                not isinstance(product["quantity"], int) or
                product["quantity"] < 1)


def validate_invoice_data(data):
    client_name = data.get("client_name", None)
    client_email = data.get("client_email", None)
    products = data.get("products", None)
    errors = []
    items = []
    invoice_data = {}
    if not client_name:
        errors.append("Client name required")
    else:
        invoice_data["client_name"] = client_name
    if not client_email:
        errors.append("Client email required")
    else:
        invoice_data["client_email"] = client_email
    if not isinstance(products, list) or not products:
        errors.append("'products' must have at least 1 product")
    else:
        for p in products:
            if validate_product_dict(p):
                try:
                    product = Product.objects.get(pk=p['id'])
                    items.append(
                        Item(product=product, quantity=p['quantity'], sale_price=product.price))
                except:
                    errors.append(f"Product {p} does not exist")
            else:
                errors.append(f"Invalid product {p}")
        invoice_data["items"] = items
    if "discount_code" in data and data["discount_code"] != "":
        try:
            invoice_data["discount_code"] = DiscountCode.objects.get(
                code=data["discount_code"], used=False)
        except:
            errors.append("Invalid discount code")
    return invoice_data, errors
