import rpg_personaje
class Objeto:
    def __init__(self, nombre_objeto:str, cantidad_efecto:int, efecto_objeto:str):
        self.nombre = nombre_objeto
        self.cantidad_efecto = cantidad_efecto
        self.efecto = efecto_objeto

    def __str__(self):
        return f"{self.nombre} : {self.cantidad_efecto} {self.efecto}"

class Objeto_Curacion(Objeto):
    def __init__(self, nombre_objeto, cantidad_efecto, efecto_objeto):
        super().__init__(nombre_objeto, cantidad_efecto, efecto_objeto)
        

    def curar(self, jugador: rpg_personaje.Jugador):
        print("He entrado en el método curar")
        if(jugador.vida_actual < jugador.vida_max):
            jugador.vida_actual += self.cantidad_efecto
            if(jugador.vida_actual >= jugador.vida_max):
                jugador.vida_actual = jugador.vida_max

        print(f"se han curado {self.cantidad_efecto} {self.efecto} de {jugador.nombre_jugador}")

class Objeto_Magia(Objeto):
    def __init__(self, nombre_objeto, cantidad_efecto, efecto_objeto):
        super().__init__(nombre_objeto, cantidad_efecto, efecto_objeto)


    def restaurar_magia(self, jugador:rpg_personaje.Jugador):
        if(jugador.magia_actual < jugador.magia_max):
            jugador.magia_actual += self.cantidad_efecto
            if(jugador.magia_actual >= jugador.magia_max):
                jugador.magia_actual = jugador.magia_max

class Objeto_Ataque(Objeto):
    def __init__(self, nombre_objeto, cantidad_efecto, efecto_objeto):
        super().__init__(nombre_objeto, cantidad_efecto, efecto_objeto)

    def danyo_ataque(self):
        return self.cantidad_efecto
