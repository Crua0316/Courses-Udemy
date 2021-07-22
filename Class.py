class personaje:
    life = 100
    damage = 200

    def __init__(self, name, age, velocity):
        self.name = name
        self.age = age
        self.velocity = velocity
    
    def takingDamage(self, dmgRecive):
        self.life -= dmgRecive

personajeO = personaje("Thor", 200, 35)
print ("Name = "+personajeO.name)
print ("Life = "+str(personajeO.life))
print ("Damage = "+str(personajeO.damage))
print ("Age = "+str(personajeO.age))

personajeO.takingDamage(30)
print("Vida actual = "+str(personajeO.life))

personajeO.age = 300
personajeO.velocity = 60
print("Age = "+str(personajeO.age), "Velocity = "+str(personajeO.velocity}))
