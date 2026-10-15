import shutil
import unicodedata
from pathlib import Path

DESTINO = Path("pedidos_ordenados")
SEDES = ("itagui", "envigado", "sabaneta")


def _normalizar(texto):
    """'Itagüí ' -> 'itagui'."""
    texto = unicodedata.normalize("NFD", str(texto).strip().lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def crear_carpetas():
    """Crea pedidos_ordenados/ y una subcarpeta por sede."""
    for sede in SEDES:
        (DESTINO / sede).mkdir(parents=True, exist_ok=True)


def guardar_pedido_en_sede(archivo, sede):
    """Copia el archivo a pedidos_ordenados/<sede>/ sin tocar bandeja_entrada/.

    Acepta 'Itagüí', 'itagui', etc. Devuelve True si copió, False si no.
    """
    sede = _normalizar(sede)
    if sede not in SEDES:
        return False

    crear_carpetas()
    shutil.copy(archivo, DESTINO / sede / Path(archivo).name)
    return True

