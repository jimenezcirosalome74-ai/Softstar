# 📓 Bitácora R1 · Estiven Garcés Abreo

> 🛵 Proyecto: Rápido Paisa · Requerimiento 1 (R1)
> 📅 Fecha: 15/10/2026

## 🎫 Ticket que hice

#39 Implementar las funciones de lectura de archivos (.txt, .csv, .json) en el módulo lectores.py.

## 🧩 Problema que encontré y cómo lo resolví

Tuve inconvenientes iniciales al crear la rama debido a espacios en el nombre, lo cual solucioné usando guiones y barras diagonales. Además, al estructurar la lectura de archivos, el formato de extensión presentaba diferencias de mayúsculas, por lo que agregué `.lower()` para normalizarlo correctamente.

## 🤖 Uso de IA

Usé la IA para repasar la sintaxis exacta de `csv.DictReader` y asegurar el manejo correcto de la codificación UTF-8 en los tres formatos. Tuve que corregir la forma en que se retornaban los diccionarios para que fueran compatibles con el resto del equipo.