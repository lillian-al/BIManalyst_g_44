# Volumes and Cost Tutorial
### **How This Script Works**

The script is structured into several key sections. First, it loads and validates the IFC file, ensuring we have a valid path to work with. Then, it extracts column elements from the model and organizes them by their type. Each column type is categorized as either a "small" or "big" column based on its size, with corresponding unit prices. Next, it calculates the volume for each column and sums up the volume and price totals based on the type. Finally, it displays a summary of the total volumes and costs for each category of columns.

### **Steps to the code**

1. loading the IFC model in Python using ifcopenshell.

2. Extracts column data and access properties such as type and volume.

3. Categorizes columns based on type and calculate cumulative volume.

4. Defines costs per unit volume for different types of columns.

5. Calculates total costs based on these volumes and unit prices.

6. Outputs a summary with total volumes and costs for different column types.




### **Breakdown of the provided code:**

---

### **1. Import Libraries**
The code starts by importing `ifcopenshell` to work with IFC files and `Path` from `pathlib` to handle file paths.
```python
import ifcopenshell
from pathlib import Path
```

- **ifcopenshell**: Provides tools to work with IFC files, allowing access to building model data.
- **Path (from pathlib)**: Offers a convenient way to handle file paths.

---

### **2. Load the IFC Model File**

```python
model_path = input("Enter the IFC file path (or press Enter to use default): ")
if not model_path:
    model_path = Path(r"C:\Users\lilli\OneDrive\Desktop\DTU\Kandidat\OpenBIM\CES_BLD_24_06_STR.ifc")
else:
    model_path = Path(model_path)

if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

model = ifcopenshell.open(model_path)
```

- **User Input for Model Path**: Prompts the user to input a path to the IFC model file. If the user presses Enter without providing a path, it defaults to a predefined location.
- **model_path**: Converts the provided file path into a `Path` object, making it easy to verify and handle.
- **File Existence Check**: Checks if the specified file exists. If the file isn’t found, a `FileNotFoundError` is raised with a message indicating the missing file path.
- **ifcopenshell.open**: Opens the IFC model file using `ifcopenshell`, enabling extraction and analysis of data.

---

### **3. Retrieve IFC Elements from the Model**
The code then extracts all `IfcColumn` elements from the model.
```python
columns = model.by_type("IfcColumn")
```

- **columns**: Collects all elements of type `IfcColumn` in the model, setting the stage for further analysis.

---

### **4. Initialize Totals for Volume and Pricing**
Variables are initialized to store total volumes and costs for “small” and “big” columns.
```python
total_small_volume = 0.0
total_big_volume = 0.0

unit_price_small = 17467.0  # Unit price for small columns
unit_price_big = 13452.69    # Unit price for big columns
```

- **total_small_volume and total_big_volume**: Store cumulative volumes for small and big columns, respectively.
- **unit_price_small and unit_price_big**: Define the cost per cubic meter for small and big columns.

---

### **5. Define a Dictionary for Column Types**
The code creates a dictionary to store column types and uses it to categorize columns based on size.
```python
column_types = {}
```

- **column_types**: A dictionary to categorize columns based on their type (small or big), associating them with their unique indices.

---

### **6. Loop Through Columns and Extract Properties**
The code iterates through each column, extracting its type information to group them as “small” or “big.” For each IfcColumn, it inspects the IfcPropertySet to check for a "Type" property, which determines the column category.
```python
for i, column in enumerate(columns, start=1):
    column_type = None  # Initialize column_type

    for definition in column.IsDefinedBy:
        if definition.is_a("IfcRelDefinesByProperties"):
            property_set = definition.RelatingPropertyDefinition
            
            if property_set.is_a("IfcPropertySet"):
                for prop in property_set.HasProperties:
                    if prop.Name == "Type":
                        column_type = prop.NominalValue.wrappedValue if prop.NominalValue else 'None'

    if column_type:
        # Store the column index in the dictionary
        if column_type not in column_types:
            column_types[column_type] = []
        column_types[column_type].append(i)
```

