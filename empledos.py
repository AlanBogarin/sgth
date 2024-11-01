from datetime import date
from utilidades import (
    FMT_LINEA,
    FMT_SEP_LINEA,
    FMT_TITULO,
    SEPARADOR,
    esperar_tecla,
    limpiar_pantalla,
    mostrar_menu,
    pedir_fecha,
    pedir_numero,
    pedir_numero_positivo,
    pedir_texto
)

CONTRATO_FIJO = "fijo"
CONTRATO_TEMPORAL = "temporal"
CONTRATO_HORAS = "horas"
FMT_CONSULTA = FMT_LINEA.format("{:^6s} | {:^28s} | {:^18s} | {:^17s}")

empleados: list["Empleado"] = []

class PuestoLaboral:
    def __init__(
        self,
        nombre: str, 
        salario: int,
        contrato: str,
        inicio: date,
        fin: date | None
    ) -> None:
        self.nombre = nombre
        self.salario = salario
        self.contrato = contrato
        self.inicio = inicio
        self.fin = fin

class LlegadaTardia:
    def __init__(self, fecha: date, horas: int) -> None:
        self.fecha = fecha
        self.horas = horas

class Empleado:
    id_anterior = 0
    def __init__(
        self,
        nombre: str,
        apellido: str,
        nacimiento: date,
        direccion: str,
        barrio: str,
        ciudad: str,
        puesto: PuestoLaboral,
        puestos_anteriores: list[str] | None = None,
        ausencias: list[date] | None = None,
        llegadas_tardias: list[LlegadaTardia] | None = None
    ) -> None:
        Empleado.id_anterior += 1
        self.id = self.id_anterior
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.direccion = direccion
        self.barrio = barrio
        self.ciudad = ciudad
        self.puesto = puesto
        if not puestos_anteriores:
            puestos_anteriores = []
        if not ausencias:
            ausencias = []
        if not llegadas_tardias:
            llegadas_tardias = []
        self.puestos_anteriores = puestos_anteriores
        self.ausencias = ausencias
        self.llegadas_tardias = llegadas_tardias

    def agregar_ausencia(self, fecha: date) -> bool:
        if self.puesto.inicio > fecha:
            return False
        if self.puesto.fin and self.puesto.fin < fecha:
            return False
        self.ausencias.append(fecha)
        return True

    def agregar_llegada_tardia(self, fecha: date, horas: int) -> bool:
        if self.puesto.inicio > fecha:
            return False
        if self.puesto.fin and self.puesto.fin < fecha:
            return False
        self.llegadas_tardias.append(LlegadaTardia(fecha, horas))
        return True

    def dias_trabajando(self) -> int:
        fin = date.today()
        if self.puesto.fin and not self.trabajando():
            fin = self.puesto.fin
        return (fin - self.puesto.inicio).days

    def edad(self):
        return (date.today() - self.nacimiento).days // 365

    def trabajando(self) -> bool:
        if not self.puesto.fin:
            return True
        return self.puesto.fin <= date.today()

    def consulta(self) -> None:
        print(FMT_CONSULTA.format(f"{self.id}", f"{self.nombre} {self.apellido}", self.puesto.nombre, f"{self.puesto.salario}"))

def hay_empleados(silencioso: bool = False, esperar: bool = True):
    resultado = len(empleados) != 0
    if not resultado:
        if not silencioso:
            print(FMT_SEP_LINEA.format("No hay empleados"))
        if esperar:
            esperar_tecla()
    return resultado

def consultar_empleado():
    limpiar_pantalla()
    if not hay_empleados():
        return
    print(FMT_TITULO.format(FMT_CONSULTA.format("Legajo", "Nombre y Apellido", "Puesto", "Salario")))
    for empleado in empleados:
        empleado.consulta()

def crear_puesto() -> PuestoLaboral:
    fin = None
    nombre = pedir_texto(FMT_LINEA.format("Nombre del puesto: "))
    inicio = pedir_fecha(FMT_LINEA.format("Fecha de inicio (Dia/Mes/Año): "))
    while True:
        match pedir_texto(FMT_LINEA.format("Tipo de contrato (fijo, temporal, horas): ")).lower():
            case "fijo": contrato = CONTRATO_FIJO
            case "temporal":
                contrato = CONTRATO_TEMPORAL
                while True:
                    fin = pedir_fecha(FMT_LINEA.format("Fecha de finalizacion del contrato (Dia/Mes/Año): "))
                    if fin > inicio:
                        break
            case "horas": contrato = CONTRATO_HORAS
            case _: continue
        break
    salario = int(pedir_numero_positivo(FMT_LINEA.format("Salario: ")))
    return PuestoLaboral(nombre, salario, contrato, inicio, fin)

def agregar_empleado() -> None:
    limpiar_pantalla()
    print(SEPARADOR)
    nombre = pedir_texto(FMT_LINEA.format("Nombre: "))
    apellido = pedir_texto(FMT_LINEA.format("Apellido: "))
    nacimiento = pedir_fecha(FMT_LINEA.format("Fecha de nacimiento (Dia/Mes/Año): "))
    direccion = pedir_texto(FMT_LINEA.format("Direccion: "))
    barrio = pedir_texto(FMT_LINEA.format("Barrio: "))
    ciudad = pedir_texto(FMT_LINEA.format("Ciudad: "))
    puesto = crear_puesto()
    empleado = Empleado(nombre, apellido, nacimiento, direccion, barrio, ciudad, puesto)
    empleados.append(empleado)
    limpiar_pantalla()
    print(FMT_SEP_LINEA.format(f"Nuevo Empleado! Nro Legajo: {empleado.id}"))
    esperar_tecla()

