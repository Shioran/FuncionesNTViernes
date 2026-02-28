#crear una lista de 20 notas
import random

def crear_lista(cantidadElementos,rangoInicial,rangoFinal):
    lista=[]
    for _ in range(cantidadElementos):
        lista.append(random.randint(rangoInicial,rangoFinal))
        return lista