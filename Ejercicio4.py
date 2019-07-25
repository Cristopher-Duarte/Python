num1= int (input("Escriba un numero:   "))
num2= int (input("Escriba otro numero: "))
operacion= int(input("Digite 1 para suma , 2 para resta, 3 para multiplicacion, 4 division  "))

if operacion==1:
    print("La suma es: ",(num1+num2))
elif operecion==2:
    print("La resta es: ",(num1-num2))
elif operacion==3:
    print("La multiplicacion es: ",(num1*num2))
elif operacion==4:
     print("La division es: ",(num1/num2))
else:
     print("Por favor ingrese un valor correcto para la operacion ")
    
    
