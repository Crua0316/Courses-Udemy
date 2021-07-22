# Class padre
class personaje:
    # Variables
    Comida = 50 # 0 esta hambriento y 100 no esta hambriento
    # Contructor con propiedades
    def __init__(self, name, age, velocity, fuerza):
        self.name = name
        self.age = age
        self.velocity = velocity
        self.fuerza = fuerza

    # métodos
    def __isHungry(self):
        return self.Comida < 50
    def pasandohambre(self , Comida):
        self.Comida -= Comida
    def eat(self):
        if self.__isHungry():
            self.Comida += 10
    def defend(self):
        print(self.name+" se ha defendido de su enemigo")

# Hijos
class Otherpersonaje(personaje):
    pass

class personaje2(personaje):
    def __init__(self, name, age, velocity, fuerza, power):
        super().__init__(name, age, velocity, fuerza)
        self.power = power
    def typeofpower(self):
        print("Water")

# Main
personaje1 = Otherpersonaje("Luis", 17, 15, 45)
personaje1.defend()

Personaje2 = personaje2("Carlos", 20, 35, 55, "Water")
print (Personaje2.name)
Personaje2.typeofpower()
