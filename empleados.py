"""
Modulo para la gestion de empleados

Constantes:
- empleados

Funciones:
- empleados_activos
- buscar_empleado
- cargar_predeterminado
- registrar_empleado
- consultar_empleados
- consultar_empleado
- modificar_empleado
- borrar_empleado
- gestion_empleados
"""

from random import randint
from datetime import date
from modelos import Empleado, Puesto
from utilidades import (
    FMT_FECHA,
    esperar_tecla,
    limpiar_pantalla,
    pedir_fecha,
    pedir_fecha_opcional,
    pedir_numero,
    pedir_numero_positivo_opcional,
    pedir_texto,
    pedir_texto_opcional
)

empleados: list[Empleado] = []
"""Lista de todos los empleados"""

def empleados_activos() -> list[Empleado]:
    """Filtra los empleados activos"""
    return [empleado for empleado in empleados if not empleado.inactivo]

def buscar_empleado(info: str | None = None) -> Empleado | None:
    """Busca un empleado en la lista de empleados

    Si encuentra una conincidencia, retorna la instancia,
    sino, devuelve None
    """
    if not info:
        info = "Ingrese número de legajo: "
    if not empleados:
        print("No hay empleados registrados")
        return None
    id = int(pedir_numero(info))
    for empleado in empleados:
        if empleado.id == id and not empleado.inactivo:
            return empleado
    print("Empleado no encontrado")
    return None

def cargar_predeterminado() -> None:
    """Carga unos empleados ficticios de forma predeterminada"""
    for empleado in [
        Empleado(11111111, "Alejandro", "Arguello", date(1980, 1, 1), "Km 1", "Santa Maria", "Concepcion", Puesto("Limpiador", 2000000, date(2000, 1, 1))),
        Empleado(22222222, "Benjamin", "Benitez", date(1970, 1, 1), "Km 2", "San Antonio", "Concepcion", Puesto("Gerente", 5000000, date(1990, 1, 1))),
        Empleado(33333333, "Cesar", "Colman", date(1960, 1, 1), "Km 3", "Itacurubi", "Concepcion", Puesto("Tecnico", 6000000, date(2000, 1, 1))),
        Empleado(44444444, "Dario", "Duarte", date(1975, 1, 1), "Km 4", "Redencion", "Concepcion", Puesto("CEO", 7000000, date(1990, 1, 1))),
    ]:
        for a in range(2000, 2030):
            empleado.asistencia.registrar_llegada_tardia(date(a, 9, randint(1, 30)))
            empleado.asistencia.registrar_incapacidad(date(a, 10, 1), date(a, 10, 5), "Enfermedad contagiosa")
            empleado.asistencia.registrar_ausencia(date(a, randint(5, 7), randint(5, 7)), None)
            empleado.asistencia.registrar_vacacion(date(a, 12, 1), date(a, 12, 30))
            empleado.asistencia.registar_permiso(date(a, randint(6, 8), randint(2, 20)), "Reparar vehiculo")
            empleado.asistencia.registrar_trabajo_extra(date(a, randint(1, 4), randint(1, 20)), randint(1, 5))
            empleado.asistencia.registrar_feriado_trabajado(date(a, 1, 1))
        empleados.append(empleado)

def registrar_empleado() -> None:
    """Registra un nuevo empleado a partir de los datos ingresados"""
    limpiar_pantalla()
    ci = int(pedir_numero("Ingrese el CI: "))
    nombre = pedir_texto("Ingrese nombre: ")
    apellido = pedir_texto("Ingrese apellido: ")
    nacimiento = pedir_fecha("Ingrese fecha de nacimiento: ")
    direccion = pedir_texto("Ingrese direccion: ")
    barrio = pedir_texto("Ingrese barrio: ")
    ciudad = pedir_texto("Ingrese la ciudad: ")
    puesto_nombre = pedir_texto("Ingrese puesto de trabajo: ")
    salario = int(pedir_numero("Ingrese el salario: "))
    inicio = pedir_fecha("Ingrese fecha de inicio (Dia-Mes-Año): ")
    puesto = Puesto(puesto_nombre, salario, inicio)
    empleado = Empleado(ci, nombre, apellido, nacimiento, direccion, barrio, ciudad, puesto)
    empleados.append(empleado)
    print("Empleado registrado con èxito.")

def consultar_empleados() -> None:
    """Muestra una informacion basica de una linea para cada empleado activo"""
    limpiar_pantalla()
    for empleado in empleados_activos():
        empleado.mostrar()

def consultar_empleado() -> None:
    """Muestra una informacion detallada de un empleado activo"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    print("Nombre:", empleado.nombre)
    print("Apellido:", empleado.apellido)
    print("Fecha de Nacimiento:", empleado.nacimiento.strftime(FMT_FECHA))
    print("Direccion:", empleado.direccion)
    print("Barrio:", empleado.barrio)
    print("Ciudad:", empleado.ciudad)
    if empleado.trabajos_anteriores:
        trabajos_anteriores = empleado.trabajos_anteriores[0].nombre
        for trabajo_anterior in empleado.trabajos_anteriores[1:]:
            trabajos_anteriores += ", " + trabajo_anterior.nombre
        print("Trabajos Anteriores:", trabajos_anteriores)
    print("Puesto:", empleado.puesto.nombre)
    print("Salario:", empleado.puesto.salario_actual())

def modificar_empleado() -> None:
    """Modifica los valores ingresados de un empleado activo"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    empleado.modificar(
        nombre=pedir_texto_opcional("Ingrese nuevo nombre: "),
        apellido=pedir_texto_opcional("Ingrese nuevo apellido: "),
        nacimiento=pedir_fecha_opcional("Ingrese nueva fecha de nacimientos (Dia-Mes-Año): "),
        direccion=pedir_texto_opcional("Ingrese nueva direccion: "),
        barrio=pedir_texto_opcional("Ingrese nuevo barrio: "),
        ciudad=pedir_texto_opcional("Ingrese nueva ciudad: "),
    )
    puesto = pedir_texto_opcional("Ingrese nuevo puesto: ")
    salario = pedir_numero_positivo_opcional("Ingrese nuevo salario: ")
    if salario is not None:
        salario = int(salario)
    if not puesto:
        inicio = pedir_fecha_opcional("Ingrese fecha de modificacion (Dia-Mes-Año): ")
    else:
        inicio = pedir_fecha("Ingrese fecha de inicio (Dia-Mes-Año): ")
    empleado.modificar_puesto(puesto, salario, inicio)
    print("Datos del empleado modificado con exito")

def borrar_empleado() -> None:
    """Da de baja a un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if empleado:
        empleado.inactivo = True
        print("Empleado borrado con èxito.")

def gestion_empleados() -> None:
    """Opciones del menu

    - Consultar empleados
    - Consultar un empleado
    - Agregar empleado
    - Editar datos del empleado
    - Borrar empleado
    - Regresar al menu principal
    """
    while True:
        limpiar_pantalla()
        # 17 + 1 + 14 + 1 + 15 = 50
        print("=" * 17, "MENU EMPLEADOS", "=" * 17)
        print("1. Consultar empleados")
        print("2. Consultar empleado")
        print("3. Registrar empleado")
        print("4. Modificar empleado")
        print("5. Borrar empleado")
        print("0. Regresar")
        print("=" * 50)
        match pedir_numero("Seleccione una opción: "):
            case 1: consultar_empleados()
            case 2: consultar_empleado()
            case 3: registrar_empleado()
            case 4: modificar_empleado()
            case 5: borrar_empleado()
            case 0: break
            case _: print("Opcion Invalida")
        esperar_tecla()
