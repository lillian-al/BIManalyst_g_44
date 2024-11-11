To create an IDS for verifying the construction cost of concrete columns in Building #2406, here’s how the requirements can be structured based on the code you shared:

### Information Delivery Specification (IDS) Requirements

#### 1. **IFC Model General Requirements**
   - **IFC Schema Version**: Ensure compatibility with the version your tool is developed for (e.g., IFC2x3 or IFC4).

#### 2. **Entity Requirements**
   - **Required Entity**: `IfcColumn` — the IFC model must contain concrete columns, identified by `IfcColumn` entities.

#### 3. **Property Requirements for Concrete Columns**
   - **Property Set**: Each `IfcColumn` should include:
     - **Type**: Property indicating column type (e.g., "420" for small columns, "480" for big columns) based on dimensional indicators.
     - **Volume**: Property indicating the volume of each column. This value is essential for calculating costs.

#### 4. **Classification of Columns**
   - **Column Types**: Ensure that columns are correctly classified by type to distinguish small (420mm or smaller) and big (480mm or larger) columns.
   - **Column Grouping**: Each `IfcColumn` entity must be grouped by type, allowing the tool to identify columns based on type ranges for small and big categories.

#### 5. **Cost Calculation Requirements**
   - **Unit Prices**: Verify that the model aligns with the unit prices specified in the code:
     - Small columns: 17,467 DKK per cubic meter.
     - Big columns: 13,452.69 DKK per cubic meter.
   - **Total Cost Verification**: The IDS should ensure that the calculated total cost of columns, based on the sum of individual column volumes and their respective unit prices, matches the total construction cost in the project management report.

#### 6. **IDS JSON Structure Example**
Here’s how this specification might look in JSON, which a validation tool can use to enforce these rules:

```json
{
  "ifc_version": "IFC4",
  "entities": {
    "IfcColumn": {
      "required": true,
      "properties": ["Type", "Volume"],
      "classification": {
        "small_column_types": ["420", "360"],
        "big_column_types": ["480", "600"]
      }
    }
  },
  "cost_requirements": {
    "unit_prices": {
      "small": 17467.0,
      "big": 13452.69
    },
    "total_cost_verification": true
  }
}
```

This IDS structure will ensure that all essential information for cost calculation and volume classification is in place, so the model can be checked thoroughly before running the tool.