- **column_type**: Determines the type of each column by accessing its "Type" property within property sets.
- **Dictionary Update**: Stores each column's index based on its type, categorizing them for further analysis.

---

### **7. Determine Ranges for Small and Big Columns**
The code categorizes columns as “small” or “big” based on the type, grouping columns in ranges for efficient calculation.
```python
small_column_ranges = []
big_column_ranges = []

for col_type, indices in column_types.items():
    ranges = []
    start = indices[0]
    
    for j in range(1, len(indices)):
        if indices[j] != indices[j - 1] + 1:  # Check for breaks in sequence
            ranges.append((start, indices[j - 1]))
            start = indices[j]
    ranges.append((start, indices[-1]))  # Append the last range

    # Check the column type to determine small or big
    if '420' in col_type or '360' in col_type:  # Assuming small columns are 420mm or smaller
        small_column_ranges.extend(ranges)
    elif '480' in col_type or '600' in col_type:  # Assuming big columns are 480mm or larger
        big_column_ranges.extend(ranges)
```

- **Range Calculation**: Groups consecutive indices to identify continuous ranges, storing these in either small or big column lists based on the type (e.g., '420' or '360' for small columns, '480' or '600' for big columns).

---

### **8. Calculate Volumes by Column Range**
The code iterates through the columns, finds their volume, and checks if the column index falls within the range of either small or big columns. It then adds the volume to the appropriate total.
```python
for i, column in enumerate(columns, start=1):
    psets = column.IsDefinedBy
    volume = None

    for definition in psets:
        if definition.is_a("IfcRelDefinesByProperties"):
            property_set = definition.RelatingPropertyDefinition
            if property_set.is_a("IfcPropertySet"):
                for prop in property_set.HasProperties:
                    if prop.Name == "Volume":
                        volume = prop.NominalValue.wrappedValue if prop.NominalValue else None
                        break
            if volume is not None:
                break

    # Check if the column index falls into small columns range
    for small_range in small_column_ranges:
        if small_range[0] <= i <= small_range[1]:
            if volume is not None:
                total_small_volume += volume
            break

    # Check if the column index falls into big columns range
    for big_range in big_column_ranges:
        if big_range[0] <= i <= big_range[1]:
            if volume is not None:
                total_big_volume += volume
            break
```

- **Volume Calculation**: Searches each column’s property sets for the "Volume" property, adding it to either `total_small_volume` or `total_big_volume` depending on which range the column falls into.

---

### **9. Calculate Prices and Total Cost**
The total costs for small and big columns are calculated based on their volumes and unit prices, with an overall total cost for all columns.
```python
total_small_price = total_small_volume * unit_price_small
total_big_price = total_big_volume * unit_price_big

total_cost = total_small_price + total_big_price
```

- **total_small_price and total_big_price**: Multiply each volume total by its unit price.
- **total_cost**: Sums the prices for all columns, giving the overall cost.

---

### **10. Output Results**
The results are printed to the console, providing a breakdown of the total volumes and costs for small and big columns and the total cost.
```python
print(f"Total volume of big columns: {total_big_volume:.2f} cubic meters")
print(f"Total volume of small columns: {total_small_volume:.2f} cubic meters")

print(f"Total price of big columns: {total_big_price:.2f} DKK")
print(f"Total price of small columns: {total_small_price:.2f} DKK")

print(f"Total cost of all columns: {total_cost:.2f} DKK")
```

- **Output**: Displays the calculated volumes and prices for both small and big columns, followed by the total cost. Each result is formatted to two decimal places for readability.

---

### **Example Output**
Once executed, the script might output something similar to:
```python
Total volume of big columns: 50.00 cubic meters
Total volume of small columns: 30.00 cubic meters
Total price of big columns: 672634.50 DKK
Total price of small columns: 524010.00 DKK
Total cost of all columns: 1196644.50 DKK
```
---

This code systematically categorizes columns, calculates their volumes and total costs, and provides a summary, making it useful for analyzing column costs based on volume and type.
