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
        resultado = input(info)
    return resultado

def pedir_numero(info: str) -> float:
    """Asegurar el retorno de un numero"""
    while True:
        try:
            return float(pedir_texto(info))
        except ValueError:
            continue

def pedir_numero_positivo(info: str) -> float:
    """Asegurar el retorno de un nummero mayor a cero"""
    resultado = 0.0
    while resultado <= 0:
        resultado = pedir_numero(info)
    return resultado

def pedir_fecha(info: str, min: datetime.date | None = None, max: datetime.date | None = None) -> datetime.date:
    """Asegurar el retorno de una fecha, comprobando si esta en el rango (min, max)"""
    fecha = None
    while not fecha or (min and fecha < min) or (max and fecha > max):
        try:
            fecha = datetime.datetime.strptime(pedir_texto(info), FMT_FECHA).date()
        except ValueError:
            continue
    return fecha
