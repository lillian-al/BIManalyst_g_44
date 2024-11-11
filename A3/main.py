import ifcopenshell
from pathlib import Path
from column_cost import column_cost  # Import the function from the other module

# Prompt the user to specify an IFC file path or use the default location
model_path = input("Enter the IFC file path (or press Enter to use default): ")
if not model_path:
    # Default path
    model_path = Path(r"C:\Users\lilli\OneDrive\Desktop\DTU\Kandidat\OpenBIM\CES_BLD_24_06_STR.ifc")
else:
    model_path = Path(model_path)

# Check if the file exists
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

# Load the model
model = ifcopenshell.open(model_path)

# Call the function to calculate the costs
small_columns, big_columns, total_cost = column_cost(model)

# Print the results
print(f"Total volume of small columns: {small_columns[0]:.2f} cubic meters")
print(f"Total volume of big columns: {big_columns[0]:.2f} cubic meters")
print(f"Total price of small columns: {small_columns[1]:.2f} DKK")
print(f"Total price of big columns: {big_columns[1]:.2f} DKK")
print(f"Total cost of all columns: {total_cost:.2f} DKK")
