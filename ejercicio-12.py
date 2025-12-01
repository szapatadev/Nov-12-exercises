nota = int(input("Pon la nota que sacaste "))

if nota > 5 or nota < 1:
    print("Tiene que ser una nota de 1 - 5, volver a ejecutar")
elif nota > 3:
    print(f"Aprovaste con {nota}")
else:
    print(f"Reprobaste con {nota}")