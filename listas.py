#necesito crear un programa que almacene una lista de 200 personas
import random

notas=[]
for i in range (5):
    notaSimulada=random.random()
    notas.append(notaSimulada)
print(notas)

#metodos para transformar, modificar o administrar listas
notas.insert(0,80)
#notas.remove(80)
notas.pop(0)
notas.sort()
notas.sort(reverse=True)
notas.clear()
print(notas)


#for i in range (notas.__len__()):
    #print(notas[i])