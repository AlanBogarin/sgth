from utilidades import esperar_tecla, limpiar_pantalla, pedir_numero

def ausencias_llegadas_tardias(): ...
def vacaciones_permisos(): ...
def incapacidades_licencias(): ...

def gestion_asistencia() -> None:
    """Opciones del menu

    - Registro de ausencias y llegadas tardias
    - Registro de vacaciones, permisos y horas extra
    - Gestión de incapacidades y licencias
    - Regresar al menu principal
    """
    while True:
        limpiar_pantalla()
        print("=" * 15, "GESTION ASISTENCIA", "=" * 15)
        print("1. Registro de ausencias y llegadas tardias")
        print("2. Registro de vacaciones, permisos y horas extra")
        print("3. Gestión de incapacidades y licencias")
        print("0. Regresar al menu principal")
        print("=" * 50)
        match pedir_numero("Ingrese una opcion: "):
            case 1: ausencias_llegadas_tardias()
            case 2: vacaciones_permisos()
            case 3: incapacidades_licencias()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()
