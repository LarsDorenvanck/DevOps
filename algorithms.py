import json
import time

def best_fit_decreasing(order, box_types):
    # Expand items by quantity and sort by weight in decreasing order
    expanded_order = [item for item in order for _ in range(item['quantity'])]
    sorted_order = sorted(expanded_order, key=lambda x: x['weight'], reverse=True)
    
    # Initialize list of boxes and box types used
    boxes = []
    box_types_used = []
    
    # Iterate over each item in the sorted order
    for item in sorted_order:
        # Try to place the item in an existing box
        for index, box in enumerate(boxes):
            current_box_weight = sum(i['weight'] for i in box)
            if current_box_weight + item['weight'] <= box_types_used[index]['capacity']:
                box.append(item)
                break
        else:
            # If the item doesn't fit in any existing box, create a new box
            for box_type in box_types:
                if item['weight'] <= box_type['capacity']:
                    boxes.append([item])
                    box_types_used.append(box_type)
                    break
    
    return boxes, box_types_used

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load the order and box types from JSON files
order = load_json('db_generation/output_folder/order_1_products.json')['products']
box_types = load_json('db_generation/tables_mockup')['boxes']

# Measure the time taken to calculate the packed boxes
start_time = time.time()
packed_boxes, box_types_used = best_fit_decreasing(order, box_types)
end_time = time.time()

# Print the packed boxes
for i, box in enumerate(packed_boxes):
    print(f"Box {i+1}:")
    for item in box:
        print(f"  {item['name']} - {item['weight']}kg")
    total_weight = sum(i['weight'] for i in box)
    print(f"  Total weight: {total_weight}kg")
    print(f"  Box type: {box_types_used[i]['id']} - Capacity: {box_types_used[i]['capacity']}kg\n")

# Print the number of products processed
total_products_processed = sum(item['quantity'] for item in order)
print(f"Total products processed: {total_products_processed}")

# Print the time taken to calculate
print(f"Time taken to calculate: {end_time - start_time:.4f} seconds")
