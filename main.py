import ifcopenshell

from ColumnTotalVolumesAndTotalCost import calculate_total_column_volume

model = ifcopenshell.open("path/to/ifcfile.ifc")

CostResult = calculate_total_column_volume.checkColumnTotalVolumesAndTotalCost(model)

print("Cost result:", CostResult)

