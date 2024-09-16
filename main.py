import ifcopenshell
import bpy
from ColumnTotalVolumesAndTotalCost import calculate_total_column_volume, calculate_total_cost

model = ifcopenshell.open("path/to/ifcfile.ifc")

unit_price_per_cubic_meter = 15459.85

total_volume = calculate_total_column_volume()
total_cost = calculate_total_cost(total_volume, unit_price_per_cubic_meter)

print(f"Total Volume of All Columns: {total_volume:.2f} cubic meters")
print(f"Total Cost: {total_cost:.2f} DKK")  # Adjust the currency unit if needed


