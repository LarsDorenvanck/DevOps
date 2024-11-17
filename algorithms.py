import json

def best_fit_decreasing(order, box_types):
    # Sort items by weight in decreasing order
    sorted_order = sorted(order, key=lambda x: x['weight'], reverse=True)
    
    # Initialize list of boxes
    boxes = []
    box_types_used = []  # To keep track of box types used
    
    # Iterate over each item in the sorted order
    for item in sorted_order:
        # Flag to check if the item has been placed in a box
        placed = False
        
        # Try to place the item in an existing box
        for index, box in enumerate(boxes):
            # Calculate the current total weight of the box
            current_box_weight = sum([i['weight'] for i in box])
            # Find the box type that matches the current box
            box_type = next((bt for bt in box_types if bt['weight'] >= current_box_weight + item['weight']), None)
            
            # Check if the item can fit in the current box
            if box_type and current_box_weight + item['weight'] <= box_type['weight']:
                # Add the item to the box
                box.append(item)
                # Mark the item as placed
                placed = True
                # Update the box type used for this box
                box_types_used[index] = box_type
                # Exit the loop since the item has been placed
                break
        
        # If the item doesn't fit in any existing box, create a new box
        if not placed:
            # Find the smallest box that can fit the item
            for box_type in box_types:
                if item['weight'] <= box_type['weight']:
                    # Create a new box with the item
                    new_box = [item]
                    # Add the new box to the list of boxes
                    boxes.append(new_box)
                    # Record the box type used
                    box_types_used.append(box_type)
                    # Exit the loop since the item has been placed
                    break
    
    return boxes, box_types_used

# Load the order from the JSON file
with open('Resources/testorder1.json', 'r') as file:
    data = json.load(file)
    order = data['order']

# Load the box types from the JSON file
with open('Resources/default_box_types.json', 'r') as file:
    box_data = json.load(file)
    box_types = box_data['box_types']

# Get the packed boxes using the best-fit-decreasing algorithm
packed_boxes, box_types_used = best_fit_decreasing(order, box_types)

# Print the packed boxes
for i, box in enumerate(packed_boxes):
    print(f"Box {i+1}:")
    for item in box:
        print(f"  {item['product']} - {item['weight']}kg")
    # Calculate and print the total weight of the box
    total_weight = sum([i['weight'] for i in box])
    # Print the box type and its capacity
    print(f"  Total weight: {total_weight}kg")
    print(f"  Box type: {box_types_used[i]['box']} - Capacity: {box_types_used[i]['weight']}kg\n")
