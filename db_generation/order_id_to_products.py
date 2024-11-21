import json
import os

def generate_order_products_json(order_id, db):
    order_lines = [line for line in db["order_lines"] if line["order_id"] == order_id]
    products = []
    
    for line in order_lines:
        product = next((product for product in db["products"] if product["id"] == line["product_id"]), None)
        if product:
            product_info = {
                "id": product["id"],
                "name": product["name"],
                "weight": product["weight"],
                "quantity": line["quantity"]
            }
            products.append(product_info)
    
    order_products_json = {"order_id": order_id, "products": products}
    return order_products_json

def save_order_products_to_file(order_products_json, folder_name, file_name):
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        json.dump(order_products_json, file, indent=2)

# Example usage
db = {
    "warehouses": [
      {
        "id": 1,
        "name": "Warehouse A",
        "columns": 10,
        "rows": 15
      },
      {
        "id": 2,
        "name": "Warehouse B",
        "columns": 8,
        "rows": 12
      }
    ],
    "products": [
      {
        "id": 1,
        "name": "Product 1",
        "weight": 5.5
      },
      {
        "id": 2,
        "name": "Product 2",
        "weight": 3.2
      }
    ],
    "product_warehouse_locations": [
      {
        "warehouse_id": 1,
        "product_id": 1,
        "x_coordinate": 3,
        "y_coordinate": 7
      },
      {
        "warehouse_id": 1,
        "product_id": 2,
        "x_coordinate": 5,
        "y_coordinate": 10
      },
      {
        "warehouse_id": 2,
        "product_id": 1,
        "x_coordinate": 2,
        "y_coordinate": 4
      }
    ],
    "orders": [
      {
        "id": 1
      },
      {
        "id": 2
      }
    ],
    "order_lines": [
      {
        "order_id": 1,
        "product_id": 1,
        "quantity": 3
      },
      {
        "order_id": 1,
        "product_id": 2,
        "quantity": 2
      },
      {
        "order_id": 2,
        "product_id": 1,
        "quantity": 1
      }
    ],
    "boxes": [
      {
        "id": 1,
        "capacity": 100
      },
      {
        "id": 2,
        "capacity": 150
      }
    ]
}

order_id = 1
order_products_json = generate_order_products_json(order_id, db)
save_order_products_to_file(order_products_json, 'output_folder', 'order_1_products.json')
