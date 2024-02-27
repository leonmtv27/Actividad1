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