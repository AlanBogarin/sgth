"""
Inicio del programa, con empleados predeterminados
"""
from menu import menu
from empleados import cargar_predeterminado

if __name__ == "__main__":
    cargar_predeterminado()
    menu()
