from datetime import date
from utilidades import FMT_FECHA

DIAS_FERIADOS = [
    (1, 1),   # Año Nuevo
    (1, 3),   # Día de los Héroes
    (1, 5),   # Día del Trabajador
    (15, 5),  # Día de la Independencia Nacional
    (12, 6),  # Paz del Chaco
    (15, 8),  # Fundación de Asunción
    (29, 9),  # Batalla de Boquerón
    (8, 12),  # Virgen de Ca’acupé
    (25, 12), # Navidad
]

class Ausencia:
    def __init__(self, fecha: date, justificacion: str | None) -> None:
        self.fecha = fecha
        self.justificacion = justificacion

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(self.fecha.strftime(FMT_FECHA), "justificacion:", self.justificacion)

class LlegadaTardia:
    def __init__(self, fecha: date) -> None:
        self.fecha = fecha

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(self.fecha.strftime(FMT_FECHA))

class Vacacion:
    def __init__(self, inicio: date, fin: date) -> None:
        self.inicio = inicio
        self.fin = fin

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(self.inicio.strftime(FMT_FECHA), "al", self.fin.strftime(FMT_FECHA))

class Permiso:
    def __init__(self, fecha: date, motivo: str) -> None:
        self.fecha = fecha
        self.motivo = motivo

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(self.fecha.strftime(FMT_FECHA), "-", self.motivo)

class Incapacidad:
    def __init__(self, inicio: date, fin: date, motivo: str) -> None:
        self.inicio = inicio
        self.fin = fin
        self.motivo = motivo

    def mostrar(self) -> None:
        print(self.inicio.strftime(FMT_FECHA), "al", self.fin.strftime(FMT_FECHA), ":", self.motivo)

class Licensia:
    def __init__(self, inicio: date, fin: date, motivo: str) -> None:
        self.inicio = inicio
        self.fin = fin
        self.motivo = motivo

    def mostrar(self) -> None:
        print(self.inicio.strftime(FMT_FECHA), "al", self.fin.strftime(FMT_FECHA), ":", self.motivo)

class TrabajoExtra:
    def __init__(self, fecha: date, horas: int) -> None:
        self.fecha = fecha
        self.horas = horas

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(self.fecha.strftime(FMT_FECHA), "-", self.horas, "hs")

class FeriadoTrabajado:
    def __init__(self, fecha: date) -> None:
        self.fecha = fecha

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(self.fecha.strftime(FMT_FECHA))

