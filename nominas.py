from datetime import date
from utilidades import limpiar_pantalla,pedir_numero, esperar_tecla
from empleados import  buscar_empleado, empleados_activos

class RegistroSalarial:
    ...

class RegistroMensual:
    def __init__(self, fecha: date, registros: list[tuple[int, RegistroSalarial]] | None = None) -> None:
        self.fecha = fecha
        """Fecha del registro (mes, año)"""
        self.registros = registros or []
        """Registros de empleados (id, registro)"""

    def agregar_registro(self):
        pass

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
    - Cálculo de horas extras, y dias festivos.
    """
    while True:
        limpiar_pantalla()
        # 14 +  1 + 20 + 1 + 14
        print("=" * 15, "Generacion de Nomina", "=" * 15)
        print("2. Bonificaciones")
        # horas extras, dias festivos
        print("3. Descuentos")
        # 
        print("0. Regresar")
        match pedir_numero("Ingrese una opcion: "):
            case 1: total_cobrar()
            case 2: consultar_bonificaciones()
            case 3: consultar_descuentos()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()


