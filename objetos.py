class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".Inteligencia:", self.inteligencia)
        print(".Defensa:", self.defensa)
        print(".Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia 
        self.defensa = self.defensa + defensa

'''mi_personaje = Personaje()'''
mi_personaje = Personaje("Ricardo", 10, 1, 5, 100)
'''print("El nombre del jugador es: \n", mi_personaje.nombre)
print("La fuerza del jugador es: \n", mi_personaje.fuerza)'''
mi_personaje.atributos()
mi_personaje.subir_nivel(1, 2, 0)
mi_personaje.atributos()