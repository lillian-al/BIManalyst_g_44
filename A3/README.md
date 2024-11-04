# Group 44 Use Case

The primary problem addressed by this tool is verifying the accuracy of construction cost estimates associated with all concrete columns in Building #2406. Specifically, it aims to ensure that the total cost for concrete columns, based on their calculated volumes and corresponding costs for small and large columns, aligns with the construction cost presented in the project management report. 

The problem was identified through a review of the project management documentation for Building #2406. In the project management appendix, the cost estimates for small and large concrete columns were presented but required independent verification to confirm accuracy and prevent potential budget discrepancies.

The verification process involves using a Python-based tool that leverages the ifcOpenShell library to extract detailed data on all concrete columns from an IFC (Industry Foundation Classes) model, which is a standardized file format for BIM data. The tool automates the classification of columns into "small" and "large" categories based on their cross-sectional dimensions, allowing for accurate volume calculations for each category. By multiplying these volumes by established unit costs, the total construction cost for the columns is computed. This calculated total is then compared with the reported costs in the project documentation, providing a data-driven validation of column-related cost estimates. This outcome is essential for ensuring financial accountability and adherence to budget constraints in the project.




The script utilizes several core IFC concepts to access and manipulate data.
1. **IfcColumn:**
   The script retrieves all columns from the model using model.by_type("IfcColumn"). This IFC entity type (IfcColumn) represents individual structural columns within the building model. The script iterates through each instance of IfcColumn to access and classify columns based on properties such as type and volume.
2. **IfcRelDefinesByProperties:**
   The IfcRelDefinesByProperties relationship is used to link each column to its associated properties. In the script, this relationship is explored to locate property sets (IfcPropertySet) attached to each IfcColumn. This structure is essential for gathering specific data about column types and volumes for cost estimation.
3. **IfcPropertySet:**
   Within IfcRelDefinesByProperties, the script accesses IfcPropertySet instances, which contain various properties associated with the columns. The script specifically searches for two properties in these sets, which is type and volume.
   Type determines the classification of each column (e.g., small or large) based on its type description (e.g., 420mm or 480mm). This classification influences the unit price applied to the column.
   The Volume property, when available, provides the cubic measurement of each column. This is crucial for calculating the total construction cost as it is directly multiplied by the respective unit price.
5. **Classification**
   While not strictly an IFC concept, the script applies custom logic to classify columns into small or large categories based on the type property. By checking for specific dimension indicators within the type (e.g., '420', '360' for small, and '480', '600' for large), the script organizes columns into ranges and accumulates their volumes for cost estimation purposes.




The script relies on the following data inputs to function effectively:
- The IFC model file, which includes geometric data, material properties, and associated attributes for all concrete columns in Building #2406.
- Established unit costs for different column sizes, to calculate total costs accurately. These rates are indicated in the project management report appendix, which are drawn from Molio.dk
- Volume of each column, which is extracted using ifcopenshell.
- Column classification data, which is described in the project management report appendix.











