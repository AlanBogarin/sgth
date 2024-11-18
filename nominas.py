from empleados import buscar_empleado
from modelos import RegistroMensual, RegistroSalarial
from utilidades import FMT_FECHA_MES, limpiar_pantalla, pedir_fecha,pedir_numero, esperar_tecla

registros: list[RegistroMensual] = []

def consultar_registro():
    """Busca un registro mensual a partir de la fecha ingresada, si
    encuentra, muestra el salario, sino, informa que no existe un
    registro para esa fecha
    """
    fecha = pedir_fecha("Ingrese el mes y año a consultar (Mes-Año): ", fmt=FMT_FECHA_MES)
    for registro in registros:
        if registro.fecha == fecha:
            print(f"Registro para {registro.fecha.strftime(FMT_FECHA_MES)}:")
            for reg in registro.registros:
                print("ID Empleado:", reg.legajo, "Salario Total:", reg.calcular_salario())
            return
    print("No se encontró un registro para esa fecha.")

def crear_registro():
    """A partir de una fecha ingresada, busca o crea si no existe un
    registro mensual, en el cual, al ingresar un empleado, se calcula
    automaticamente los datos para el registro salarial
    """
    fecha = pedir_fecha("Ingrese el mes y año a registrar (Mes-Año): ", fmt=FMT_FECHA_MES)
    empleado = buscar_empleado()
    if not empleado:
        return
    rsalarial = RegistroSalarial(fecha, empleado)
    for registro in registros:
        if registro.fecha == fecha:
            registro.agregar_registro(rsalarial)
            print("Registro actualizado")
            return
    registros.append(RegistroMensual(fecha, [rsalarial]))
    print("Nuevo registro creado")

def calculo_nomina():
    """Descripcion del PDF

    - Cálculo automático de salarios basados en horas trabajadas, salarios fijos, comisiones y bonos.
    - Cálculo de horas extras, y dias festivos.
    """
    while True:
        limpiar_pantalla()
        # 14 +  1 + 20 + 1 + 14
        print("=" * 15, "Generacion de Nomina", "=" * 15)
        print("1. Consultar registros")
        print("2. Consultar empleado")
        print("3. Crear Registro")
        print("0. Regresar")
        match pedir_numero("Ingrese una opcion: "):
            case 1: consultar_registro()
            case 2: crear_registro()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()
