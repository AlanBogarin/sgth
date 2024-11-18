from empleados import empleados_activos, buscar_empleado
from utilidades import (
    esperar_tecla,
    limpiar_pantalla,
    pedir_numero,
    pedir_fecha,
    pedir_numero_positivo,
    pedir_texto,
    pedir_texto_opcional
)

def consultar_alt_registros():
    """Muestra el registro basico sobre ausencias y llegadas tardias de todos los empleados"""
    limpiar_pantalla()
    for empleado in empleados_activos():
        ausencias = len(empleado.asistencia.ausencias)
        llegadas_tardias = len(empleado.asistencia.llegadas_tardias)
        print("ID:", empleado.id, "ausencias:", ausencias, "llegadas tardias:", llegadas_tardias, "nombre:", empleado.nombre, empleado.apellido)

def consultar_alt():
    """Muestra el registro detallado sobre ausencias y llegadas tardias de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    limpiar_pantalla()
    print("AUSENCIAS")
    for ausencia in empleado.asistencia.ausencias:
        ausencia.mostrar()
    print("LLEGADAS TARDIAS")
    for llegada_tardia in empleado.asistencia.llegadas_tardias:
        llegada_tardia.mostrar()

def consultar_vphe_registros():
    """Muestra el registro basico sobre vacaciones, permisos y horas extras de todos los empleados"""
    limpiar_pantalla()
    for empleado in empleados_activos():
        vacaciones = len(empleado.asistencia.vacaciones)
        permisos = len(empleado.asistencia.permisos)
        trabajos_extra = len(empleado.asistencia.trabajos_extra)
        print("ID:", empleado.id, "vacaciones:", vacaciones, "permisos:", permisos, "trabajo extras:", trabajos_extra, "nombre:", empleado.nombre, empleado.apellido)

def consultar_vphe():
    """Muestra el registro detallado sobre vacaciones, permisos y horas extras de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    limpiar_pantalla()
    print("VACACIONES")
    for vacacion in empleado.asistencia.vacaciones:
        vacacion.mostrar()
    print("PERMISOS")
    for permiso in empleado.asistencia.permisos:
        permiso.mostrar()
    print("TRABAJOS EXTRA")
    for trabajo_extra in empleado.asistencia.trabajos_extra:
        trabajo_extra.mostrar()

def consultar_il_registros():
    """Muestra el registro basico sobre incapacidades y licensias de todos los empleados"""
    for empleado in empleados_activos():
        incapacidades = len(empleado.asistencia.incapacidades)
        licensias = len(empleado.asistencia.licensias)
        print("ID:", empleado.id, "incapacidades:", incapacidades, "licensias:", licensias, "nombre:", empleado.nombre, empleado.apellido)

def consultar_il():
    """Muestra el registro detallado sobre incapacidades y licensias de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    limpiar_pantalla()
    print("INCAPACIDADES")
    for incapacidad in empleado.asistencia.incapacidades:
        incapacidad.mostrar()
    print("LICENSIAS")
    for licensia in empleado.asistencia.licensias:
        licensia.mostrar()

def registrar_ausencia():
    """Registra la ausencia de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    fecha = pedir_fecha("Ingrese la fecha (Dia-Mes-Año): ")
    justificacion = pedir_texto_opcional("Ingrese la justificacion (opcional): ")
    empleado.asistencia.registrar_ausencia(fecha, justificacion)
    print("Registrado exitosamente")

def registrar_llegada_tardia():
    """Registra la llegada tardia de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    fecha = pedir_fecha("Ingrese la fecha (Dia-Mes-Año): ")
    empleado.asistencia.registrar_llegada_tardia(fecha)
    print("Registrado exitosamente")

def registrar_vacacion():
    """Registra una vacacion de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    inicio = pedir_fecha("Ingrese la fecha de inicio (Dia-Mes-Año): ")
    fin = pedir_fecha("Ingrese la fecha de fin (Dia-Mes-Año): ", inicio)
    empleado.asistencia.registrar_vacacion(inicio, fin)
    print("Registrado exitosamente")

def registrar_permiso():
    """Registra un permiso de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    fecha = pedir_fecha("Ingrese la fecha (Dia-Mes-Año): ")
    motivo = pedir_texto("Ingrese el motivo (opcional): ")
    empleado.asistencia.registar_permiso(fecha, motivo)
    print("Registrado exitosamente")

def registrar_horas_extra():
    """Registra las horas extras de trabajo de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    fecha = pedir_fecha("Ingrese la fecha de trabajo (Dia-Mes-Año): ")
    horas = int(pedir_numero_positivo("Ingrese las horas trabajadas: "))
    empleado.asistencia.registrar_trabajo_extra(fecha, horas)
    print("Registrado exitosamente")

def registrar_incapacidad():
    """Registra una incapacidad de un empleado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    inicio = pedir_fecha("Ingrese el inicio (Dia-Mes-Año): ")
    fin = pedir_fecha("Ingrese el fin (Dia-Mes-Año): ", inicio)
    motivo = pedir_texto("Ingrese el motivo: ")
    empleado.asistencia.registrar_incapacidad(inicio, fin, motivo)
    print("Registrado exitosamente")

def registrar_licensia():
    """Registra una licensia de un emplado"""
    limpiar_pantalla()
    empleado = buscar_empleado()
    if not empleado:
        return
    inicio = pedir_fecha("Ingrese el inicio (Dia-Mes-Año): ")
    fin = pedir_fecha("Ingrese el fin (Dia-Mes-Año): ", inicio)
    motivo = pedir_texto("Ingrese el motivo: ")
    empleado.asistencia.registrar_licensia(inicio, fin, motivo)
    print("Registrado exitosamente")

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
        # 16 + 1 + 16 + 1 + 16
        print("=" * 16, "MENU ASISTENCIAS", "=" * 16)
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
