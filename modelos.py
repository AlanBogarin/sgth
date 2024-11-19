from datetime import date
from utilidades import (
    BONO_DIA_FERIADO,
    BONO_TRABAJO_EXTRA,
    DESCUENTO_AUSENCIA,
    DESCUENTO_IPS,
    DESCUENTO_LLEGADA_TARDIA,
    FMT_FECHA,
    FMT_FECHA_MES,
    comprobar_feriado
)

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
        if comprobar_feriado(fecha):
            self.feriados_trabajados.append(FeriadoTrabajado(fecha))

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
        print(f"id: {self.id} nombre: {self.nombre}, {self.apellido} puesto: {self.puesto.nombre} salario: {self.puesto.salario_actual()}")

class RegistroSalarial:
    def __init__(self, fecha: date, empleado: Empleado) -> None:
        self.fecha = fecha
        self.empleado = empleado
        self.salario = empleado.puesto.salario_actual()
        """Salario bruto"""
        # descuento
        self.ausencias: list[Ausencia] = []
        """Ausencias del mes"""
        self.llegadas_tardias: list[LlegadaTardia] = []
        """Llegadas tardias del mes"""
        # neutral
        self.vacaciones = empleado.asistencia.vacaciones
        self.permisos = empleado.asistencia.permisos
        self.incapacidades = empleado.asistencia.incapacidades
        self.licensias = empleado.asistencia.licensias
        # aumento
        self.trabajos_extra: list[TrabajoExtra] = []
        """Trabajos extras del mes"""
        self.feriados_trabajados: list[FeriadoTrabajado] = []
        """Feriados trabajados del mes"""
        # filtrar los registros que sean de la fecha ingresada
        for ausencia in empleado.asistencia.ausencias:
            if (ausencia.fecha.month, ausencia.fecha.year) == (fecha.month, fecha.year):
                self.ausencias.append(ausencia)
        for llegada in empleado.asistencia.llegadas_tardias:
            if (llegada.fecha.month, llegada.fecha.year) == (fecha.month, fecha.year):
                self.llegadas_tardias.append(llegada)
        for extra in empleado.asistencia.trabajos_extra:
            if (extra.fecha.month, extra.fecha.year) == (fecha.month, fecha.year):
                self.trabajos_extra.append(extra)
        for feriado in empleado.asistencia.feriados_trabajados:
            if (feriado.fecha.month, feriado.fecha.year) == (self.fecha.month, self.fecha.year):
                self.feriados_trabajados.append(feriado)

    def salario_por_hora(self) -> float:
        """Calcula el salario bruto por hora"""
        return round(self.salario / 30 / 8, 2)

    def descuento_ausencia(self) -> float:
        """Calcula el descuento por ausencias del mes"""
        return len(self.ausencias) * DESCUENTO_AUSENCIA

    def descuento_llegada_tardia(self) -> float:
        """Calcula el descuento por llegadas tardias del mes"""
        return len(self.llegadas_tardias) * DESCUENTO_LLEGADA_TARDIA

    def calcular_descuentos(self) -> float:
        """Calcula la tarifa final del descuento por faltas"""
        return self.descuento_ausencia() + self.descuento_llegada_tardia()

    def bono_trabajo_extra(self) -> float:
        """Calcula el bono por trabajos extras del mes"""
        bono = 0.0
        salario_por_hora = self.salario_por_hora()
        for extra in self.trabajos_extra:
            if comprobar_feriado(extra.fecha):
                porcentaje = BONO_DIA_FERIADO
            else:
                porcentaje = BONO_TRABAJO_EXTRA
            bono += extra.horas * (salario_por_hora + salario_por_hora * porcentaje)
        return round(bono, 2)

    def bono_feriado_trabajado(self) -> float:
        """Calcula el bono por trabajos en dias feriados/festivos del mes"""
        bono = 0.0
        salario_por_hora = self.salario_por_hora()
        for feriado in self.feriados_trabajados:
            for extra in self.trabajos_extra:
                # comprueba si ya se incluyo como trabajo extra
                if extra.fecha == feriado.fecha:
                    break
            else:
                # solo si no se calcula como trabajo extra, para evitar calculo duplicado
                bono += 8 * (salario_por_hora + salario_por_hora * BONO_DIA_FERIADO)
        return round(bono, 2)

    def calcular_bonos(self) -> float:
        """Calcula la tarifa de aumento por bonos"""
        return self.bono_trabajo_extra() + self.bono_feriado_trabajado()

    def calcular_salario_neto(self) -> float:
        """Calcula el salario neto (sin IPS)"""
        return self.salario + self.calcular_bonos() - self.calcular_descuentos()

    def calcular_ips(self) -> float:
        """Calcula el descuento IPS"""
        return round(self.calcular_salario_neto() * DESCUENTO_IPS, 2)

    def calcular_salario(self) -> float:
        """Calcula el salario total del empleado incluyendo horas extras y deducciones."""
        return round(self.calcular_salario_neto() - self.calcular_ips(), 2)

    def mostrar(self) -> None:
        """Mostrar una informacion basica de una sola linea"""
        print("id:", self.empleado.id, "descuentos:", self.calcular_descuentos(), "bonos:", self.calcular_bonos(), "salario:", self.calcular_salario())

class RegistroMensual:
    def __init__(self, fecha: date, registros: list[RegistroSalarial] | None = None) -> None:
        self.fecha = fecha
        """Fecha del registro (mes, año)"""
        self.registros = registros or []
        """Registros de empleados (id, registro)"""

    def agregar_registro(self, registro: RegistroSalarial) -> None:
        """Agrega un nuevo registro salarial"""
        anterior = None
        for reg in self.registros:
            if reg.empleado.id == registro.empleado.id:
                anterior = reg
        if anterior:
            # borra el registro anterior del empleado
            self.registros.remove(anterior)
        self.registros.append(registro)

    def pago_ips(self) -> float:
        """Monto a pagar a IPS (suma de todos los IPS de empleados)"""
        monto = 0.0
        for registro in self.registros:
            monto += registro.calcular_ips()
        return round(monto, 2)

    def pago_empleados(self) -> float:
        """Monto a pagar a empleados (suma de todos los salarios)"""
        monto = 0.0
        for registro in self.registros:
            monto += registro.calcular_salario()
        return round(monto, 2)

    def mostrar(self) -> None:
        print(self.fecha.strftime(FMT_FECHA_MES), "registros:", len(self.registros))
