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

# Aplicación Streamlit
st.title("Personaje en Streamlit")

# Input inicial
nombre = st.text_input("Nombre del personaje", "Ricardo")
fuerza = st.number_input("Fuerza inicial", value=10)
inteligencia = st.number_input("Inteligencia inicial", value=1)
defensa = st.number_input("Defensa inicial", value=5)
vida = st.number_input("Vida inicial", value=100)

# Crear personaje
mi_personaje = Personaje(nombre, fuerza, inteligencia, defensa, vida)

# Mostrar atributos iniciales
if st.button("Mostrar atributos"):
    st.text(mi_personaje.atributos())

# Subir nivel
st.header("Subir de nivel")
fuerza_nueva = st.number_input("Incremento de fuerza", value=1, key="fuerza_nueva")
inteligencia_nueva = st.number_input("Incremento de inteligencia", value=2, key="inteligencia_nueva")
defensa_nueva = st.number_input("Incremento de defensa", value=0, key="defensa_nueva")

if st.button("Subir nivel"):
    mi_personaje.subir_nivel(fuerza_nueva, inteligencia_nueva, defensa_nueva)
    st.text("Atributos después de subir de nivel:")
    st.text(mi_personaje.atributos())

# Comprobar si el personaje está vivo
st.header("¿Está vivo?")
if st.button("Comprobar estado de vida"):
    if mi_personaje.esta_vivo():
        st.success(f"{mi_personaje.nombre} está vivo.")
    else:
        st.error(f"{mi_personaje.nombre} está muerto.")