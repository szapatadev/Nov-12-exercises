n = []
i = 0

while i != 5:
  n.append(int(input("Ingresa un numero: ")))
  i += 1
else:
  i = 0
  

while i != 5:
 if n[i] % 2 == 0:
    print(f"El numero {n[i]} es par")
 else:
   print(f"El numero {n[i]} es impar")
 i += 1