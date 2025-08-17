import json
import os

CARPETA = "data"
ARCHIVO = os.path.join(CARPETA, "data.json")

def cargar_datos():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            if isinstance(datos, dict):
                return []
            return datos
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(cuentas):
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(cuentas, f, indent=4, ensure_ascii=False)
