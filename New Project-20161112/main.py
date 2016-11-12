# práctica de Python

class Persona:
        nombre=""
        edad=0
        
        def __init__(self, nombre, edad):
            self.nombre=nombre
            self.edad=edad
        
        def setNombre (self, nombre):
            self.nombre=nombre
        
        def setEdad(self, edad):
            self.edad=edad
        
        def printPersona(self):
            print(self.nombre + " edad:"+str(self.edad))
            
        def esMayorDeEdad(self):
            if (self.edad >= 18):
                return (True)
            else:
                return (False)
                
        def esMayorQue(self, p):
            if (self.edad > p.edad):
                print(self.nombre+" es mayor que "+p.nombre)
            else:
                print(self.nombre+" es menor que "+p.nombre)
    
p=Persona("Orlando", 14)

p2=Persona("Adriana", 15)


p.printPersona()
if (p.esMayorDeEdad()):
    print (p.nombre+ " es mayor")
else:
    print (p.nombre+ " es menor")
p2. printPersona()
if (p2.esMayorDeEdad()):
    print (p2.nombre+ " es mayor")
else:
    print (p2.nombre+ " es menor")
    
p2.esMayorQue(p)
