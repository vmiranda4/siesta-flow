import os
from siesta_flow.modules.extract_coords import extract_relaxed_structure_from_out

def run_extract_relaxed(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".out"):
            out_path = os.path.join(input_dir, file_name)
            fdf_name = file_name.replace(".out", "_relaxed.fdf")
            output_path = os.path.join(output_dir, fdf_name)

            try:
                content = extract_relaxed_structure_from_out(out_path)
                with open(output_path, "w") as f:
                    f.write(content)
                print(f"✔ Extracted: {out_path} → {output_path}")
            except Exception as e:
                print(f"❌ Failed to extract from {out_path}: {e}")