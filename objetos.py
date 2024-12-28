import streamlit as st

# Clase Personaje
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        return f"""
        ⚔️ {self.nombre}:
        - Fuerza: {self.fuerza}
        - Inteligencia: {self.inteligencia}
        - Defensa: {self.defensa}
        - ❤️ Vida: {self.vida}
        """

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        return f"💀 {self.nombre} ha muerto."

    def daño(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)
        if enemigo.esta_vivo():
            return f"⚔️ {self.nombre} infligió {daño} puntos de daño a {enemigo.nombre}. ❤️ {enemigo.nombre} ahora tiene {enemigo.vida} de vida."
        else:
            return f"⚔️ {self.nombre} infligió {daño} puntos de daño a {enemigo.nombre}. 💀 {enemigo.morir()}"

# Clase Guerrero
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self, opcion):
        if opcion == 1:
            self.espada = 8
            return "🔪 Cambiaste tu arma a Acero Valyrio (daño 8)."
        elif opcion == 2:
            self.espada = 10
            return "🗡️ Cambiaste tu arma a Matadragones (daño 10)."
        else:
            return "❌ Número de arma incorrecta."

    def atributos(self):
        base_atributos = super().atributos()
        return base_atributos + f"- 🗡️ Espada: {self.espada}\n"

    def daño(self, enemigo):
        return max(0, self.fuerza * self.espada - enemigo.defensa)

# Clase Mago
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        base_atributos = super().atributos()
        return base_atributos + f"- 📖 Libro: {self.libro}\n"

    def daño(self, enemigo):
        return max(0, self.inteligencia * self.libro - enemigo.defensa)

# Instancias de los personajes
goku = Personaje("Goku", 20, 15, 10, 100)
guts = Guerrero("Guts", 20, 15, 10, 100, 5)
vanessa = Mago("Vanessa", 20, 15, 10, 100, 5)

# Aplicación Streamlit
st.title("⚔️ Simulador de Combate RPG con Streamlit")
st.header("Atributos de los Personajes")

# Mostrar atributos iniciales
if st.button("Mostrar atributos de todos los personajes"):
    st.text(goku.atributos())
    st.text(guts.atributos())
    st.text(vanessa.atributos())

# Atacar entre personajes
st.header("⚔️ Realizar Ataques")

# Goku ataca a Guts
if st.button("Goku ataca a Guts"):
    resultado = goku.atacar(guts)
    st.success(resultado)

# Guts ataca a Vanessa
if st.button("Guts ataca a Vanessa"):
    resultado = guts.atacar(vanessa)
    st.success(resultado)

# Vanessa ataca a Goku
if st.button("Vanessa ataca a Goku"):
    resultado = vanessa.atacar(goku)
    st.success(resultado)

# Cambiar arma del Guerrero
st.header("🗡️ Cambiar Arma de Guts")
opcion_arma = st.radio(
    "Selecciona un arma para Guts:",
    options=["Acero Valyrio (daño 8)", "Matadragones (daño 10)"],
    index=0,
)
if st.button("Cambiar arma de Guts"):
    if opcion_arma == "Acero Valyrio (daño 8)":
        st.info(guts.cambiar_arma(1))
    else:
        st.info(guts.cambiar_arma(2))