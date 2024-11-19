"""
Modulo para la generacion de comprobantes de los empleados

Funciones:
- mostrar_comprobante
- generar_comprobantes
- generar_comprobante
- generacion_comprobantes
"""
from empleados import buscar_empleado
from modelos import RegistroSalarial
from nominas import buscar_registro
from utilidades import FMT_FECHA_MES, esperar_tecla, limpiar_pantalla, pedir_numero

def mostrar_comprobante(rsalarial: RegistroSalarial) -> None:
    """Muestra una informacion detallada sobre el registro salarial generado"""
    print("INFORME PARA", rsalarial.empleado.nombre, rsalarial.empleado.apellido, "del", rsalarial.fecha.strftime(FMT_FECHA_MES))
    print("ID:", rsalarial.empleado.id)
    print("Salario bruto:", rsalarial.salario)
    print()
    print("DESCUENTOS")
    print("Ausencias:", len(rsalarial.ausencias))
    print("Descuento:", rsalarial.descuento_ausencia())
    print("Llegadas tardias:", len(rsalarial.llegadas_tardias))
    print("Descuento:", rsalarial.descuento_llegada_tardia())
    print("Total:", rsalarial.calcular_descuentos())
    print()
    print("BONOS")
    print("Trabajos extras:", len(rsalarial.trabajos_extra))
    print("Bono:", rsalarial.bono_trabajo_extra())
    print("Feriados trabajados:", len(rsalarial.feriados_trabajados))
    print("Bono:", rsalarial.bono_feriado_trabajado())
    print("Total:", rsalarial.calcular_bonos())
    print()
    print("Salario:", rsalarial.calcular_salario_neto())
    print("IPS:", rsalarial.calcular_ips())
    print()
    print("Total a pagar:", rsalarial.calcular_salario())

def generar_comprobantes() -> None:
    """Genera un comprobante para cada empleado del registro"""
    limpiar_pantalla()
    registro = buscar_registro()
    if not registro:
        return
    limpiar_pantalla()
    # 18 + 1 + 12 + 1 + 18
    print("=" * 18, "COMPROBANTES", "=" * 18)
    for rsalarial in registro.registros:
        mostrar_comprobante(rsalarial)
        print("-" * 50)
    print("Total registros:", len(registro.registros))
    print("Total IPS:", registro.pago_ips())
    print("Total salario:", registro.pago_empleados())
    print("Total a pagar:", registro.pago_empleados() + registro.pago_ips())

def generar_comprobante() -> None:
    """Genera un comprobante para un empleado"""
    limpiar_pantalla()
    registro = buscar_registro()
    if not registro:
        return
    empleado = buscar_empleado()
    if not empleado:
        return
    rsalarial = None
    for reg in registro.registros:
        if reg.empleado.id == empleado.id:
            rsalarial = reg
    if not rsalarial:
        print("El registro no incluye a este empleado")
        return
    limpiar_pantalla()
    mostrar_comprobante(rsalarial)

def generacion_comprobantes() -> None:
    """Opciones del menu

    - Generar comprobantes para todos los empleados
    - Generar un comprobante para un empleado
    """
    while True:
        limpiar_pantalla()
        # 16 + 1 + 16 + 1 + 16
        print("=" * 16, "MENU COMPROBANTE", "=" * 16)
        print("1. Generar comprobantes")
        print("2. Generar un comprobante")
        print("0. Regresar")
        match pedir_numero("Ingrese una opcion: "):
            case 1: generar_comprobantes()
            case 2: generar_comprobante()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()
