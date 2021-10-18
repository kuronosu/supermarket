import csv

# https://gist.githubusercontent.com/spacecowb0y/8244758/raw/4bf44ed70543dd452b83ee49790f6a0d6727008b/productos.csv
file = "productos.csv"

new_data = {}
with open(file, encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        p = (row[1]
             .split('-')[0]
             .strip()
             .replace("  ", " ")
             .replace(" °", "°")
             .lower())
        if p not in new_data and len(p) < 30:
            new_data[p] = float(row[5])

with open('insert_products.py', 'w', encoding='utf-8') as f:
    objs = []
    for key, value in new_data.items():
        objs.append(f"Product(name='{key}',price={value})")
    f.write("from products.models import Product\n")
    f.write(f"products = [{','.join(objs)}]\n")
    f.write("Product.objects.bulk_create(products)")
