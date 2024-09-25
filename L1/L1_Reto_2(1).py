corriente = float(input("Escriba la corriente: "))
voltaje = float(input("Escriba el voltaje: "))

resistencia = voltaje/corriente
potencia = voltaje * corriente

print(f"La resistencia es: {resistencia} ohmios")
print(f"La potencia es: {potencia} watts")