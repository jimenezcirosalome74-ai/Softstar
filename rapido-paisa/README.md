# 🛵 Rápido Paisa · Automatización de pedidos

## 📦 ¿Qué hace el proyecto?

Rápido Paisa es una empresa de domicilios con sedes en **Itagüí, Envigado y
Sabaneta** 📍. Este sistema toma los pedidos que llegan desordenados en una sola
carpeta y los organiza por sede ✅.

## 🔧 Prerrequisitos

- 🐍 Python 3 instalado (comprobar con `python --version`)
- 🌿 Git
- 🚫 No hay que instalar librerías: solo se usa la biblioteca estándar de Python.

## ▶️ Cómo ejecutarlo

1. 📥 Clonar el repositorio:

```bash
   git clone https://github.com/jimenezcirosalome74-ai/Softstar.git
   cd Softstar/rapido-paisa
```

2. 🗂️ Generar los pedidos de ejemplo del cliente (crea la carpeta `bandeja_entrada/`):

```bash
   python generar_pedidos.py
```

3. 🚀 Organizar los pedidos por sede:

```bash
   python organizar.py
```

4. 🎉 Revisar el resultado: aparece la carpeta `pedidos_ordenados/` con una
   carpeta por sede. `bandeja_entrada/` no se modifica.

> 💡 En Mac o Linux, si `python` no funciona, usa `python3`.

## 🗺️ Estructura del proyecto

- 🧠 `organizar.py`: programa principal, es el que se ejecuta
- 📍 `sedes.py`: funciones para reconocer la sede
- 📖 `lectores.py`: funciones para leer archivos .txt, .csv y .json
- 🏭 `generar_pedidos.py`: script del cliente, no se modifica
- 📝 `docs/bitacora/`: bitácoras individuales del equipo

## 📝 Bitácoras

Cada integrante escribe su bitácora en `docs/bitacora/tu-nombre.md`,
usando como base `docs/bitacora/PLANTILLA.md`.
