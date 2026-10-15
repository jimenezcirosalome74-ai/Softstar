import os
from pathlib import Path

# Importamos las funciones desarrolladas por los compañeros
from lectores import leer_pedido
from sedes import identificar_sede
from organizar import guardar_pedido_en_sede

def procesar_bandeja_entrada():
    """
    Recorre la carpeta bandeja_entrada, identifica la sede de cada pedido,
    lo copia a su carpeta correspondiente y genera el resumen.txt.
    """
    ruta_bandeja = Path("bandeja_entrada")
    
    if not ruta_bandeja.exists():
        print("❌ La carpeta 'bandeja_entrada' no existe. Ejecuta primero 'python generar_pedidos.py'.")
        return

    # Contadores para el reporte
    conteo_sedes = {
        "itagui": 0,
        "envigado": 0,
        "sabaneta": 0,
        "revisar": 0
    }
    
    total_procesados = 0

    print("🚀 Iniciando procesamiento de la bandeja de entrada...\n")

    # Recorrer todos los archivos dentro de bandeja_entrada
    for archivo in ruta_bandeja.iterdir():
        # Validar que sea un archivo y omitir archivos ocultos del sistema (ej. .DS_Store)
        if archivo.is_file() and not archivo.name.startswith('.'):
            total_procesados += 1
            
            # 1. Leer contenido
            contenido = leer_pedido(archivo)
            
            # 2. Identificar la sede y normalizar a minúsculas sin tildes si es necesario
            sede = identificar_sede(contenido, archivo)
            if isinstance(sede, str):
                sede = sede.strip().lower().replace("ü", "u").replace("í", "i")
            else:
                sede = "revisar"
            
            # 3. Guardar/copiar el archivo a su sede
            guardar_pedido_en_sede(archivo, sede)
            
            # Actualizar conteo
            if sede in conteo_sedes:
                conteo_sedes[sede] += 1
            else:
                conteo_sedes["revisar"] += 1

    # 4. Generar el archivo resumen.txt
    escribir_resumen(total_procesados, conteo_sedes)
    
    print("\n✅ ¡Proceso completado con éxito!")


def escribir_resumen(total, conteo):
    """Genera el archivo resumen.txt con las métricas del lote 1."""
    contenido_resumen = f"""=== RESUMEN DE PROCESAMIENTO - LOTE 1 ===
Total de pedidos procesados: {total}
- Itagüí: {conteo.get('itagui', 0)}
- Envigado: {conteo.get('envigado', 0)}
- Sabaneta: {conteo.get('sabaneta', 0)}
- Por revisar/Desconocidos: {conteo.get('revisar', 0)}
"""
    with open("resumen.txt", "w", encoding="utf-8") as f:
        f.write(contenido_resumen)
        
    print("📄 Archivo 'resumen.txt' generado exitosamente.")


if __name__ == "__main__":
    procesar_bandeja_entrada()