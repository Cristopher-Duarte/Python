import math
peso= int (input("Escriba su peso:   "))
altura= float (input("Escriba su altura:  "))
imc = peso/math.pow(altura,2)

if imc<18.5:
    print ("Su IMC es de ",imc," Bajo peso")
elif imc>18.5 and imc< 24.9:
    print ("Su IMC es de ",imc," Normal")
elif imc>25 and imc<29.9:
    print ("Su IMC es de ",imc," Sobrepeso")
elif imc>30 and imc<34.9:
    print ("Su IMC es de ",imc, " Obesidad I")
elif imc>35 and imc<39.9:
    print ("Su IMC es de ",imc, " Obesidad II")
elif imc>40 and imc<49.9:
    print ("Su IMC es de ",imc, " Obesidad III")
elif imc>50:
    print ("Su IMC es de ",imc, " Obesidad IV")
