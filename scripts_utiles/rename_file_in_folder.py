import os
import re
from pathlib import Path
from difflib import SequenceMatcher

pdfs_dir = Path("pdfs")
temario_dir = Path("temario")

# Función para limpiar el nombre de comparaciones
def clean_name(name):
    name = name.lower()
    name = re.sub(r"[\s_]+", "", name)      # quitar espacios y guiones bajos
    return name

# Obtener lista de archivos .ipynb
temario_files = [f for f in temario_dir.iterdir() if f.suffix == ".ipynb"]

# Ordenar por número al inicio
def get_number(f):
    match = re.match(r"(\d+)", f.name)
    return int(match.group(1)) if match else float('inf')

temario_files.sort(key=get_number)

# Renombrar archivos en pdfs
for pdf_file in pdfs_dir.iterdir():
    if pdf_file.suffix not in [".pdf", ".html"]:
        continue

    pdf_clean = clean_name(pdf_file.stem)
    best_match = None
    best_ratio = 0

    for temario_file in temario_files:
        temario_clean = clean_name(re.sub(r"^\d+_", "", temario_file.stem))
        ratio = SequenceMatcher(None, pdf_clean, temario_clean).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = temario_file

    # Solo renombrar si la coincidencia es bastante buena (>0.6)
    if best_match and best_ratio > 0.6:
        number = get_number(best_match)
        new_name = f"{number}_{pdf_file.name}"
        new_path = pdf_file.parent / new_name
        print(f"Renombrando: {pdf_file.name} -> {new_name}")
        pdf_file.rename(new_path)
