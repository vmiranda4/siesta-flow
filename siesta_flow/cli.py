import click

@click.group()
def main():
    """SIESTA Flow - Automate your SIESTA workflows from CIF to results."""
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
def relax():
    """Run structure relaxation calculations."""
    click.echo("[SIESTA-FLOW] Running structure relaxation...")
    # Placeholder - run relaxation step

@main.command()
def extract():
    """Extract relaxed coordinates from .out files."""
    click.echo("[SIESTA-FLOW] Extracting relaxed coordinates...")
    # Placeholder - extract from .out to new .fdf

@main.command()
def optical():
    """Run optical properties calculation."""
    click.echo("[SIESTA-FLOW] Running optical calculations...")
    # Placeholder - use relaxed structure for optics

@main.command()
def dos():
    """Run density of states (DOS) calculation."""
    click.echo("[SIESTA-FLOW] Running DOS calculations...")
    # Placeholder - use relaxed structure for DOS

if __name__ == '__main__':
    main()