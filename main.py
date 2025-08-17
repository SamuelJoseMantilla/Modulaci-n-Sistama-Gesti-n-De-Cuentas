"""
Autor: Samuel Jose Mantilla Pallares
Fecha: 17/08/2025
Descripcion: modulacion del programa sistema de gestion de cuentas bancarias.
"""
from modules.menu import ejecutar_menu
from modules.corefiles import cargar_datos

def main():
    cuentas = cargar_datos()
    ejecutar_menu(cuentas)

if __name__ == "__main__":
    main()