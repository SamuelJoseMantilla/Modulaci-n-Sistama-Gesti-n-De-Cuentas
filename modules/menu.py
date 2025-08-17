
from modules.logic import (
    crear_cuenta,
    depositar_dinero,
    retirar_dinero,
    solicitar_credito,
    pagar_credito,
    eliminar_cuenta,
    mostrar_cuentas
)
from modules.corefiles import guardar_datos
from modules.utilities import limpiar_consola

def ejecutar_menu(cuentas):
    while True:
        limpiar_consola()
        print("====== SISTEMA BANCARIO ======")
        print("1. Crear cuenta")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Solicitar crédito")
        print("5. Pagar crédito")
        print("6. Eliminar cuenta")
        print("7. Mostrar cuentas")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            crear_cuenta(cuentas)
        elif opcion == "2":
            depositar_dinero(cuentas)
        elif opcion == "3":
            retirar_dinero(cuentas)
        elif opcion == "4":
            solicitar_credito(cuentas)
        elif opcion == "5":
            pagar_credito(cuentas)
        elif opcion == "6":
            eliminar_cuenta(cuentas)
        elif opcion == "7":
            mostrar_cuentas(cuentas)
            input("\nPresione Enter para continuar...")
        elif opcion == "0":
            guardar_datos(cuentas)
            print("✅ Datos guardados. Saliendo...")
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")
