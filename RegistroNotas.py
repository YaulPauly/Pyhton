# inicializamos la clase
class Alumno:
    
    def inicializar(usuario,nombre,nota):
        usuario.nombre=nombre
        usuario.nota=nota
 
 
    # función para imprimir los datos
    def imprimir(data):
               print("Nombre: ",data.nombre)
               print("Nota: ",data.nota)
 
 
    # función para obtener el resultado
    def resultado(calificacion):
            if calificacion.nota < 5:
                print("El alumno ha suspendido")
            else:
                print("El alumno ha aprobado")
 
 
 
# bloque principal
# creamos los nuevos objetos
alumno1=Alumno()
alumno2=Alumno()
 
# inicializamos los atributos
alumno1.inicializar("Paul",10)
alumno2.inicializar("Mary",3)
 
# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()