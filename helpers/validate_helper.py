import time

def validarOpcion(opcion, ini, fin):
    try:
        if int(opcion) >= ini and int(opcion) <= fin:
            return True
        else:
            return False
    except:
        return False
    
def cerrarApp():
    print("¡Gracias por usar el Sistema! Saliendo...")
    time.sleep(3)
    SystemExit