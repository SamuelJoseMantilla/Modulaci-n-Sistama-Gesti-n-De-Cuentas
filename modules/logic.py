import random
import time
from modules.corefiles import guardar_datos
from modules.utilities import limpiar_consola


def _get_cuenta(cuentas, numeroCuenta):
    for c in cuentas:
        if c.get("numeroCuenta") == numeroCuenta:
            return c
    return None

def _numero_cuenta_unico(cuentas):
    intentos = 0
    while True:
        intentos += 1
        if intentos > 200000:
            raise RuntimeError("No se pudo generar número de cuenta único.")
        n = random.randint(1000, 4000)
        if _get_cuenta(cuentas, n) is None:
            return n

def _id_producto_unico(cuentas):
    intentos = 0
    while True:
        intentos += 1
        if intentos > 200000:
            raise RuntimeError("No se pudo generar id de producto único.")
        pid = random.randint(1000, 4000)
        usado = False
        for c in cuentas:
            for p in c.get("productos", []):
                if p.get("idProducto") == pid:
                    usado = True
                    break
            if usado:
                break
        if not usado:
            return pid

def _siguiente_id_credito(cuenta):
    if not cuenta.get("creditos"):
        return 1
    return max((c.get("idProducto", 0) for c in cuenta["creditos"]), default=0) + 1

def crear_cuenta(cuentas):
    limpiar_consola()
    print("=== CREAR CUENTA ===")
    titular = input("Nombre completo del titular: ").strip()
    cc = input("Cédula (CC): ").strip()
    email = input("Correo electrónico: ").strip()
    while True:
        try:
            edad = int(input("Edad: ").strip())
            break
        except ValueError:
            print("Edad inválida. Intenta de nuevo.")
    movil = input("Teléfono móvil: ").strip()
    fijo = input("Teléfono fijo (si no tiene, deja vacío): ").strip()
    pais = input("País: ").strip()
    departamento = input("Departamento / Estado: ").strip()
    ciudad = input("Ciudad: ").strip()
    direccion = input("Dirección: ").strip()

    numeroCuenta = _numero_cuenta_unico(cuentas)
    idProducto = _id_producto_unico(cuentas)
    producto_tipo = "Cuenta de Ahorros"

    cuenta = {
        "numeroCuenta": numeroCuenta,
        "titular": titular,
        "CC": cc,
        "Correo": email,
        "Edad": edad,
        "Contacto": {"Movil": movil, "Fijo": fijo},
        "Ubicacion": {"Pais": pais, "Departamento": departamento, "Ciudad": ciudad, "Direccion": direccion},
        "productos": [
            {
                "idProducto": idProducto,
                "tipo": producto_tipo,
                "Saldo": 0.0,
                "Estado": "Activo",
                "Historial": []
            }
        ],
        "creditos": []
    }

    cuentas.append(cuenta)
    guardar_datos(cuentas)
    print(f"\n Cuenta creada correctamente.")
    print(f"Número de cuenta: {numeroCuenta}")
    print(f"ID del producto (guárdalo): {idProducto} -> {producto_tipo}")
    input("\nPresiona Enter para continuar...")


def depositar_dinero(cuentas):
    limpiar_consola()
    print("=== DEPOSITAR DINERO ===")
    try:
        numero = int(input("Número de cuenta: ").strip())
    except ValueError:
        print("Número inválido.")
        input("Enter para continuar...")
        return
    cuenta = _get_cuenta(cuentas, numero)
    if not cuenta:
        print("Cuenta no encontrada.")
        input("Enter para continuar...")
        return

    productos = cuenta.get("productos", [])
    if not productos:
        print("La cuenta no tiene productos.")
        input("Enter para continuar...")
        return

    print("\nProductos de la cuenta:")
    for p in productos:
        saldo = p.get("Saldo", 0)
        print(f"  ID: {p['idProducto']} - {p['tipo']} - Saldo: {saldo} - Estado: {p.get('Estado','N/A')}")

    try:
        idp = int(input("\nID del producto a depositar: ").strip())
        monto = float(input("Monto a depositar: ").strip())
    except ValueError:
        print("Valores inválidos.")
        input("Enter para continuar...")
        return

    for p in productos:
        if p["idProducto"] == idp:
            p["Saldo"] = float(p.get("Saldo", 0)) + monto
            p.setdefault("Historial", []).append({
                "FechaMovimiento": time.strftime("%Y-%m-%d %H:%M:%S"),
                "Valor": monto,
                "TipoMovimiento": "Depósito"
            })
            guardar_datos(cuentas)
            print(f" Depósito realizado. Nuevo saldo: {p['Saldo']}")
            input("Enter para continuar...")
            return

    print("Producto no encontrado.")
    input("Enter para continuar...")

def retirar_dinero(cuentas):
    limpiar_consola()
    print("=== RETIRAR DINERO ===")
    try:
        numero = int(input("Número de cuenta: ").strip())
    except ValueError:
        print("Número inválido.")
        input("Enter para continuar...")
        return
    cuenta = _get_cuenta(cuentas, numero)
    if not cuenta:
        print("Cuenta no encontrada.")
        input("Enter para continuar...")
        return

    productos = cuenta.get("productos", [])
    if not productos:
        print("La cuenta no tiene productos.")
        input("Enter para continuar...")
        return

    print("\nProductos de la cuenta:")
    for p in productos:
        print(f"  ID: {p['idProducto']} - {p['tipo']} - Saldo: {p.get('Saldo',0)}")

    try:
        idp = int(input("\nID del producto a retirar: ").strip())
        monto = float(input("Monto a retirar: ").strip())
    except ValueError:
        print("Valores inválidos.")
        input("Enter para continuar...")
        return

    for p in productos:
        if p["idProducto"] == idp:
            if p.get("Saldo", 0) >= monto:
                p["Saldo"] = float(p.get("Saldo",0)) - monto
                p.setdefault("Historial", []).append({
                    "FechaMovimiento": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "Valor": -monto,
                    "TipoMovimiento": "Retiro"
                })
                guardar_datos(cuentas)
                print(f" Retiro realizado. Nuevo saldo: {p['Saldo']}")
            else:
                print(" Saldo insuficiente.")
            input("Enter para continuar...")
            return

    print("Producto no encontrado.")
    input("Enter para continuar...")

