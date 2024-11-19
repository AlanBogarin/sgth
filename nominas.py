from empleados import buscar_empleado, empleados_activos
from modelos import RegistroMensual, RegistroSalarial
from utilidades import FMT_FECHA_MES, limpiar_pantalla, pedir_fecha, pedir_numero, esperar_tecla

registros: list[RegistroMensual] = []

def buscar_registro() -> RegistroMensual | None:
    if not registros:
        print("No hay registros")
        return None
    fecha = pedir_fecha("Ingrese la fecha a consultar (Mes-Año): ", fmt=FMT_FECHA_MES)
    for registro in registros:
        if registro.fecha == fecha:
            return registro
    print("No se encontró un registro para esa fecha.")
    return None

def consultar_registros() -> None:
    limpiar_pantalla()
    if not registros:
        print("No hay registros")
        return
    for registro in registros:
        registro.mostrar()

def consultar_registro() -> None:
    """Busca un registro mensual a partir de la fecha ingresada, si
    encuentra, muestra el salario, sino, informa que no existe un
    registro para esa fecha
    """
    limpiar_pantalla()
    registro = buscar_registro()
    if not registro:
        return
    print("Registro para", registro.fecha.strftime(FMT_FECHA_MES))
    for rsalarial in registro.registros:
        rsalarial.mostrar()
    print("Total a pagar:", registro.pago_empleados())

def consultar_empleado() -> None:
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
        print("No hay registros para este empleado en la fecha ingresada")
        return
    limpiar_pantalla()
    print("Registro para", empleado.nombre, empleado.apellido, "del", registro.fecha.strftime(FMT_FECHA_MES))
    print("AUSENCIAS")
    print("Cantidad:", len(rsalarial.ausencias))
    print("Descuento:", rsalarial.descuento_ausencia())
    print("LLEGADAS TARDIAS")
    print("Cantidad:", len(rsalarial.llegadas_tardias))
    print("Descuento:", rsalarial.descuento_llegada_tardia())
    print("TRABAJOS EXTRAS")
    print("Cantidad:", len(rsalarial.trabajos_extra))
    print("Bono:", rsalarial.bono_trabajo_extra())
    print("FERIADO TRABAJADOS")
    print("Cantidad:", len(rsalarial.feriados_trabajados))
    print("Bono:", rsalarial.bono_feriado_trabajado())

def crear_registros() -> None:
    """A partir de la fecha ingresada, calcula los datos para el
    registro salarial de todos los empleados activos
    """
    limpiar_pantalla()
    empleados = empleados_activos()
    if not empleados:
        print("No hay empleados")
        return None
    fecha = pedir_fecha("Ingrese la fecha a registrar (Mes-Año): ", fmt=FMT_FECHA_MES)
    registro = None
    for reg in registros:
        if reg.fecha == fecha:
            registro = reg
    if not registro:
        registro = RegistroMensual(fecha)
        registros.append(registro)
    for empleado in empleados:
        registro.agregar_registro(RegistroSalarial(fecha, empleado))
    print(len(empleados), "registros creados")

def crear_registro() -> None:
    """A partir de una fecha ingresada, busca o crea si no existe un
    registro mensual, en el cual, al ingresar un empleado, se calcula
    automaticamente los datos para el registro salarial
    """
    limpiar_pantalla()
    fecha = pedir_fecha("Ingrese la fecha a registrar (Mes-Año): ", fmt=FMT_FECHA_MES)
    empleado = buscar_empleado()
    if not empleado:
        return
    rsalarial = RegistroSalarial(fecha, empleado)
    registro = None
    for reg in registros:
        if reg.fecha == fecha:
            registro = reg
    if not registro:
        registro = RegistroMensual(fecha)
        registros.append(registro)
        print("Nuevo registro creado")
    else:
        print("Registro actualizado")
    registro.agregar_registro(rsalarial)

def calculo_nomina() -> None:
    """Descripcion del PDF

    - Cálculo automático de salarios basados en horas trabajadas, salarios fijos, comisiones y bonos.
    - Cálculo de horas extras, y dias festivos.
    """
    while True:
        limpiar_pantalla()
        # 18 +  1 + 12 + 1 + 18
        print("=" * 18, "MENU NOMINA", "=" * 18)
        print("1. Consultar registros")
        print("2. Consultar un registro")
        print("3. Consultar empleado")
        print("4. Crear registros")
        print("5. Crear un registro")
        print("0. Regresar")
        match pedir_numero("Ingrese una opcion: "):
            case 1: consultar_registros()
            case 2: consultar_registro()
            case 3: consultar_empleado()
            case 4: crear_registros()
            case 5: crear_registro()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()
