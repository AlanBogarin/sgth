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
        if empleado.id == id:
            return empleado
    print("Empleado no encontrado")
    return None

def registrar_empleado():
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

def consultar_empleado():
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
            trabajos_anteriores += "," + trabajo_anterior.nombre
        print("Trabajos Anteriores:", trabajos_anteriores)
    print("Puesto:", empleado.puesto.nombre)
    print("Salario:", empleado.puesto.salario_actual())

def modificar_empleado():
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
    if puesto:
        inicio = pedir_fecha("Ingrese fecha de inicio (Dia-Mes-Año): ")
    else:
        inicio = pedir_fecha_opcional("Ingrese fecha de modificacion (Dia-Mes-Año): ")
    empleado.modificar_puesto(puesto, salario, inicio)
    print("Datos del empleado modificado con exito")

def borrar_empleado():
    empleado = buscar_empleado()
    if empleado:
        empleados.remove(empleado)
        print("Empleado borrado con èxito.")

def gestion_empleados():
    """Opciones del menu

    - Consultar empleados
    - Agregar empleado
    - Editar datos del empleado
    - Borrar empleado
    - Regresar al menu principal
    """
    while True:
        limpiar_pantalla()
        # 17 + 1 + 14 + 1 + 15 = 50
        print("=" * 17, "MENU EMPLEADOS", "=" * 17)
        print("1. Consultar Empleado")
        print("2. Registrar Empleado")
        print("3. Modificar Empleado")
        print("4. Borrar Empleado")
        print("0. Salir")
        print("=" * 50)
        match pedir_numero("Seleccione una opción: "):
            case 1: consultar_empleado()
            case 2: registrar_empleado()
            case 3: modificar_empleado()
            case 4: borrar_empleado()
            case 0: break
            case _: print("Opcion Invalida")
        esperar_tecla()
