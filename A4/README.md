# Extracting IFC Element Properties: A Guide to Accessing Column Volumes with ifcopenshell
### **Overview**

In this tutorial, we'll cover how to use `ifcopenshell` to access element properties in an IFC file. Specifically, we’ll focus on extracting and calculating the total volume of columns in a building model. This guide is valuable for anyone looking to analyze IFC files for design, estimation, or building information modeling (BIM) purposes.
### **What you will learn**

- Loading an IFC file into a Python environment
- Retrieving specific elements (e.g., columns) from the model
- Accessing and calculating properties, such as total volume, of these elements
- Understanding how properties are stored in property sets

---

### **1. Set Up the Environment**
To begin, ensure that you have `ifcopenshell` installed in your Python environment. Then, import the necessary libraries in your script:

```python
import ifcopenshell
from pathlib import Path
```

- **ifcopenshell**: Provides tools to work with IFC files, allowing access to building model data.
- **Path (from pathlib)**: Offers a convenient way to handle file paths.

---

### **2. Load the IFC Model File**
We’ll start by loading the IFC file containing the building model.

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

### **3. Retrieve Specific IFC Elements (Columns) from the Model **
IFC files classify building elements by type, so if we want to access all columns in the model, we can use `model.by_type("IfcColumn").` This retrieves all column elements, making it easy to analyze properties specific to columns.

```python
columns = model.by_type("IfcColumn")
```

- **columns**: Stores all instances of `IfcColumn`, allowing us to access each one individually.

---

### **4. Access and Sum Column Volumes**
IFC properties are often stored within *property sets* (`IfcPropertySet`). To access specific properties like volume, we need to navigate through these sets and locate the property by name.

Here’s how we can retrieve and sum the volume for each column element:

```python
# Initialize total volume for columns
total_volume = 0.0

for column in columns:
    volume = None  # Initialize volume as None in case it’s not found

    # Access all property sets associated with the column
    for definition in column.IsDefinedBy:
        if definition.is_a("IfcRelDefinesByProperties"):
            property_set = definition.RelatingPropertyDefinition

            # Check if the property set is of type IfcPropertySet
            if property_set.is_a("IfcPropertySet"):
                # Iterate through properties in the set
                for prop in property_set.HasProperties:
                    if prop.Name == "Volume":
                        # Get the volume value if available
                        volume = prop.NominalValue.wrappedValue if prop.NominalValue else None
                        break
            if volume is not None:
                break  # Exit if volume is found

    # Add the volume to the total if available
    if volume is not None:
        total_volume += volume

```
**Explanation**
- **IsDefinedBy**: This attribute links an element to its property definitions.
- **IfcRelDefinesByProperties**: Identifies relationships between elements and their properties.
- **IfcPropertySet**: Contains various properties (e.g., volume, area) associated with an element.
- **Volume Property**: Within `IfcPropertySet`, we look for a property named "Volume" and retrieve its value. If found, it’s added to the total volume.

---

### **5. Display Total Volume**
Finally, we can print the total volume of all columns in the model:
```python
print(f"Total volume of all columns: {total_volume:.2f} cubic meters")
```

This output provides the total volume of columns within the model, offering valuable insights into material quantities.

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
