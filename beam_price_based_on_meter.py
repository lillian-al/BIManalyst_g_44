import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('IfcColumn')
print(len(things))

file = IfcStore.get_file()

# Initialize total length and cost
total_beam_length = 0
total_beam_cost = 0

# Define prices per meter for different materials (e.g., concrete, steel)
beam_material_prices = {
    'CONCRETE': 100,  # 50 currency units per meter for concrete
    'STEEL': 50     # 100 currency units per meter for steel
}

# Helper function to find the material of a beam
def get_beam_material(entity):
    if hasattr(entity, 'HasAssociations'):
        for assoc in entity.HasAssociations:
            if assoc.is_a('IfcRelAssociatesMaterial'):
                material = assoc.RelatingMaterial
                # If it's a composite material, it may have layers
                if material.is_a('IfcMaterial'):
                    return material.Name.upper()  # Returning the material name in uppercase
    return None

# Loop through each beam and calculate length and cost
for entity in file.by_type("IfcBeam"):
    beam_length = 0
    beam_material = None
    
    # Get the material of the beam
    beam_material = get_beam_material(entity)
    
    # Loop through properties to find the length
    if hasattr(entity, 'IsDefinedBy'):
        for relDefinesByProperties in entity.IsDefinedBy:
            if hasattr(relDefinesByProperties, 'RelatingPropertyDefinition'):
                if hasattr(relDefinesByProperties.RelatingPropertyDefinition, 'HasProperties'):
                    for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                        if prop.Name == 'Length':
                            beam_length = prop.NominalValue.wrappedValue
                            total_beam_length += beam_length
                            
                            # Determine the price of the beam based on its material
                            if beam_material in beam_material_prices:
                                beam_price_per_meter = beam_material_prices[beam_material]
                            else:
                                # Default price if material not found (could be handled differently)
                                beam_price_per_meter = 70  # Default price
                                
                            # Calculate the cost of this beam
                            beam_cost = beam_price_per_meter * beam_length
                            total_beam_cost += beam_cost

# Print the results
print(f"\nTotal beam length: {total_beam_length} meters")
print(f"Total beam cost: {total_beam_cost} currency units")
