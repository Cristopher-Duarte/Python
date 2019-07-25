edad =int(input("Digite su edad "))
genero= input("Digite sexo, M para Masculino, F para Femenino ")

if edad>=18:
    if genero=="M" or genero=="m":
        input("Señor, usted es mayor de edad")
    elif genero=="F" or genero=="f":
        input("Señora, usted es mayor de edad")
    else:
        input ("Dato Incorrecto")
else:
    if genero=="F" or genero=="f": 
        input ("Señora, usted es menor de edad")
    elif genero=="M" or genero=="m":
        input ("Señor, uste es menor de edad")
    else:
        print("Dato Incorrecto")
