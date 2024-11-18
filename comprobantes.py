from utilidades import esperar_tecla, limpiar_pantalla, pedir_numero

def generar_comprobantes(): pass
def generar_informe(): pass

def generacion_comprobantes() -> None:
    """Descripcion del PDF

    - Emisión de recibos de pago detallados para los empleados. 
    - Generación de informes y reportes para Talento humano (Monto total
        del sueldo a ser pagado, Monto total por IPS empleado/empresa, Detalle
        de descuentos y pagos en un rango de meses para un empleado, etc.)
    """
    while True:
        limpiar_pantalla()
        # 16 + 1 + 16 + 1 + 16
        print("=" * 16, "MENU COMPROBANTE", "=" * 16)
        print("1. Generar comprobantes")
        print("2. Generar informe")
        print("0. Regresar")
        match pedir_numero("Ingrese una opcion: "):
            case 1: pass
            case 2: pass
            case 0: break
            case _: print("Opción Invalida")
        esperar_tecla()
