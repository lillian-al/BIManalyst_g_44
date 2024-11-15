import ifcopenshell
from pathlib import Path
from column_cost import column_cost  # Import the function from the other module

def column_cost(model):
    """
    Calculate the total volume and price for small and large columns in an IFC model.
    
    :param model: The IFC model object loaded using ifcopenshell.open.
    :return: A tuple containing the total volume and price for small columns, 
             the total volume and price for large columns, and the total cost.
    """
    
    # Get all columns from the model
    columns = model.by_type("IfcColumn")

    # Initialize total volumes and prices
    total_small_volume = 0.0
    total_big_volume = 0.0

    # Define unit prices
    unit_price_small = 17467.0  # Unit price for small columns
    unit_price_big = 13452.69   # Unit price for big columns

    # Dictionary to store column types and their indices
    column_types = {}

    # Loop through each column and extract its properties
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

    # Determine ranges for small and big columns based on their types
    small_column_ranges = []
    big_column_ranges = []

    for col_type, indices in column_types.items():
        # Create ranges from indices
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

    # Loop through the ranges and calculate volumes
    for i, column in enumerate(columns, start=1):
        # Get the property sets defined for this column
        psets = column.IsDefinedBy

        # Loop through the property sets to find the volume
        volume = None
        for definition in psets:
            if definition.is_a("IfcRelDefinesByProperties"):
                property_set = definition.RelatingPropertyDefinition
                if property_set.is_a("IfcPropertySet"):
                    for prop in property_set.HasProperties:
                        if prop.Name == "Volume":
                            volume = prop.NominalValue.wrappedValue if prop.NominalValue else None
                            break  # Break after finding the volume property
                if volume is not None:
                    break  # Break if volume is found

        # Check if the column index falls into small columns range
        for small_range in small_column_ranges:
            if small_range[0] <= i <= small_range[1]:
                if volume is not None:
                    total_small_volume += volume  # Add the volume to the total for small columns
                break  # Break after finding the range

        # Check if the column index falls into big columns range
        for big_range in big_column_ranges:
            if big_range[0] <= i <= big_range[1]:
                if volume is not None:
                    total_big_volume += volume  # Add the volume to the total for big columns
                break  # Break after finding the range

    # Calculate prices
    total_small_price = total_small_volume * unit_price_small
    total_big_price = total_big_volume * unit_price_big

    # Calculate total cost of all columns
    total_cost = total_small_price + total_big_price

    # Return results
    return (total_small_volume, total_small_price), (total_big_volume, total_big_price), total_cost
