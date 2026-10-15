import json
import csv
from pathlib import Path

def leer_txt(ruta_archivo: Path) -> str:
    """Lee un archivo de texto plano (.txt) y retorna su contenido completo."""
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        return f.read()

def leer_csv(ruta_archivo: Path) -> list:
    """Lee un archivo CSV (.csv) y retorna su contenido como una lista de diccionarios."""
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def leer_json(ruta_archivo: Path) -> dict:
    """Lee un archivo JSON (.json) y retorna su contenido como un diccionario."""
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def leer_pedido(ruta_archivo: Path):
    """
    Función general que detecta la extensión del archivo y 
    ejecuta el lector correspondiente (.txt, .csv o .json).
    """
    ruta = Path(ruta_archivo)
    extension = ruta.suffix.lower()
    
    if extension == '.txt':
        return leer_txt(ruta)
    elif extension == '.csv':
        return leer_csv(ruta)
    elif extension == '.json':
        return leer_json(ruta)
    else:
        raise ValueError(f"Formato de archivo no soportado: {extension}")
    


    # Para importar esta función en otro archivo, puedes usar:
    # from lectores import leer_pedido