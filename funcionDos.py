import random
def crearListaNotas(cantidadNotas):
    notas=[]
    for _ in range (cantidadNotas):
        notas.append(random.randint(1,5))
    return notas

print(crearListaNotas(20))