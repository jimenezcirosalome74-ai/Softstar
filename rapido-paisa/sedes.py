
import json
import csv
import re
import unicodedata
from pathlib import Path


def normalizar(texto):
    """Quita tildes, espacios sobrantes y diferencias de mayúsculas."""
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        letra for letra in texto
        if unicodedata.category(letra) != "Mn"
    )
    return texto


def reconocer_sede(texto):
    """Reconoce el municipio en un texto o nombre de archivo."""

    texto = normalizar(texto)

    # Separamos por espacios, guiones, puntos y otros signos.
    palabras = re.findall(r"[a-z0-9]+", texto)

    sedes = {
        "itagui": "Itagüí",
        "envigado": "Envigado",
        "env": "Envigado",
        "sabaneta": "Sabaneta",
        "bello": "Bello"
    }

    encontradas = []
    for palabra in palabras:
        if palabra in sedes and sedes[palabra] not in encontradas:
            encontradas.append(sedes[palabra])

    if len(encontradas) == 0:
        return None

    if len(encontradas) > 1:
        return "INCONSISTENTE"

    return encontradas[0]


def leer_pedido(ruta):
    """Lee el contenido de un pedido TXT, JSON o CSV."""

    try:
        contenido = ruta.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError):
        return None

    if not contenido.strip():
        return None

    try:
        if ruta.suffix.lower() == ".json":
            datos = json.loads(contenido)

            if not isinstance(datos, dict):
                return None

            return datos

        elif ruta.suffix.lower() == ".csv":
            from io import StringIO

            lector = csv.DictReader(StringIO(contenido))
            fila = next(lector, None)

            if fila is None:
                return None

            return fila

        elif ruta.suffix.lower() == ".txt":
            datos = {}

            for linea in contenido.splitlines():
                if ":" in linea:
                    clave, valor = linea.split(":", 1)
                    datos[clave.strip().lower()] = valor.strip()

            return datos if datos else None

    except (json.JSONDecodeError, csv.Error, ValueError):
        return None

    return None


def determinar_sede(datos, nombre_archivo):
    """Determina la sede y detecta posibles inconsistencias."""

    if not isinstance(datos, dict):
        return {
            "sede": "Desconocida",
            "estado": "Revisar",
            "motivo": "No se pudieron leer los datos del pedido."
        }

    # Buscamos la sede dentro de los datos.
    sede_contenido = None

    for clave, valor in datos.items():
        if normalizar(clave) == "sede":
            sede_contenido = reconocer_sede(valor)
            break

    # Buscamos la sede escrita en el nombre del archivo.
    sede_archivo = reconocer_sede(Path(nombre_archivo).stem)

    # Si aparecen varios municipios en una misma fuente.
    if sede_contenido == "INCONSISTENTE":
        return {
            "sede": "Desconocida",
            "estado": "Revisar",
            "motivo": "El contenido menciona varias sedes."
        }

    if sede_archivo == "INCONSISTENTE":
        return {
            "sede": "Desconocida",
            "estado": "Revisar",
            "motivo": "El nombre del archivo menciona varias sedes."
        }

    # Si falta la sede en el contenido, usamos el nombre
    # solo como pista, no como confirmación definitiva.
    if sede_contenido is None:
        if sede_archivo is not None:
            return {
                "sede": sede_archivo,
                "estado": "Revisar",
                "motivo": "La sede aparece en el nombre, pero falta en el contenido."
            }

        return {
            "sede": "Desconocida",
            "estado": "Revisar",
            "motivo": "No se encontró la sede en el pedido."
        }

    # Comparamos el contenido con el nombre del archivo.
    if sede_archivo is not None and sede_archivo != sede_contenido:
        return {
            "sede": sede_contenido,
            "estado": "Revisar",
            "motivo": "La sede del archivo no coincide con su contenido."
        }

    # Bello existe en el lote 2, pero está fuera del grupo solicitado.
    if sede_contenido == "Bello":
        return {
            "sede": "Bello",
            "estado": "Revisar",
            "motivo": "Sede fuera de las tres solicitadas."
        }

    return {
        "sede": sede_contenido,
        "estado": "Correcto",
        "motivo": "Sede identificada correctamente."
    }


def main():
    carpeta = Path("bandeja_entrada")

    if not carpeta.exists():
        print("No se encontró la carpeta bandeja_entrada.")
        return

    for ruta in carpeta.iterdir():
        if ruta.suffix.lower() not in [".txt", ".csv", ".json"]:
            continue

        datos = leer_pedido(ruta)
        resultado = determinar_sede(datos, ruta.name)

        print(
            f"Archivo: {ruta.name}\n"
            f"Sede: {resultado['sede']}\n"
            f"Estado: {resultado['estado']}\n"
            f"Motivo: {resultado['motivo']}\n"
            f"{'-' * 45}"
        )


if __name__ == "__main__":
    main()