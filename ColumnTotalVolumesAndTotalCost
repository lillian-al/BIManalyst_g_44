import bpy

# Function to calculate the total volume of columns using Blender's Object Information
def calculate_total_column_volume():
    total_volume = 0
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            # Check if the object is a column by name or other identifier
            if "column" in obj.name.lower():  # Adjust this filter based on your column naming convention
                # Make sure the object has a mesh and is visible in the viewport
                if obj.data and obj.visible_get():
                    # Get volume from dimensions panel in Blender
                    # Note: This assumes the object has been properly measured and has a volume value
                    volume = obj.dimensions.z * obj.dimensions.y * obj.dimensions.x  # This is a rough estimate
                    if volume:
                        total_volume += volume
                    else:
                        print(f"Column {obj.name}: Volume Not Available")
    
    return total_volume

# Define the unit price per cubic meter
unit_price_per_cubic_meter = 15459.85

# Get the total volume of columns
total_volume = calculate_total_column_volume()

# Calculate the total cost
total_cost = total_volume * unit_price_per_cubic_meter

# Print the total volume and cost
print(f"Total Volume of All Columns: {total_volume:.2f} cubic meters")
print(f"Total Cost: {total_cost:.2f} DKK")  # Adjust the currency unit if needed

