numeros = []
i = 0
n = 1
suma = 0

while n != 0:
    n = int(input("Ingresa un numero para sumar, preciona 0 para sumar: "))
    numeros.append(n)
    suma += numeros[i]
    i += 1
else:
    print(f"La suma de todos los valores es {suma}")