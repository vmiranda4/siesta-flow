import os
from siesta_flow.modules import write_full_fdf

def generate_fdf_from_structure_dir(input_dir: str, calc_type: str, output_dir: str, param_overrides: dict = None):
    """
    Generates a full FDF file for a given calculation type based on the structure files in the input directory.

    Args:
        input_dir (str): Directory containing the structure files.
        calc_type (str): Type of calculation (e.g., 'relax', 'optical', 'dos').
        output_dir (str): Directory to save the generated FDF file.
        param_overrides (dict, optional): Dictionary of parameters to override in the FDF file.
    """
    if param_overrides is None:
        param_overrides = {}

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all .fdf files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".fdf"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{calc_type}.fdf")

            # Generate the FDF file
            generate_fdf(input_path, calc_type, output_path, param_overrides)

            print(f"✔ Generated: {output_path}")



def generate_fdf(input_path: str, calc_type: str, output_path: str, param_overrides: dict = None):
    """
    Create a full .fdf by appending the calculation-specific blocks to the structure from input_path.
    Args:
        input_path (str): Path to the input structure file.
        calc_type (str): Type of calculation (e.g., 'relax', 'optical', 'dos').
        output_path (str): Path to save the generated FDF file.
        param_overrides (dict, optional): Dictionary of parameters to override in the FDF file.
    """

    # Read the structure part from the input .fdf file
    with open(input_path, "r") as f:
        structure_content = f.read()

    # Get the calculation-specific blocks
    blocks = get_blocks_for_type(calc_type, param_overrides)
    
    # Combine the structure content with the calculation-specific blocks
    full_fdf_content = structure_content + "\n" + "\n".join(blocks)

    # Write the full FDF content to the output file
    with open(output_path, "w") as f:
        f.write(full_fdf_content)
    print(f"✔ Generated: {output_path}")



def get_blocks_for_type(calc_type: str, param_overrides: dict) -> list:
    """
    Define which building blocks each calculation type needs
    """
    base = [write_full_fdf.general_options_fdf(param_overrides),
            write_full_fdf.parallel_options_fdf(param_overrides),
            write_full_fdf.system_options_fdf(param_overrides)]
    if calc_type == "relax":
        return base + [write_full_fdf.relax_fdf(param_overrides)]
    elif calc_type == "optical":
        return base + [write_full_fdf.optical_fdf(param_overrides)]
    elif calc_type == "dos":
        return base + [write_full_fdf.dos_fdf(param_overrides)]
    else:
        raise ValueError(f"Unknown calculation type: {calc_type}")