from datetime import date
from utilidades import limpiar_pantalla,pedir_numero, esperar_tecla
from empleados import  buscar_empleado, empleados

class RegistroSalarial:
    ...

class RegistroMensual:
    fecha: date
    """Fecha del registro (mes, año)"""
    registros: list[tuple[int, RegistroSalarial]]
    """Registros de empleados (id, registro)"""

registros: list[RegistroMensual] = []

def total_cobrar():
    pass

def consultar_bonificaciones():
    pass

def consultar_descuentos():
    empleado = buscar_empleado()
    if not empleado:
        return

def calculo_nomina() -> None:
    """Descripcion del PDF

    - Cálculo automático de salarios basados en horas trabajadas, salarios fijos, comisiones y bonos.
    - Gestión de deducciones obligatorias y voluntarias (impuestos, seguridad social, préstamos, adelantos etc.).
    - Cálculo de horas extras, recargos nocturnos y festivos.
    """

    while True:
        limpiar_pantalla()
        print("="*15,"Calculo de Nomina","="*15)
        print("1.Total a cobrar ")
        print("2.Bonificaciones")
        print("3.Descuentos")
        print("0.Regresar al menu principal")
        match pedir_numero("Ingrese una opcion: "):
            case 1: total_cobrar()
            case 2: consultar_bonificaciones()
            case 3: consultar_descuentos()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()