class Asistencia:
    def __init__(self) -> None:
        # descuento
        self.ausencias: list[Ausencia] = []
        self.llegadas_tardias: list[LlegadaTardia] = []
        # neutral
        self.vacaciones: list[Vacacion] = [] 
        self.permisos: list[Permiso] = []
        self.incapacidades: list[Incapacidad] = []
        self.licensias: list[Licensia] = []
        # aumento
        self.trabajos_extra: list[TrabajoExtra] = []
        self.feriados_trabajados: list[FeriadoTrabajado] = []

    def registrar_ausencia(self, fecha: date, justificacion: str | None) -> None:
        """Registra una ausencia, justificada o no"""
        self.ausencias.append(Ausencia(fecha, justificacion))

    def registrar_llegada_tardia(self, fecha: date) -> None:
        """Registra una llegada tardia"""
        self.llegadas_tardias.append(LlegadaTardia(fecha))

    def registrar_vacacion(self, inicio: date, fin: date) -> None:
        """Registra una vacacion"""
        self.vacaciones.append(Vacacion(inicio, fin))

    def registar_permiso(self, fecha: date, motivo: str) -> None:
        """Registra un permiso"""
        self.permisos.append(Permiso(fecha, motivo))

    def registrar_incapacidad(self, inicio: date, fin: date, motivo: str) -> None:
        """Registra una ausencia por incapacidad fisica (accidentes, embarazo, etc)"""
        self.incapacidades.append(Incapacidad(inicio, fin, motivo))

    def registrar_licensia(self, inicio: date, fin: date, motivo: str) -> None:
        """Registra una ausencia por motivos externos (duelos, medico, etc)"""
        self.licensias.append(Licensia(inicio, fin, motivo))

    def registrar_trabajo_extra(self, fecha: date, horas: int) -> None:
        """Registra un trabajo extra diario"""
        self.trabajos_extra.append(TrabajoExtra(fecha, horas))

    def registrar_feriado_trabajado(self, fecha: date) -> None:
        if (fecha.day, fecha.month) in DIAS_FERIADOS:
            self.feriados_trabajados.append(FeriadoTrabajado(fecha))

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea (solo cantidades)"""
        print("ausencias:", len(self.ausencias), "llegadas tardias:", len(self.llegadas_tardias), "vacaciones:", len(self.vacaciones),
              "permisos:", len(self.permisos), "incapacidades:", len(self.incapacidades), "licensias:", len(self.licensias), "trabajos extras:", len(self.trabajos_extra))

class Puesto:
    def __init__(self, nombre: str, salario: int, inicio: date) -> None:
        self.nombre = nombre
        """Nombre del puesto"""
        self.inicio = inicio
        """Inicio del puesto"""
        self.historial_salarial: list[tuple[date, int]] = [(inicio, salario)]
        """Modificaciones del salario (fecha, salario)"""

    def salario_actual(self) -> int:
        """El salario mas reciente (si se ha modificado)"""
        return self.historial_salarial[-1][1]

    def cambiar_salario(self, salario: int, fecha: date | None = None) -> None:
        self.historial_salarial.append((fecha or self.inicio, salario))

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(self.nombre, "inicio:", self.inicio.strftime(FMT_FECHA), "salario:", self.salario_actual())

class Empleado:
    idAnterior = 0
    def __init__(
        self,
        ci: int,
        nombre: str,
        apellido: str,
        nacimiento: date,
        direccion: str,
        barrio: str,
        ciudad: str,
        puesto: Puesto
    ) -> None:
        Empleado.idAnterior += 1
        self.id: int = Empleado.idAnterior
        """El ID Legajo"""
        self.ci = ci
        """La cedula de identidad"""
        self.nombre = nombre
        """Nombre del empleado"""
        self.apellido = apellido
        """Apellido del empleado"""
        self.nacimiento = nacimiento
        """Fecha de nacimiento"""
        self.direccion = direccion
        """Direccion de hospedaje"""
        self.barrio = barrio
        """Barrio de hospedaje"""
        self.ciudad = ciudad
        """Ciudad de hospedaje"""
        self.puesto = puesto
        """Actual puesto del empleado"""
        self.trabajos_anteriores: list[Puesto] = []
        """Anteriores trabajos en la empresa"""
        self.asistencia = Asistencia()
        self.inactivo: bool = False

    def tiempo_trabajando(self, fecha: date) -> int:
        """Años de trabajo del empleado"""
        delta = (fecha - self.puesto.inicio)
        if delta.days:
            return (delta // 365).days
        else:
            return 0

    def modificar(
        self,
        ci: int | None = None,
        nombre: str | None = None,
        apellido: str | None = None,
        nacimiento: date | None = None,
        direccion: str | None = None,
        barrio: str | None = None,
        ciudad: str | None = None
    ) -> None:
        """Modificar informacion personal"""
        if ci: self.ci = ci
        if nombre: self.nombre = nombre
        if apellido: self.apellido = apellido
        if nacimiento: self.nacimiento = nacimiento
        if direccion: self.direccion = direccion
        if barrio: self.barrio = barrio
        if ciudad: self.ciudad = ciudad

    def modificar_puesto(self, nombre: str | None, salario: int | None, inicio: date | None) -> None:
        if nombre:
            self.trabajos_anteriores.append(Puesto(self.puesto.nombre, self.puesto.salario_actual(), self.puesto.inicio))
            self.puesto = Puesto(nombre, salario or self.puesto.salario_actual(), inicio or self.puesto.inicio)
        elif salario:
            self.puesto.cambiar_salario(salario, inicio)

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(f"ID: {self.id} Nombre: {self.nombre}, {self.apellido} Puesto: {self.puesto.nombre} Salario: {self.puesto.salario_actual()}")

class Descuento:
    def __init__(self, ips: float = 9.5) -> None:
        self.ips = ips

    def desc_llegada_tar(self):
        pass

