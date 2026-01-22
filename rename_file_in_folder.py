import os
import os
import re
from pathlib import Path

# Rutas a tus carpetas
pdfs_dir = Path("pdfs")
temario_dir = Path("temario")

# Obtener lista de archivos .ipynb en temario
temario_files = [f for f in temario_dir.iterdir() if f.suffix == ".ipynb"]

# Ordenar por el número al inicio del nombre
def get_number(f):
    match = re.match(r"(\d+)_", f.name)
    return int(match.group(1)) if match else float('inf')

temario_files.sort(key=get_number)

# Crear un mapping de nombre base -> número
name_to_number = {}
for f in temario_files:
    number = get_number(f)
    # quitar número y guion bajo
    base_name = re.sub(r"^\d+_", "", f.stem)
    name_to_number[base_name] = number

# Renombrar archivos en pdfs
for f in pdfs_dir.iterdir():
    if f.suffix in [".pdf", ".html"]:
        # quitar extensión
        base_name = f.stem
        # buscar el número correspondiente (coincidencia parcial)
        matched_number = None
        for key in name_to_number:
            if key in base_name:
                matched_number = name_to_number[key]
                break
        if matched_number is not None:
            new_name = f"{matched_number}_{base_name}{f.suffix}"
            new_path = f.parent / new_name
            print(f"Renombrando: {f.name} -> {new_name}")
            f.rename(new_path)
