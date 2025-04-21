import click

@click.group()
def main():
    """SIESTA Flow - Automate your SIESTA workflows from CIF to results.\n
    🌷  🌸  🌼  🌻  🌺\n
      ~ Siesta Flow ~\n
    🌺  🌻  🌼  🌸  🌷\n
    """
    pass

@main.command()
@click.option('--input-dir', required=True, type=click.Path(exists=True, file_okay=False), help='Directory containing .cif files.')
@click.option('--output-dir', required=True, type=click.Path(file_okay=False), help='Directory to save generated .fdf files.')
def init_fdf(input_dir, output_dir):
    """Convert .cif files to initial .fdf files."""
    click.echo(f"[SIESTA-FLOW] Generating .fdf files from .cif in '{input_dir}' -> '{output_dir}'")
    
    from siesta_flow.workflows.init_fdf import run_init_fdf
    run_init_fdf(input_dir, output_dir)


@main.command()
@click.option('--input-dir', required=True, type=click.Path(exists=True, file_okay=False), help='Directory witht the structure-only .fdf files.')
@click.option('--calc-type', required=True, type=click.Choice(['relax', 'optical', 'dos']), help='Type of calculation to prepare.')
@click.option('--output-dir', required=True, type=click.Path(file_okay=False), help='Directory to save generated .fdf files.')
@click.option('--param', multiple=True, type=(str, str), help='Override default parameters (e.g., --param MeshCutoff 300 Ry)')
def build_fdf(input_dir, calc_type, output_dir, param):
    """Build full .fdf files for a specific calculation from structure-only .fdf files."""
    click.echo(f"[SIESTA-FLOW] Building '{calc_type} '.fdf files from '{input_dir}' -> '{output_dir}'")

    from siesta_flow.workflows.full_fdf import generate_fdf_from_structure_dir

    param_overrides = dict(param) if param else {}

    generate_fdf_from_structure_dir(input_dir, calc_type, output_dir, param_overrides)

@main.command()
@click.option('--input-dir', required=True, type=click.Path(exists=True, file_okay=False), help='Directory containing .out files.')
@click.option('--output-dir', required=True, type=click.Path(file_okay=False), help='Directory to save relaxed coordinates as .fdf files.')
def extract_from_out(input_dir, output_dir):
    """Extract relaxed structures from .out files into .fdf format."""
    click.echo(f"[SIESTA-FLOW] Extracting relaxed structures from '{input_dir}' -> '{output_dir}'")
    
    from siesta_flow.workflows.extract_relaxed import run_extract_relaxed
    run_extract_relaxed(input_dir, output_dir)

if __name__ == '__main__':
    main()