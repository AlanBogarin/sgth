from empleados import gestion_empleados
from asistencias import gestion_asistencia
from nominas import calculo_nomina
from comprobantes import generacion_comprobantes
from utilidades import esperar_tecla, limpiar_pantalla, pedir_numero

def menu() -> None:
    """Opciones del menu principal

    - Gestión de empleados
    - Gestión de asistencias
    - Cálculo de Nómina
    - Generación de comprobantes
    - Salir
    """
    while True:
        limpiar_pantalla()
        # 50 = 17 + 1 + 14 + 1 + 17
        print("=" * 17, "MENU PRINCIPAL", "=" * 17)
        print("1. Gestión de empleados")
        print("2. Gestión de asistencias")
        print("3. Cálculo de Nómina")
        print("4. Generación de comprobantes")
        print("0. Salir")
        print("=" * 50)
        match pedir_numero("Ingrese una opcion: "):
            case 1: gestion_empleados()
            case 2: gestion_asistencia()
            case 3: calculo_nomina()
            case 4: generacion_comprobantes()
            case 0: break
            case _: print("Opcion Invalida")
        esperar_tecla()
