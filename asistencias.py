from empleados import buscar_empleado
from utilidades import esperar_tecla, limpiar_pantalla, pedir_numero, pedir_fecha

def consultar_alt_registros():
    """Muestra el registro basico sobre ausencias y llegadas tardias de todos los empleados"""
def consultar_alt():
    """Muestra el registro detallado sobre ausencias y llegadas tardias de un empleado"""
def consultar_vphe_registros():
    """Muestra el registro basico sobre vacaciones, permisos y horas extras de todos los empleados"""
def consultar_vphe():
    """Muestra el registro detallado sobre vacaciones, permisos y horas extras de un empleado"""
def consultar_il_registros():
    """Muestra el registro basico sobre incapacidades y licensias de todos los empleados"""
def consultar_il():
    """Muestra el registro detallado sobre incapacidades y licensias de un empleado"""
def registrar_ausencia():
    """Registra la ausencia de un empleado"""
def registrar_llegada_tardia():
    """Registra la llegada tardia de un empleado"""
def registrar_vacacion():
    """Registra una vacacion de un empleado"""
def registrar_permiso():
    """Registra un permiso de un empleado"""
def registrar_horas_extra():
    """Registra las horas extras de trabajo de un empleado"""
def registrar_incapacidad():
    """Registra una incapacidad de un empleado"""
def registrar_licensia():
    """Registra una licensia de un emplado"""

def gestion_ausencias_llegadas_tardias():
    """Opciones del menu

    - Consultar registros
    - Consultar empleado
    - Registrar ausencia
    - Registrar llegada tardia
    - Regresar
    """
    while True:
        limpiar_pantalla()
        # 6 + 1 + 36 + 1 + 6
        print("=" * 6, "GESTION AUSENCIAS & LLEGADAS TARDIAS", "=" * 6)
        print("1. Consultar registros")
        print("2. Consultar empleado")
        print("3. Registrar ausencia")
        print("4. Registrar llegada tardia")
        print("0. Regresar")
        print("=" * 50)
        match pedir_numero("Ingrese una opcion: "):
            case 1: consultar_alt_registros()
            case 2: consultar_alt()
            case 3: registrar_ausencia()
            case 4: registrar_llegada_tardia()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()

def vacaciones_permisos():
    """Opciones del menu

    - Consultar registros
    - Consultar empleado
    - Registrar vacacion
    - Registrar permiso
    - Registrar horas extras
    - Regresar
    """
    while True:
        limpiar_pantalla()
        # 5 + 1 + 38 + 1 + 5
        print("=" * 5, "GESTION VACACION PERMISO & HORAS EXTRA", "=" * 5)
        print("1. Consultar registros")
        print("2. Consultar empleado")
        print("3. Registrar vacacion")
        print("4. Registrar permiso")
        print("5. Registrar horas extras")
        print("0. Regresar")
        print("=" * 50)
        match pedir_numero("Ingrese una opcion: "):
            case 1: consultar_vphe_registros()
            case 2: consultar_vphe()
            case 3: registrar_vacacion()
            case 4: registrar_permiso()
            case 5: registrar_horas_extra()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()

def incapacidades_licencias():
    """Opciones del menu

    - Consultar registros
    - Consultar empleado
    - Registrar incapacidad
    - Registrar licensia
    - Regresar
    """
    while True:
        limpiar_pantalla()
        # 9 + 1 + 30 + 1 + 9
        print("=" * 9, "GESTION INCAPACIDAD & LICENSIA", "=" * 9)
        print("1. Consultar registros")
        print("2. Consultar empleado")
        print("3. Registrar incapacidad")
        print("4. Registrar licensia")
        print("0. Regresar")
        print("=" * 50)
        match pedir_numero("Ingrese una opcion: "):
            case 1: consultar_il_registros()
            case 2: consultar_il()
            case 3: registrar_incapacidad()
            case 4: registrar_licensia()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()

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
            case 1: gestion_ausencias_llegadas_tardias()
            case 2: vacaciones_permisos()
            case 3: incapacidades_licencias()
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()
