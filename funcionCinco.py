#crear una funcion que permita generar 20 modificaciones de una represa
#(0-800) y calcular el promedio de esas modificaciones
#debemos ser capaces de indicar cual es el nivel de operacion de la represa

#crear las mediciones
#calcular promedio
def calcular_nivel_represa(promedioNivel):
    if promedioNivel > 0 and promedioNivel <= 250:
        print( "Nivel Bajo")
    elif promedioNivel > 250 and promedioNivel <= 400:
        print("Nivel Medio")
    elif promedioNivel > 400:
        print("Nivel Alto")
    else:
        print("Nivel Invalido")