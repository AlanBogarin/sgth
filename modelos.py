from datetime import date
from utilidades import FMT_FECHA

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

class Asistencia:
    def __init__(self) -> None:
        self.ausencias: list[Ausencia] = []
        self.llegadas_tardias: list[LlegadaTardia] = []
        self.vacaciones: list[Vacacion] = []
        self.permisos: list[Permiso] = []

    def registrar_ausencia(self, fecha: date, justificacion: str | None) -> None:
        """Registra una ausencia, justificada o no"""
        self.ausencias.append(Ausencia(fecha, justificacion))

    def registrar_llegada_tardia(self, fecha: date) -> None:
        """Registra una llegada tardia"""
        self.llegadas_tardias.append(LlegadaTardia(fecha))

    def registrar_vacacion(self, inicio: date, fin: date) -> None:
        self.vacaciones.append(Vacacion(inicio, fin))

    def registar_permiso(self, fecha: date, motivo: str) -> None:
        self.permisos.append(Permiso(fecha, motivo))

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea (solo cantidades)"""
        print("ausencias:", len(self.ausencias), "llegadas tardias:", len(self.llegadas_tardias), "vacaciones:", len(self.vacaciones), "permisos:", len(self.permisos))

    def mostrar_todo(self) -> None:
        """Mostrar una informacion detallada de varias lineas"""
        print("Ausencias:")
        for ausencia in self.ausencias:
            ausencia.mostrar()
        print("Llegadas Tardias:")
        for llegada_tardia in self.llegadas_tardias:
            llegada_tardia.mostrar()
        print("Vacaciones:")
        for vacacion in self.vacaciones:
            vacacion.mostrar()
        print("Permisos:")
        for permiso in self.permisos:
            permiso.mostrar()

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

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print(f"ID: {self.id} Nombre: {self.nombre}, {self.apellido} Puesto: {self.puesto.nombre} Salario: {self.puesto.salario_actual()}")
