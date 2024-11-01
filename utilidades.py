import os
from datetime import date, datetime

SEPARADOR = "|" + "-" * 80

FMT_LINEA = "| {}"
FMT_SEP_LINEA = f"{SEPARADOR}\n{FMT_LINEA}"
FMT_TITULO = f"{SEPARADOR}\n" + "{}" + f"\n{SEPARADOR}"

def pycharm():
    return os.getenv("PYCHARM_HOSTED") == "YES"

def esperar_tecla():
    print(FMT_SEP_LINEA.format(""), end="")
    os.system("pause")

def limpiar_pantalla():
    if pycharm():
        print("\n" * 30)
    else:
        os.system("cls||clear")

def pedir_texto(texto: str) -> str:
    respuesta = None
    while not respuesta:
        respuesta = input(texto).strip()
    return respuesta

def pedir_numero(texto: str) -> float:
    numero = None
    while numero is None:
        try:
            numero = float(pedir_texto(texto))
        except ValueError:
            continue
    return numero

def pedir_numero_positivo(texto: str) -> float:
    numero = 0.0
    while numero <= 0:
        numero = pedir_numero(texto)
    return numero

def pedir_fecha(texto: str) -> date:
    fecha = None
    while not fecha:
        respuesta = pedir_texto(texto)
        if "-" in respuesta:
            fmt = "%d-%m-%Y"
        else:
            fmt = "%d/%m/%Y"
        try:
            fecha = datetime.strptime(respuesta, fmt).date()
        except ValueError:
            continue
    return fecha

def mostrar_menu(opciones: list[tuple[int, str]]):
    menu = ""
    for n, opcion in opciones:
        menu += FMT_LINEA.format(f"{n}. {opcion}") + "\n"
    print(FMT_TITULO.format(menu.strip()))
