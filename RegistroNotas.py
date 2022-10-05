# inicializamos la clase
class Alumno:
    
    def __init__(usuario,nombre,nota):
        usuario.nombre=nombre
        usuario.nota=nota
  
    # función para obtener el resultado
    def resultado(calificacion):
            if calificacion.nota < 5:
                print("El alumno ha suspendido")
            else:
                print("El alumno ha aprobado")
 
 
 
# bloque principal
# creamos los nuevos objetos
# inicializamos los atributos              
alumno1=Alumno("Paul",10)
alumno2=Alumno("Mary",3)
  
# imprimimos los datos y resultados de cada alumno
print("Nombre:",alumno1.nombre)
print("Nota:",alumno1.nota)
alumno1.resultado()
print("Nombre:",alumno2.nombre)
print("Nota:",alumno2.nota)
alumno2.resultado()