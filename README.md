# BIManalyst group 44

The primary goal of this use case is to verify the construction cost accuracy for concrete columns in Building #2406 as documented in the project management report. The verification process involves extracting detailed data on all concrete columns from an IFC model to calculate the total construction cost. This calculation uses volume data for each column, distinguishing between "small" and "large" columns based on cross-sectional dimensions. By multiplying the volume by established unit costs, the total column construction cost is calculated and then compared with the reported cost in the project documentation. The outcome provides a data-driven validation of column-related cost estimates, which is essential for ensuring financial accountability and adherence to budget constraints in the project.



This use case is designed for stakeholders involved in project management, cost estimation, and financial auditing of the construction project. Specifically, project managers and cost estimators benefit from this process by ensuring that construction costs are accurately represented, which is crucial for maintaining the project budget. Financial auditors can use this verification to assess the accuracy and transparency of cost documentation, contributing to accountability in financial reporting.



This use case requires expertise in several key areas outside of Building Information Modeling (BIM):
- **Cost Estimation:** Knowledge of standard pricing for concrete elements, particularly for small and large columns, is needed to apply accurate unit costs.
- **Structural Engineering:** An understanding of column sizes and structural classifications is necessary to correctly categorize columns by size and type, as structural standards often influence column dimensions.
- **Financial Analysis:** Familiarity with cost verification methods and construction budgeting ensures the verification aligns with financial management practices.
- **Indstry Standards Knowledge:** Awareness of industry-specific standards, such as cost-per-square-meter rates (from resources like Molio.dk), enables standardized and reliable cost estimates.



The script utilizes several core IFC concepts to access and manipulate data.
1. **IfcColumn:**
   The script retrieves all columns from the model using model.by_type("IfcColumn"). This IFC entity type (IfcColumn) represents individual structural columns within the building model. The script iterates through each instance of IfcColumn to access and classify columns based on properties such as type and volume.
2. **IfcRelDefinesByProperties:**
   The IfcRelDefinesByProperties relationship is used to link each column to its associated properties. In the script, this relationship is explored to locate property sets (IfcPropertySet) attached to each IfcColumn. This structure is essential for gathering specific data about column types and volumes for cost estimation.
4. **IfcPropertySet:**
5. **Ifc**
6. **Classification**


This use case involves cost verification analysis, which first of all includes calculating total volumes for different column types and validating costs using established unit rates. This analysis ensures that calculated costs match those reported, allowing stakeholders to address any discrepancies. By conducting a detailed cost assessment, the use case contributes to compliance in project financial reporting, reinforcing transparency in construction spending. Furthermore, accurate classification of column types (small vs. large) is essential for applying the correct unit cost and verifying construction budgeting accurately.



The focus is exclusively on concrete columns within Building #2406. These are categorized into "small" and "large" based on the cross-sectional dimensions, which typically correspond to industry standards for column sizing (e.g., columns with 420mm or 360mm cross-sections classified as small, and 480mm or 600mm classified as large). Accurate classification ensures that each column type is assigned the appropriate unit cost during the estimation.




The script relies on the following data inputs to function effectively:
- The IFC model file, which includes geometric data, material properties, and associated attributes for all concrete columns in Building #2406.
- Established unit costs for different column sizes, to calculate total costs accurately. These rates are indicated in the project management report appendix, which are drawn from Molio.dk
- Volume of each column, which is extracted using ifcopenshell.
- Column classification data, which is described in the project management report appendix.




For this cost verification use case to proceed, certain conditions must be met. The structural model must first of all be finalized, with all concrete columns and their properties fully defined in the IFC model. Unit prices for both small and large concrete columns must also be confirmed according to industry standards, like Molio.dk, to ensure consistency in cost estimation. Lastly, the classification system for column sizes should be predefined to allow accurate sorting and cost application for small vs. large columns.


