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
        {self.nombre}:
        - Fuerza: {self.fuerza}
        - Inteligencia: {self.inteligencia}
        - Defensa: {self.defensa}
        - Vida: {self.vida}
        """

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        return f"{self.nombre} ha muerto."

    def daño(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)
        return f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}. La vida de {enemigo.nombre} ahora es {enemigo.vida}."

# Aplicación Streamlit
st.title("Personaje en Streamlit")

# Crear Personaje Principal
st.header("Personaje Principal")
nombre = st.text_input("Nombre del personaje", "Ricardo", key="nombre_personaje")
fuerza = st.number_input("Fuerza inicial", value=10, key="fuerza_personaje")
inteligencia = st.number_input("Inteligencia inicial", value=1, key="inteligencia_personaje")
defensa = st.number_input("Defensa inicial", value=5, key="defensa_personaje")
vida = st.number_input("Vida inicial", value=100, key="vida_personaje")
mi_personaje = Personaje(nombre, fuerza, inteligencia, defensa, vida)

# Crear Enemigo
st.header("Enemigo")
nombre_enemigo = st.text_input("Nombre del enemigo", "Jose A", key="nombre_enemigo")
fuerza_enemigo = st.number_input("Fuerza inicial", value=8, key="fuerza_enemigo")
inteligencia_enemigo = st.number_input("Inteligencia inicial", value=5, key="inteligencia_enemigo")
defensa_enemigo = st.number_input("Defensa inicial", value=3, key="defensa_enemigo")
vida_enemigo = st.number_input("Vida inicial", value=100, key="vida_enemigo")
mi_enemigo = Personaje(nombre_enemigo, fuerza_enemigo, inteligencia_enemigo, defensa_enemigo, vida_enemigo)

# Mostrar atributos
if st.button("Mostrar atributos de ambos personajes"):
    st.text("Atributos del Personaje Principal:")
    st.text(mi_personaje.atributos())
    st.text("Atributos del Enemigo:")
    st.text(mi_enemigo.atributos())

# Realizar ataque
st.header("Realizar ataque")
if st.button("Atacar enemigo"):
    resultado_ataque = mi_personaje.atacar(mi_enemigo)
    st.success(resultado_ataque)
    st.text("Atributos del enemigo después del ataque:")
    st.text(mi_enemigo.atributos())
    if not mi_enemigo.esta_vivo():
        st.error(f"{mi_enemigo.nombre} ha muerto.")

# Subir nivel al personaje principal
st.header("Subir de nivel")
fuerza_nueva = st.number_input("Incremento de fuerza", value=1, key="fuerza_subir")
inteligencia_nueva = st.number_input("Incremento de inteligencia", value=2, key="inteligencia_subir")
defensa_nueva = st.number_input("Incremento de defensa", value=0, key="defensa_subir")

if st.button("Subir nivel del personaje principal"):
    mi_personaje.subir_nivel(fuerza_nueva, inteligencia_nueva, defensa_nueva)
    st.success("Personaje principal subió de nivel.")
    st.text(mi_personaje.atributos())