def solicitar_credito(cuentas):
    limpiar_consola()
    print("=== SOLICITAR CRÉDITO ===")
    try:
        numero = int(input("Número de cuenta: ").strip())
    except ValueError:
        print("Número inválido.")
        input("Enter para continuar...")
        return
    cuenta = _get_cuenta(cuentas, numero)
    if not cuenta:
        print("Cuenta no encontrada.")
        input("Enter para continuar...")
        return

    try:
        monto = float(input("Monto solicitado: ").strip())
        plazo = int(input("Plazo (meses): ").strip())
        tasa = float(input("Tasa anual (%) [ej. 5.0]: ").strip())
    except ValueError:
        print("Valores inválidos.")
        input("Enter para continuar...")
        return

    id_credito = _siguiente_id_credito(cuenta)
    credito = {
        "idProducto": id_credito,
        "monto": monto,
        "plazo": plazo,
        "tasa": tasa,
        "saldoPendiente": monto,
        "estado": "Activo",
        "Historial": [
            {"FechaMovimiento": time.strftime("%Y-%m-%d %H:%M:%S"), "Valor": monto, "TipoMovimiento": "Crédito Aprobado"}
        ]
    }
    cuenta.setdefault("creditos", []).append(credito)
    guardar_datos(cuentas)
    print(f"\n Crédito aprobado. ID del crédito: {id_credito}")
    print(f"Saldo pendiente: {monto}")
    input("Enter para continuar...")

def pagar_credito(cuentas):
    limpiar_consola()
    print("=== PAGAR CRÉDITO ===")
    try:
        numero = int(input("Número de cuenta: ").strip())
    except ValueError:
        print("Número inválido.")
        input("Enter para continuar...")
        return

    cuenta = _get_cuenta(cuentas, numero)
    if not cuenta:
        print("Cuenta no encontrada.")
        input("Enter para continuar...")
        return

    creditos = cuenta.get("creditos", [])
    if not creditos:
        print("La cuenta no tiene créditos.")
        input("Enter para continuar...")
        return

    print("\nCréditos de la cuenta:")
    for c in creditos:
        print(f"  ID: {c['idProducto']} - Saldo pendiente: {c['saldoPendiente']} - Estado: {c['estado']}")

    try:
        idc = int(input("\nID del crédito a pagar: ").strip())
        monto = float(input("Monto a pagar: ").strip())
    except ValueError:
        print("Valores inválidos.")
        input("Enter para continuar...")
        return

    for c in creditos:
        if c["idProducto"] == idc:
            if monto <= 0:
                print("El monto debe ser mayor a 0.")
                input("Enter para continuar...")
                return
            c["saldoPendiente"] = max(0.0, float(c["saldoPendiente"]) - monto)
            c.setdefault("Historial", []).append({
                "FechaMovimiento": time.strftime("%Y-%m-%d %H:%M:%S"),
                "Valor": -monto,
                "TipoMovimiento": "Pago Crédito"
            })
            if c["saldoPendiente"] == 0:
                c["estado"] = "Cerrado"
            guardar_datos(cuentas)
            print(f"✅ Pago realizado. Saldo restante del crédito: {c['saldoPendiente']}")
            if c["estado"] == "Cerrado":
                print("El crédito ha sido cerrado.")
            input("Enter para continuar...")
            return

    print("Crédito no encontrado.")
    input("Enter para continuar...")

def eliminar_cuenta(cuentas):
    limpiar_consola()
    print("=== ELIMINAR CUENTA ===")
    try:
        numero = int(input("Número de cuenta a eliminar: ").strip())
    except ValueError:
        print("Número inválido.")
        input("Enter para continuar...")
        return

    cuenta = _get_cuenta(cuentas, numero)
    if not cuenta:
        print("Cuenta no encontrada.")
        input("Enter para continuar...")
        return

    confirma = input(f"Confirma eliminar la cuenta {numero}? (s/n): ").strip().lower()
    if confirma != "s":
        print("Operación cancelada.")
        input("Enter para continuar...")
        return

    cuentas.remove(cuenta)
    guardar_datos(cuentas)
    print(" Cuenta eliminada correctamente.")
    input("Enter para continuar...")

def mostrar_cuentas(cuentas):
    limpiar_consola()
    print("=== LISTA DE CUENTAS ===")
    if not cuentas:
        print("No hay cuentas registradas.")
        return
    for c in cuentas:
        print(f"\nCuenta: {c.get('numeroCuenta')} - Titular: {c.get('titular')}")
        print("  Contacto:", c.get("Contacto", {}))
        print("  Ubicación:", c.get("Ubicacion", {}))
        print("  Productos:")
        for p in c.get("productos", []):
            print(f"    ID: {p['idProducto']} - {p['tipo']} - Saldo: {p.get('Saldo',0)} - Estado: {p.get('Estado','')}")
        print("  Créditos:")
        for cr in c.get("creditos", []):
            print(f"    ID: {cr['idProducto']} - Pendiente: {cr['saldoPendiente']} - Estado: {cr['estado']}")
