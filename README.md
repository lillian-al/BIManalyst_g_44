# BIManalyst group 44
#BUILD Focus Area
#Checking volumes of all columns in the building and calculating the cost for columns
#Page 6 in PM Appendix, section 6 in PM report, cost estimate
#The script calculates the total volume of all concrete columns in the structural model, and then multiplies the average unit cost of the columns with the total volume, for the total cost of all columns


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

# Optionally, add the results to Blender as a text object
bpy.ops.object.text_add()
text_obj = bpy.context.object
text_obj.data.body = (f"Total Volume of All Columns: {total_volume:.2f} cubic meters\n"
                      f"Total Cost: {total_cost:.2f} DKK")  # Adjust the currency unit if needed
text_obj.location = (0, 0, 2)  # Adjust location as needed

