from enum import Enum

class choicepersonaje:
    Thor = 1
    Loki = 2
    IronMan = 3
    Hulk = 4

class Personaje (Enum):
    Thor = 1
    Loki = 2
    IronMan = 3
    Hulk = 4

print(choicepersonaje.Loki)
print(Personaje.Thor)

if Personaje.Thor is Personaje.thor:
    print ("Ha seleccionado a Thor")
