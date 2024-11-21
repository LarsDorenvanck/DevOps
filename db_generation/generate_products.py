import json
import random
import os

def generate_products(num_products, min_weight, max_weight):
    products = []
    for i in range(1, num_products + 1):
        product = {
            "id": i,
            "name": f"Product {i}",
            "weight": round(random.uniform(min_weight, max_weight), 2)
        }
        products.append(product)
    
    products_json = {"products": products}
    return products_json

def save_products_to_file(products_json, folder_name, file_name):
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        json.dump(products_json, file, indent=2)

# Example usage
num_products = 2000  # Number of products to generate
min_weight = 1.0  # Minimum weight of products
max_weight = 10.0  # Maximum weight of products

generated_products_json = generate_products(num_products, min_weight, max_weight)
save_products_to_file(generated_products_json, 'output_folder', 'products.json')
