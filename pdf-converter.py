import os
import subprocess

# Carpeta donde están los notebooks
carpeta = "./"

# Cambiar el directorio actual a la carpeta
os.chdir(carpeta)

# Recorrer todos los archivos de la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith(".ipynb"):
        print(f"Convirtiendo {archivo} a PDF...")
        try:
            subprocess.run([
                "jupyter", "nbconvert", "--to", "pdf", archivo
            ], check=True)
        except subprocess.CalledProcessError:
            print(f"Error al convertir {archivo}")
print("¡Conversión completada!")
