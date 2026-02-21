def crear_lista_estudiantes(cantidadEstudiantes):
    estudiantes=[]
    for i in range (cantidadEstudiantes):
        estudiante={}
        estudiante["id"]=input("id: ")
        estudiante["nombre"]=input("nombre: ")
        estudiante["documento"]=input("documento: ")
        estudiante["correo"]=input("correo: ")
        estudiante["telefono"]=input("telefono: ")
        estudiante["promedio"]=input("promedio: ")
        estudiante["semestre"]=input("semestre: ")
        estudiante["becado"]=input("eres becado?: ")
        estudiantes.append(estudiante)
    return estudiantes

#invocando la funciom
resultado=crear_lista_estudiantes(2)
print(resultado)