def añobisiesto(año):
  if(año%4==0 or año%100==0 and año%400==0):
    return "Es bisiesto"
  else:
    return "No es bisiesto"

resultado = añobisiesto(2022)
print(resultado)