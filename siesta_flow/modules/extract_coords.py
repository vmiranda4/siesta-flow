import os

def extract_relaxed_structure_from_out(out_file_path: str)-> str:
    with open(out_file_path, 'r') as file:
        lines = file.readlines()

    output_lines = []

    # 1. Get lines from "SystemName" to "LatticeConstant"
    system_info_started = False
    for line in lines:
        if line.startswith("SystemName"):
            system_info_started = True
        if system_info_started:
            output_lines.append(line)
        if line.startswith("LatticeConstant"):
            break

    reversed_lines = reversed(lines)

    lengths = None
    angles = None

    for line in reversed_lines:
        if angles is None and "outcell: Cell angles" in line:
            angles = line.rsplit(":", 1)[-1].strip().split()
            print(angles)
        elif lengths is None and "outcell: Cell vector modules" in line:
            lengths = line.rsplit(":", 1)[-1].strip().split()
            print(lengths)
        if lengths and angles:
            break

    if not lengths or not angles:
        raise ValueError("Could not find lattice parameters in the output file.")
    
    output_lines.append("\n%block LatticeParameters\n")
    output_lines.append(" ".join(lengths + angles)+"\n")
    output_lines.append("%endblock LatticeParameters\n\n")

    # 3. Add atomic coordinates
    output_lines.append("AtomicCoordinatesFormat Fractional\n")
    output_lines.append("%block AtomicCoordinatesAndAtomicSpecies\n")

    coords_started = False

    for line in lines:
        if "outcoor: Relaxed atomic coordinates (fractional):" in line:
            coords_started = True
            continue
        if coords_started:
            if line.strip() == "":
                break
            output_lines.append(line)

    output_lines.append("%endblock AtomicCoordinatesAndAtomicSpecies\n")
    
    return "".join(output_lines)