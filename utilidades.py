import os
import datetime

DESCUENTO_AUSENCIA = 50000
"""Descuento por ausencias"""
DESCUENTO_LLEGADA_TARDIA = 15000
"""Descuento por llegadas tardias"""
DESCUENTO_IPS = 0.095
"""Descuento de seguro IPS"""
BONO_TRABAJO_EXTRA = 0.5
"""Bono del 50% la hora"""
BONO_DIA_FERIADO = 1.0
"""Bono del 100% la hora"""

FMT_FECHA = "%d-%m-%Y"
"""Formato de fechas (Dia-Mes-Año)"""
FMT_FECHA_MES = "%m-%Y"
"""Formato de fechas sin dias (Mes-Año)"""
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

def esperar_tecla() -> None:
    """Detiene el programa hasta que se toque cualquier tecla"""
    os.system("pause")

def limpiar_pantalla() -> None:
    """Eliminar el texto mostrado en pantalla"""
    print("\n" * 50)

def pedir_texto(info: str) -> str:
    """Asegurar el retorno de un texto no vacio"""
    resultado = None
    while not resultado:
        resultado = input(info).strip()
    return resultado

def pedir_texto_opcional(info: str) -> str | None:
    """Retorna None si se ha ingresado espacios en blanco"""
    resultado = input(info).strip()
    if not resultado:
        return None
    return resultado

def pedir_numero(info: str) -> float:
    """Asegurar el retorno de un numero"""
    while True:
        try:
            return float(pedir_texto(info))
        except ValueError:
            continue

def pedir_numero_opcional(info: str) -> float | None:
    """Retorna un numero si es valido sino None"""
    texto = pedir_texto_opcional(info)
    if texto:
        try:
            return float(texto)
        except ValueError:
            pass
    return None

def pedir_numero_positivo(info: str) -> float:
    """Asegurar el retorno de un nummero mayor a cero"""
    resultado = 0.0
    while int(resultado) <= 0:
        resultado = pedir_numero(info)
    return resultado

def pedir_numero_positivo_opcional(info: str) -> float | None:
    """Retorna un numero mayor a cero o None"""
    while True:
        num = pedir_numero_opcional(info)
        if num or num == 0:
            if int(num) <= 0:
                continue
            return num
        return None

def comprobar_feriado(fecha: datetime.date) -> bool:
    """Comprueba si la fecha es un dia feriado"""
    return (fecha.day, fecha.month) in DIAS_FERIADOS

def pedir_fecha(
    info: str,
    min: datetime.date | None = None,
    max: datetime.date | None = None,
    fmt: str | None = None
) -> datetime.date:
    """Asegurar el retorno de una fecha, comprobando si esta en el rango (min, max)"""
    fecha = None
    while not fecha or (min and fecha < min) or (max and fecha > max):
        try:
            fecha = datetime.datetime.strptime(pedir_texto(info), fmt or FMT_FECHA).date()
        except ValueError:
            continue
    return fecha

def pedir_fecha_opcional(
    info: str,
    min: datetime.date | None = None,
    max: datetime.date | None = None,
    fmt: str | None = None
) -> datetime.date | None:
    """Retorna una fecha si es valida y esta dentro del rango especificado, caso contrario retorna None"""
    while True:
        texto = pedir_texto_opcional(info)
        if texto:
            try:
                fecha = datetime.datetime.strptime(texto, fmt or FMT_FECHA).date()
                if (min and fecha < min) or (max and fecha > max):
                    continue
                return fecha
            except ValueError:
                pass
        return None
