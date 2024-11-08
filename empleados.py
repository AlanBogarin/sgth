from modelos import Empleado

empleados: list[Empleado] = []
"""Lista de todos los empleados"""

def buscar_empleado() -> Empleado | None:
    """Busca un empleado en la lista de empleados

    Si encuentra una conincidencia, retorna la instancia,
    sino, devuelve None
    """

def gestion_empleados() -> None:
    """Opciones del menu

    - Consultar empleados
    - Agregar empleado
    - Editar datos del empleado
    - Borrar empleado
    - Regresar al menu principal
    """
