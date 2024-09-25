n = eval(input("Escriba un número mayor a 0: "))
if n > 0:
    while n > 0:
        print(n)
        n = n-1
    print("Blastoff")
else:
    print("Escriba un número positivo")