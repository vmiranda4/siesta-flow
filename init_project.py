import os

# Project base structure
structure = {
    "siesta_flow": [
        "__init__.py",
        "cli.py",
        "config.py",
        ("workflows", [
            "Snakefile",
            ("rules", [
                "__init__.py",
                "placeholder.smk"
            ])
        ]),
        ("modules", [
            "__init__.py",
            "cif_to_fdf.py",
            "extract_coords.py",
            "fill_template.py"
        ]),
    ],
    "scripts": [
        "example_run.py"
    ]
}

files = {
    "pyproject.toml": """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "siesta-flow"
version = "0.1.0"
description = "Automated workflow for SIESTA calculations from CIF to DOS/optical analysis"
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.8"
dependencies = [
    "click >=8.0",
    "numpy",
    "pandas",
    "ase",
    "pyyaml"
]

[project.scripts]
siesta-flow = "siesta_flow.cli:main"
""",
    "README.md": "# Siesta Flow\n\nA CLI-based workflow automation tool for SIESTA calculations.",
    ".gitignore": "__pycache__/\n*.pyc\n*.log\n.env\n",
}

def create_structure(base, struct):
    for entry in struct:
        if isinstance(entry, tuple):
            subdir, subentries = entry
            path = os.path.join(base, subdir)
            os.makedirs(path, exist_ok=True)
            create_structure(path, subentries)
        else:
            open(os.path.join(base, entry), "w").close()

def main():
    os.makedirs("siesta_flow", exist_ok=True)
    create_structure("siesta_flow", structure["siesta_flow"])

    os.makedirs("scripts", exist_ok=True)
    create_structure("scripts", structure["scripts"])

    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content)

    print("✅ Project skeleton created successfully!")

if __name__ == "__main__":
    main()
