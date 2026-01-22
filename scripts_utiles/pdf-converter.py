import os
import subprocess

carpeta = "./"
os.chdir(carpeta)

for archivo in os.listdir(carpeta):
    if archivo.endswith(".ipynb"):
        print(f"Convirtiendo {archivo} a PDF vía HTML...")
        try:
            # Exportar a HTML
            html_file = archivo.replace(".ipynb", ".html")
            subprocess.run([
                "jupyter", "nbconvert", "--to", "html", archivo
            ], check=True)
            # Convertir HTML a PDF usando wkhtmltopdf
            pdf_file = archivo.replace(".ipynb", ".pdf")
            subprocess.run([
                "wkhtmltopdf", html_file, pdf_file
            ], check=True)
        except subprocess.CalledProcessError:
            print(f"Error al convertir {archivo}")
print("¡Conversión completada!")