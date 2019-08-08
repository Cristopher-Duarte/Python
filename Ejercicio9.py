class Empleado:
    def __init__(self):
        self.codigo=""
        self.nombres=""
        self.apellidos=""
        self.salariobase=""

        
    def retencion (self):
        tot=(self.salariobase*0.1)
        return tot

        
    def datos(self):
        Datos=self.nombres+" "+self.apellidos+" ",self.codigo
        return Datos

    
    def salarioneto (self):
        if(self.salariobase <=828116):
            neto=(self.salariobase+97032)-(self.salariobase*0.1)
        else:
            neto=(self.salariobase)-(self.salariobase*0.1)
            return neto
        

        
emp=Empleado()
emp.codigo=float(input("Ingrese el codigo "))
emp.nombres=input("Ingrese su nombre ")
emp.apellidos=input("Ingrese su apellido ")
emp.salariobase=float(input("Ingrese su salario base "))
print(emp.retencion())
print(emp.salarioneto())
print(emp.datos())


