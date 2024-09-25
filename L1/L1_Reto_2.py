voltaje = float(input("Introduzca la tensión en voltios: "))
corriente = float(input("Introduzca la corriente en Amperios: "))
resistencia = voltaje / corriente
potencia = voltaje * corriente
print(f"La resistencia equivalente en Ohmios es: {resistencia:.2f}")
print(f"La potencia en Watts es: {potencia:.2f}")