class Vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 4
    
class Coche(Vehiculo):
  velocidad = 50
  cilindrada = 4

c= Coche()
print("El color del coche es:",c.color)
print("La cantidad de ruedas es:",c.ruedas)
print("La cantidad de puertas es:",c.puertas)
print("La velocidad del coche es:",c.velocidad)
print("La cantidad de cilindros es:",c.cilindrada)