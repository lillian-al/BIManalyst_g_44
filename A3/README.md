# Group 44 Tool

### About the tool
The primary problem addressed by this tool is verifying the accuracy of construction cost estimates associated with all concrete columns in Building #2406. Specifically, it aims to ensure that the total cost for concrete columns, based on their calculated volumes and corresponding costs for small and large columns, aligns with the construction cost presented in the project management report. 

The problem was identified through a review of the project management documentation for Building #2406. In the project management appendix, the cost estimates for small and large concrete columns were presented but required independent verification to confirm accuracy and prevent potential budget discrepancies.

The verification process involves using a Python-based tool that leverages the ifcOpenShell library to extract detailed data on all concrete columns from an IFC (Industry Foundation Classes) model, which is a standardized file format for BIM data. The tool automates the classification of columns into "small" and "large" categories based on their cross-sectional dimensions, allowing for accurate volume calculations for each category. By multiplying these volumes by established unit costs, the total construction cost for the columns is computed. This calculated total is then compared with the reported costs in the project documentation, providing a data-driven validation of column-related cost estimates. This outcome is essential for ensuring financial accountability and adherence to budget constraints in the project.



To run the tool, start by setting up the necessary environment. Ensure that Python is installed on your system, along with the ifcOpenShell library. If ifcOpenShell isn’t installed, you can add it by running the command `pip install ifcopenshell` in your terminal. Next, prepare your IFC model file, which should contain detailed information on all concrete columns, including geometric properties, material specifications, and property sets as required. Place this file (CES_BLD_24_06_STR.ifc) in an easily accessible directory.

Open the Python script in a text editor and locate the model_path variable. Update this variable with the exact path to your IFC model file, replacing the placeholder path with your own file location. For example, you might set it as:
`model_path = Path(r"C:\path\to\your\IFC_file.ifc")`

Once the file path is set, run the script in a Python environment or from the command line using the command:
`python main.py`

The script will automatically extract data on all concrete columns, calculate the total volumes and costs for both "small" and "large" columns, and display the results in the terminal. This output will include the total volume of each column type, the estimated cost for each category, and the overall estimated cost for all columns, providing an accurate and data-driven cost assessment.

### Advanced Building Design
What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?


The tool could be used by professionals involved in the following subjects:
- **Structural Engineering**: Structural engineers who design the layout and size of columns will find the tool useful for verifying the accuracy of their volume calculations and ensuring cost estimates match project documentation.
- **Construction Project Management**: Project managers would benefit from using the tool for budget verification and for confirming that the volume and costs for concrete columns are correct as per the project’s cost breakdown.


In order for the tool to work, certain information is required in the model. The equired information in the model includes:
- **IfcColumn:** The model must contain columns defined as *IfcColumn* elements to ensure that all relevant concrete columns are accessible for analysis.
- **IfcRelDefinesByProperties:** Relationships must link each *IfcColumn* to its associated property sets, enabling access to detailed information about each column.
- **IfcPropertySet:** Property sets associated with *IfcColumn* elements should include key properties, such as Type (for column classification) and Volume, to allow for accurate categorization and volume-based cost calculations.







