from empledos import (
    agregar_empleado,
    borrar_empleado,
    cargar_ejemplos,
    consultar_empleado,
    editar_empleado,
    hay_empleados,
    registro_ausencias,
    registro_permisos,
    registro_incapacidades
)
from utilidades import (
    SEPARADOR,
    FMT_LINEA,
    esperar_tecla,
    limpiar_pantalla,
    mostrar_menu,
    pedir_numero
)

def gestion_empleados():
    """
    • Registro y actualización de información personal y laboral de los 
    empleados. (nro Legajo, nombre, apellido, fecha nacimiento, dirección, 
    barrio, ciudad, trabajos anteriores, puestos, años de trabajo) 
    • Mantenimiento de historial laboral y salarial. (nro Legajo, fecha, puesto, 
    salario, tipo contrato) 
    • Mantenimiento de contratos y tipos de empleados (fijo, temporal, por horas, etc.). 
    """
    while True:
        limpiar_pantalla()
        mostrar_menu([
            (1, "Consultar empleados"),
            (2, "Agregar empleado"),
            (3, "Editar datos de empleado"),
            (4, "Borrar empleado"),
            (0, "Regresar")
        ])
        match pedir_numero(FMT_LINEA.format("Seleccione una opcion: ")):
            case 1:
                consultar_empleado()
                if hay_empleados(silencioso=True, esperar=False):
                    esperar_tecla()
            case 2: agregar_empleado()
            case 3: editar_empleado()
            case 4: borrar_empleado()
            case 0: break
            case _: continue

def gestion_asistencia():
    """
    • Registro de los días ausentes y llegadas tardías 
    • Registro de vacaciones, permisos. 
    • Gestión de incapacidades y licencias
    """
    while True:
        limpiar_pantalla()
        mostrar_menu([
            (1, "Registro de ausencias y llegadas tardias"),
            (2, "Registro de vacaciones, permisos y horas extra"),
            (3, "Gestión de incapacidades y licencias"),
            (0, "Regresar")
        ])
        match pedir_numero("| Seleccione una opcion: "):
            case 1: registro_ausencias()
            case 2: registro_permisos()
            case 3: registro_incapacidades()
            case 0: break
            case _: continue

def calculo_nomina():
    """
    • Cálculo automático de salarios basados en horas trabajadas, salarios fijos, 
    comisiones y bonos. 
    • Gestión de deducciones obligatorias y voluntarias (impuestos, seguridad 
    social, préstamos, adelantos etc.). 
    • Cálculo de horas extras, recargos nocturnos y festivos.
    """

def generacion_comprobantes():
    """
    • Emisión de recibos de pago detallados para los empleados. 
    • Generación de informes y reportes para Talento humano (Monto total del 
    sueldo a ser pagado, Monto total por IPS empleado/empresa, Detalle de 
    descuentos y pagos en un rango de meses para un empleado, etc.)
    """

def menu():
    while True:
        limpiar_pantalla()
        mostrar_menu([
            (1, "Gestión de empleados"),
            (2, "Gestión de asistencias"),
            (3, "Cálculo de Nómina"),
            (4, "Generación de comprobantes"),
            (0, "Salir")
        ])
        match pedir_numero(FMT_LINEA.format("Seleccione una opcion: ")):
            case 1: gestion_empleados()
            case 2: gestion_asistencia()
            case 3: calculo_nomina()
            case 4: generacion_comprobantes()
            case 0: break
            case _: continue
    print(SEPARADOR)

if __name__ == "__main__":
    cargar_ejemplos()
    menu()
