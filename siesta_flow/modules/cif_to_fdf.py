from CifFile import ReadCif
#from periodic_table import periodic_table
from pathlib import Path

def cif_to_fdf_string(cif_path: Path) -> str:

    periodic_table = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
    'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
    'K': 19, 'Ca': 20, 'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30,
    'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36,
    'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40, 'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48,
    'In': 49, 'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54,
    'Cs': 55, 'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60, 'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65, 'Dy': 66,
    'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70, 'Lu': 71,
    'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80,
    'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86,
    'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90, 'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98,
    'Es': 99, 'Fm': 100, 'Md': 101, 'No': 102, 'Lr': 103,
    'Rf': 104, 'Db': 105, 'Sg': 106, 'Bh': 107, 'Hs': 108, 'Mt': 109, 'Ds': 110, 'Rg': 111, 'Cn': 112, 'Nh': 113, 'Fl': 114,
    'Mc': 115, 'Lv': 116, 'Ts': 117, 'Og': 118
}
    system_label = cif_path.stem
    cif = ReadCif(str(cif_path))
    block = cif.first_block()

    # Extract atom data
    atom_symbols = block['_atom_site_type_symbol']
    atom_x = block['_atom_site_fract_x']
    atom_y = block['_atom_site_fract_y']
    atom_z = block['_atom_site_fract_z']
    species = sorted(set(atom_symbols))
    number_species = len(species)
    
    species_to_number = {
        element: i for i, element in enumerate(species, start=1)
    }

    info_forma = [
        f"{species_to_number[element]} {periodic_table.get(element, 'unknown')} {element}"
        for element in species
    ]

    # Extract unit cell parameters
    a = float(block['_cell_length_a'])
    b = float(block['_cell_length_b'])
    c = float(block['_cell_length_c'])
    alpha = float(block['_cell_angle_alpha'])
    beta = float(block['_cell_angle_beta'])
    gamma = float(block['_cell_angle_gamma'])

    # Compose FDF content
    lines = []
    lines.append(f'SystemName {system_label}')
    lines.append(f'NumberOfAtoms {len(atom_symbols)}')
    lines.append(f'NumberOfSpecies {number_species}')
    lines.append('%block ChemicalSpeciesLabel')
    lines.extend(info_forma)
    lines.append('%endblock ChemicalSpeciesLabel\n')

    lines.append('#-----------------')
    lines.append('#Geometric structure')
    lines.append('#-----------------')

    lines.append('LatticeConstant 1.0 Ang\n')
    lines.append('%block LatticeParameters')
    lines.append(f'{a:.10f} {b:.10f} {c:.10f} {alpha:.10f} {beta:.10f} {gamma:.10f}')
    lines.append('%endblock LatticeParameters\n')

    lines.append('AtomicCoordinatesFormat Fractional')
    lines.append('%block AtomicCoordinatesAndAtomicSpecies')
    for element, x, y, z in zip(atom_symbols, atom_x, atom_y, atom_z):
        fx, fy, fz = float(x), float(y), float(z)
        species_num = species_to_number[element]
        lines.append(f'{fx:.10f} {fy:.10f} {fz:.10f} {species_num}')
    lines.append('%endblock AtomicCoordinatesAndAtomicSpecies')

    return "\n".join(lines)
