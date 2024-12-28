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

    def daño(self, enemigo):
        return max(0, self.fuerza * self.espada - enemigo.defensa)

# Clase Mago
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def daño(self, enemigo):
        return max(0, self.inteligencia * self.libro - enemigo.defensa)

# Configuración inicial de los personajes
if "goku" not in st.session_state:
    st.session_state.goku = Personaje("Goku", 20, 15, 10, 100)
if "guts" not in st.session_state:
    st.session_state.guts = Guerrero("Guts", 20, 15, 10, 100, 5)
if "vanessa" not in st.session_state:
    st.session_state.vanessa = Mago("Vanessa", 20, 15, 10, 100, 5)

# Función para mostrar atributos de todos los personajes
def mostrar_atributos():
    st.text("Goku:")
    st.text(st.session_state.goku.atributos())
    st.text("Guts:")
    st.text(st.session_state.guts.atributos())
    st.text("Vanessa:")
    st.text(st.session_state.vanessa.atributos())

# Aplicación Streamlit
st.title("⚔️ Simulador de Combate RPG con Atributos Dinámicos")

# Mostrar atributos de los personajes dinámicamente
st.header("Atributos de los Personajes")
mostrar_atributos()

# Atacar entre personajes
st.header("⚔️ Realizar Ataques")
if st.button("Goku ataca a Guts"):
    st.session_state["resultado"] = st.session_state.goku.atacar(st.session_state.guts)

if st.button("Guts ataca a Vanessa"):
    st.session_state["resultado"] = st.session_state.guts.atacar(st.session_state.vanessa)

if st.button("Vanessa ataca a Goku"):
    st.session_state["resultado"] = st.session_state.vanessa.atacar(st.session_state.goku)

if "resultado" in st.session_state:
    st.success(st.session_state["resultado"])

# Cambiar arma del Guerrero
st.header("🗡️ Cambiar Arma de Guts")
opcion_arma = st.radio(
    "Selecciona un arma para Guts:",
    options=["Acero Valyrio (daño 8)", "Matadragones (daño 10)"],
    index=0,
    key="arma_guts",
)
if st.button("Cambiar arma de Guts"):
    if opcion_arma == "Acero Valyrio (daño 8)":
        st.info(st.session_state.guts.cambiar_arma(1))
    else:
        st.info(st.session_state.guts.cambiar_arma(2))

# Actualización de estadísticas después de cada interacción
st.divider()
st.header("📊 Estadísticas Actualizadas")
mostrar_atributos()