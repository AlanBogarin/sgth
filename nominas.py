from datetime import date
from utilidades import limpiar_pantalla,pedir_numero, esperar_tecla


class RegistroSalarial:
    def __init__(self, id_empleado: int, salario_base: float, horas_trabajadas: float,
                     comisiones: float = 0.0, bonos: float = 0.0) -> None:
        self.id_empleado = id_empleado
        """ID del empleado"""
        self.salario_base = salario_base
        """Salario base del empleado"""
        self.horas_trabajadas = horas_trabajadas
        """Horas trabajadas en el mes"""
        self.comisiones = comisiones
        """Comisiones obtenidas"""
        self.bonos = bonos
        """Bonos otorgados"""

    def calcular_salario(self) -> float:
        """Calcula el salario total del empleado incluyendo horas extras y deducciones."""
        salario_hora = self.salario_base / 240  # Suponiendo  240 horas al mes
        horas_extras = max(0, self.horas_trabajadas - 240)
        salario_extra = horas_extras * salario_hora * 1.5  # Pago de horas extras al 150%

        '''Calcular el salario total antes de deducciones'''
        total_salario = (self.salario_base + self.comisiones + self.bonos + salario_extra)

        '''Aplicar descuento del 9.5% por IPS'''
        descuento_ips = total_salario * 0.095
        salario_neto = total_salario - descuento_ips

        return salario_neto
class RegistroMensual:
    def __init__(self, fecha: date, registros: list[tuple[int, RegistroSalarial]] | None = None) -> None:
        self.fecha = fecha
        """Fecha del registro (mes, año)"""
        self.registros = registros or []
        """Registros de empleados (id, registro)"""

registros: list[RegistroMensual] = []
def consultar_registro() -> None:
    mes_a_consultar = pedir_numero("Ingrese el mes y año a consultar (MM-YYYY): ")
    try:
        mes, anio = map(int, mes_a_consultar.split('-'))
        fecha_consulta = date(anio, mes, 1)
        for registro in registros:
            if registro.fecha == fecha_consulta:
                print(f"Registro para {registro.fecha}:")
                for id_emp, reg in registro.registros:
                    print(f"ID Empleado: {id_emp}, Salario Total: {reg.calcular_salario()}")
                return
        print("No se encontró un registro para esa fecha.")
    except ValueError:
        print("Formato de fecha incorrecto. Use MM-YYYY.")

def crear_registro() -> None:
    mes_a_registrar = pedir_numero("Ingrese el mes y año a registrar (MM-YYYY): ")
    try:
        mes, anio = map(int, mes_a_registrar.split('-'))
        fecha_registro = date(anio, mes, 1)

        id_empleado = pedir_numero("Ingrese ID del empleado: ")
        salario_base = pedir_numero("Ingrese el salario base: ")
        horas_trabajadas = pedir_numero("Ingrese las horas trabajadas en el mes: ")

        comisiones = pedir_numero("Ingrese las comisiones (si no hay ingrese 0): ")
        bonos = pedir_numero("Ingrese los bonos (si no hay ingrese 0): ")

        nuevo_registro_salarial = RegistroSalarial(id_empleado, salario_base,
                                                   horas_trabajadas,
                                                   comisiones, bonos)

        # Verifica si ya existe un registro para ese mes
        for registro in registros:
            if registro.fecha == fecha_registro:
                registro.registros.append((id_empleado, nuevo_registro_salarial))
                print("Registro actualizado.")
                return

        # Si no existe un registro para ese mes
        registros.append(RegistroMensual(fecha_registro, [(id_empleado, nuevo_registro_salarial)]))
        print("Nuevo registro creado.")

    except ValueError:
        print("Formato de fecha incorrecto o datos inválidos.")


def calculo_nomina() -> None:
    """Descripcion del PDF

    - Cálculo automático de salarios basados en horas trabajadas, salarios fijos, comisiones y bonos.
    - Cálculo de horas extras, y dias festivos.
    """
    while True:
        limpiar_pantalla()
        # 14 +  1 + 20 + 1 + 14
        print("=" * 15, "Generacion de Nomina", "=" * 15)
        print("1.Consultar Registro")
        print("2.Crear Registro")
        print("0. Regresar")
        match pedir_numero("Ingrese una opcion: "):
            case 1: consultar_registro()
            case 2: crear_registro()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()


