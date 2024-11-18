from tabulate import tabulate
import requests

while(True):

    gridsize = 10
    headers2 = [" "] + list(range(gridsize))
    warehouse = [[" " for _ in range(gridsize)] for _ in range(gridsize)]

    print("wil je; \n[1] een product in het warehouse zien \n[2] laat alle producten uit een order in het warehouse zien?")
    menu = int(input("voer een nummer in:"))


    if menu == 1:
        item_id = int(input("voer gewenste item nummer in: "))

        response = requests.get(f"http://127.0.0.1:8000/products/{item_id}")

        data = response.json()

        print(data['name'])
        product_name = data['name']
        cord_x= data['cord_x']
        cord_y= data['cord_y']
        warehouse[cord_y][cord_x] = product_name
        warehouse_with_row_numbers = [[i] + row for i, row in enumerate(warehouse)]

    elif menu == 2:
        order_id= int(input("voer gewenste order nummer in: "))
        response = requests.get(f"http://127.0.0.1:8000/orders/{order_id}")
        data = response.json()
        for index in range(len(data['order_products'])):
            product_name = data['order_products'][index]['name']
            cord_x = data['order_products'][index]['cord_x']
            cord_y = data['order_products'][index]['cord_y']




            warehouse[cord_y][cord_x] = product_name

        warehouse_with_row_numbers = [[i] + row for i, row in enumerate(warehouse)]

    print(tabulate(warehouse_with_row_numbers, headers=headers2, tablefmt="psql"))