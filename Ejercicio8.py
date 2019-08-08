class Empleado:
    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.edad=21

    def saludar(self):
        return "Hola me llamo "+ self.nombre
    def saludar2(self):
        print ("Hola me llamo "+ self.nombre+ " el saludar2")



emp = Empleado()
emp.nombre = "Cristopher"
print(emp.saludar())
