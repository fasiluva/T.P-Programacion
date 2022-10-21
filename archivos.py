#Correcta lectura del archivo 

def ingresaArchivo(nombreArchivo):
    """
    ingresaArchivo :: str -> bool

    . Chequea que el archivo existe. Devuelve true si existe, false si no.
    """
    
    archivoEnExtension = nombreArchivo + '.txt'
    
    if not chequeaArchivo(archivoEnExtension): # SI EL ARCHIVO NO EXISTE, DEVUELVE FALSE
        print('\nEl archivo no ha sido encontrado. ')
        return False
    
    return True
    
def chequeaArchivo(archivoEnExtension):
    """
    chequeaArchivo :: str -> bool

    . Chequea que el archivo exista en el directorio. Si existe, devuelve true, sino devuelve false.
    """

    try: 
        archivoExiste = open(archivoEnExtension)
        archivoExiste.close()

    except:
        return False
        
    else: 
        return True


