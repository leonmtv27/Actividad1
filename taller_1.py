#1
masa = float(input('Ingrese su peso en Kg:'))
altura = float(input('Ingrese su altura en metros'))
imc = masa/altura**2
print(imc)
"""
#2.
def costo_llamada(destino, duracion):

  costos_por_minuto = {
    "Estados Unidos": 900,
    "Canadá": 800,
    "Europa": 950,
    "Resto del mundo": 1250,
  }

  # Descuento por duración
  descuento = 0.2 if duracion > 15 else 0

  # Calcular el costo total
  costo_total = duracion * costos_por_minuto[destino] * (1 - descuento)

  return costo_total

# Ejemplo
destino = str(input("Ingrese el destino:"))
duracion = int(input("Ingrese la duracion de la llamada:"))

costo_total = costo_llamada(destino, duracion)

print(f"El costo total de la llamada es: {costo_total:.2f} pesos")
"""

#4.
nota1 = float(input("Ingrese nota 1:"))
nota2 = float(input("Ingrese nota 2:"))
nota3 = float(input("Ingrese nota 3:"))
nota4 = float(input("Ingrese nota 4:"))

promedio = (nota1 + nota2 + nota3 + nota4) / 4
matricula = float(input("Ingrese el valor normal de su matricula:"))

if promedio >=4 and promedio <=5:
  print("El rendimiento es excelente")
elif promedio >=3 and promedio <4:
  print("El rendimiento fue bueno")
else:
  print("El rendimiento fue deficiente")