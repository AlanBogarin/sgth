from modelos import Empleado
from utilidades import pedir_numero

empleados: list[Empleado] = []
"""Lista de todos los empleados"""

def buscar_empleado() -> Empleado | None:
    """Busca un empleado en la lista de empleados

    Si encuentra una conincidencia, retorna la instancia,
    sino, devuelve None
    """

def registrar_empleado():
    legajo=pedir_numero("Ingrese el numero de legajo:")
    nombre=input("Ingrese nombre:")
    apellido=input("Ingrese apellido:")
    nacimiento=input("Ingrese fecha de nacimiento:")
    direccion=input("Ingrese direccion:")
    barrio=input("Ingrese barrio:")
    ciudad=input("Ingrese la ciudad:")
    trabajo_anteriores=input("Ingrese trabajos anteriores:")
    puesto=input("Ingrese puesto de trabajo:")
    # anios_trabajos=pedir_numero("Ingrese años de trabajo:")

    empleado = Empleado(legajo, nombre, apellido, nacimiento, direccion, barrio, ciudad, trabajo_anteriores, puesto)
    empleados.append(empleado)
    print("Empleado registrado con èxito.")

def consultar_empleado():
    legajo=int(input("Ingrese su numero de legajo del empleado a consultar:"))
    for empleado in empleados:
        if legajo==legajo:
            print(f"Nombre: {empleado.nombre},\nApellido: {empleado.apellido},\n Fecha de Nacimiento: {empleado.nacimiento}")
            print(f"Direccion: {empleado.direccion},\n Barrio: {empleado.barrio},\n ciudad:{empleado.ciudad}")
            print(f"Trabajos Anteriores:\n {empleado.trabajos_anteriores}, \n puesto: {empleado.puesto}")
            # print(f"Trabajos Anteriores:\n{Empleado.trabajo_anteriores}")
            return
        print("Empleado no encontrado.")

def modificar_empleado():
    legajo=int(input("Ingrese numero de legajo del empleado a modificar:"))
    for empleado in empleados:
        if empleado.legajo==legajo:
            empleado.nombre=input("Ingrese nuevo nombre:")
            empleado.apellido=input("Ingrese nuevo apellido:")
            empleado.nacimiento=input("Ingrese nueva fecha de nacimientos.")
            empleado.direccion=input("Ingrese nueva direccion:")
            empleado.barrio=input("Ingrese nuevo barrio:")
            empleado.ciudad=input("Ingrese nueva ciudad:")
            empleado.trabajo_anteriores=input("Ingrese nuevos trabajos Anteriores:")
            empleado.puesto=input("Ingrese nuevo puesto:")
            print("Dato del empleado modificados con exitos.")
            return
        print("Empleado no encontrado.")

def borrar_empleado():
    legajo=int(input("Ingrese numero de legajo de empleado a borrar:"))
    for empleado in empleados:
        if empleado.legajo==legajo:
            empleado.remove(empleado)
            print("Empleado borrado con èxito.")
            return
    print("Empleado no encontrado.")



def gestion_empleados() -> None:
    """Opciones del menu

    - Consultar empleados
    - Agregar empleado
    - Editar datos del empleado
    - Borrar empleado
    - Regresar al menu principal
    """
    while True:
        print("===Menú Principal===")
        print("=====================")
        print("1. Registrar Empleado")
        print("2. Consultar Empleado")
        print("3. Modificar Empleado")
        print("4. Borrar Empleado")
        print("5. Salir")
        print("=====================")
        try:
            opcion = pedir_numero("Seleccione una opción: ")
            if opcion == 1:
                registrar_empleado()
            elif opcion == 2:
                consultar_empleado()
            elif opcion == 3:
                modificar_empleado()
            elif opcion == 4:
               borrar_empleado()
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