def seleccionar_empleado() -> Empleado | None:
    empleado = None
    if not hay_empleados():
        return None
    consultar_empleado()
    print(SEPARADOR)
    while not empleado:
        id = int(pedir_numero(FMT_LINEA.format("Seleccione un legajo: ")))
        for posible_empleado in empleados:
            if posible_empleado.id == id:
                empleado = posible_empleado
                break
    return empleado

def editar_empleado() -> None:
    limpiar_pantalla()
    empleado = seleccionar_empleado()
    if not empleado:
        return
    while True:
        limpiar_pantalla()
        print(FMT_SEP_LINEA.format(f"Editando información de {empleado.nombre} {empleado.apellido}"))
        mostrar_menu([
            (1, f"Puesto ({empleado.puesto.nombre})"),
            (2, f"Salario ({empleado.puesto.salario})"),
            (0, f"Regresar")
        ])
        match pedir_numero(FMT_LINEA.format("Seleccione una opcion: ")):
            case 1:
                print(SEPARADOR)
                empleado.puestos_anteriores.append(empleado.puesto.nombre)
                empleado.puesto = crear_puesto()
            case 2:
                print(SEPARADOR)
                empleado.puesto.salario = int(pedir_numero_positivo(FMT_LINEA.format("Nuevo salario: ")))
            case 0: break
            case _: continue

def borrar_empleado():
    limpiar_pantalla()
    empleado = seleccionar_empleado()
    if not empleado:
        return
    empleados.remove(empleado)
    print(FMT_SEP_LINEA.format(f"{empleado.nombre} {empleado.apellido} ya no es un empleado!"))
    esperar_tecla()

def registro_ausencias():
    while True:
        limpiar_pantalla()
        mostrar_menu([
            (1, "Consultar registros"),
            (2, "Registrar dias ausentes"),
            (3, "Registrar llegadas tardías"),
            (0, "Regresar")
        ])
        match pedir_numero("| Seleccione una opcion: "):
            case 1:
                limpiar_pantalla()
                if not hay_empleados():
                    continue
                print(FMT_TITULO.format(FMT_CONSULTA.format("Legajo", "Nombre y Apellido", "Ausencias", "Llegadas tardias")))
                for empleado in empleados:
                    print(FMT_CONSULTA.format(f"{empleado.id}", f"{empleado.nombre} {empleado.apellido}", f"{len(empleado.ausencias)}", f"{len(empleado.llegadas_tardias)}"))
                esperar_tecla()
            case 2:
                limpiar_pantalla()
                empleado = seleccionar_empleado()
                if not empleado:
                    continue
                print(FMT_TITULO.format(FMT_LINEA.format(f"Empleado {empleado.nombre} {empleado.apellido} cargado!")))
                print(FMT_LINEA.format(f"Ausencias totales: {len(empleado.ausencias)}"))
                while True:
                    if empleado.agregar_ausencia(pedir_fecha(FMT_LINEA.format("Ingrese la fecha (Dia/Mes/Año): "))):
                        break
                esperar_tecla()
            case 3:
                empleado = seleccionar_empleado()
                if not empleado:
                    continue
                print(FMT_TITULO.format(FMT_LINEA.format(f"Empleado {empleado.nombre} {empleado.apellido} cargado!")))
                print(FMT_LINEA.format(f"LLegadas tardias totales: {len(empleado.llegadas_tardias)}"))
                horas = int(pedir_numero_positivo(FMT_LINEA.format("Cantidad de horas faltantes: ")))
                while True:
                    fecha = pedir_fecha(FMT_LINEA.format("Ingrese la fecha (Dia/Mes/Año): "))
                    if empleado.agregar_llegada_tardia(fecha, horas):
                        break
                esperar_tecla()
            case 0: break
            case _: continue

def registro_permisos():
    """Registro de vacaciones, permisos y horas extra"""

def registro_incapacidades():
    """Gestión de incapacidades y licencias"""

def cargar_ejemplos():
    empleados.extend([
        Empleado("Ruben", "Rodriguez", date(2000, 1, 1), "-", "-", "Concepcion", PuestoLaboral("Gerente", 5000000, "fijo", date(2020, 1, 1), None)),
        Empleado("Pedro", "Gonzalez", date(2000, 1, 1), "-", "-", "Concepcion", PuestoLaboral("Guardia", 2000000, "fijo", date(2020, 1, 1), None)),
        Empleado("Juan", "Torrado", date(2000, 1, 1), "-", "-", "Concepcion", PuestoLaboral("Tecnico", 6000000, "fijo", date(2020, 1, 1), None)),
        Empleado("Maria", "Peralta", date(2000, 1, 1), "-", "-", "Concepcion", PuestoLaboral("CEO", 8000000, "fijo", date(2020, 1, 1), None)),
        Empleado("Luis", "Benitez", date(2000, 1, 1), "-", "-", "Concepcion", PuestoLaboral("Limpieza", 1000000, "fijo", date(2020, 1, 1), None))
    ])