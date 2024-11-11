import os
import datetime

FMT_FECHA = "%d-%m-%Y"
"""Formato de fechas"""

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

def pedir_fecha(info: str, min: datetime.date | None = None, max: datetime.date | None = None) -> datetime.date:
    """Asegurar el retorno de una fecha, comprobando si esta en el rango (min, max)"""
    fecha = None
    while not fecha or (min and fecha < min) or (max and fecha > max):
        try:
            fecha = datetime.datetime.strptime(pedir_texto(info), FMT_FECHA).date()
        except ValueError:
            continue
    return fecha

def pedir_fecha_opcional(info: str, min: datetime.date | None = None, max: datetime.date | None = None) -> datetime.date | None:
    """Retorna una fecha si es valida y esta dentro del rango especificado, caso contrario retorna None"""
    while True:
        texto = pedir_texto_opcional(info)
        if texto:
            try:
                fecha = datetime.datetime.strptime(texto, FMT_FECHA).date()
                if (min and fecha < min) or (max and fecha > max):
                    continue
                return fecha
            except ValueError:
                pass
        return None
