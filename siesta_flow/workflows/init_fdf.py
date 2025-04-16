import os
from pathlib import Path
from siesta_flow.modules.cif_to_fdf import cif_to_fdf_string

def run_init_fdf(input_dir: str, output_dir: str):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    cif_files = list(input_path.glob("*.cif"))

    if not cif_files:
        print(f"No .cif files found in {input_dir}")
        return

    for cif_file in cif_files:
        try:
            structure_name = cif_file.stem
            fdf_data = cif_to_fdf_string(cif_file)  # assuming this returns a string or list of lines
            output_file = output_path / f"{structure_name}.fdf"

            with open(output_file, "w") as f:
                f.write(fdf_data if isinstance(fdf_data, str) else "\n".join(fdf_data))

            print(f"✔ Converted: {cif_file.name} → {output_file.name}")

        except Exception as e:
            print(f"❌ Failed to convert {cif_file.name}: {e}")
