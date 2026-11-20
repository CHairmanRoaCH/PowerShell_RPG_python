import rpg_conjuro
import rpg_objeto
import rpg_arma
class Personaje:
    vivo = True

    def __init__(self, nombre, vida_max, vida_actual, magia_max, magia_actual, arma_equipada: rpg_arma.Arma):
        self.nombre_jugador = nombre
        self.vida_max = vida_max
        self.vida_actual = vida_actual
        self.magia_max = magia_max
        self.magia_actual = magia_actual
        self.arma_equipada = arma_equipada

    def jugador_vivo(self):
        if (self.vida_actual <= 0):
            print(f"{self.nombre_jugador} ha muerto")
            vivo = False
            return vivo

    def recibir_danyo(self, danyo):
        self.vida_actual -= danyo

    def atacar(self,enemigo,danyo):
        if danyo == 0:
            print(f"{self.nombre_jugador} ha fallado el ataque\n{enemigo.nombre_jugador} analiza la situación\n")
        
        if danyo > self.arma_equipada.danyo_max:
            print("¡¡IMPACTO CRÍTICO!!")
        if danyo != 0:
            print(f"{self.nombre_jugador} está atacando a {enemigo.nombre_jugador} con el arma {self.arma_equipada.nombre} y ha hecho {danyo} HP\n")

        
    
    def __str__(self):
        return f"\n\t\t{self.nombre_jugador}\n{self.vida_actual} PV / {self.vida_max} PV \t\t{self.magia_actual}/{self.magia_max} PM \n arma: {self.arma_equipada}\n"

class Jugador(Personaje):
    def __init__(self, nombre, vida_max, vida_actual, magia_max, magia_actual, arma_equipada:rpg_arma.Arma, 
                 inventario_objetos:list[rpg_objeto.Objeto], inventario_armas:list[rpg_arma.Arma], inventario_conjuros:list[rpg_conjuro.Conjuro]):
        super().__init__(nombre, vida_max, vida_actual, magia_max, magia_actual, arma_equipada)
        self.inventario_objetos = inventario_objetos
        self.inventario_armas = inventario_armas
        self.inventario_conjuros = inventario_conjuros


    def mostrar_inventario_objetos(self):
        for indice,objeto in enumerate(self.inventario_objetos):
            print(f"({indice}) {objeto}")

    def usar_objeto(self, posicion, enemigo : Enemigo):
        objeto_inventario = self.inventario_objetos[posicion]

        if(objeto_inventario.efecto == "PV"):
            print("Existe objeto PV")
            objeto_inventario : rpg_objeto.Objeto_Curacion
            objeto_inventario.curar(self)

        if(objeto_inventario.efecto == "PM"):
            print("Existe objeto PM")
            objeto_inventario : rpg_objeto.Objeto_Magia
            objeto_inventario.restaurar_magia(self)

        if(objeto_inventario.efecto == "Ataque"):
            objeto_inventario : rpg_objeto.Objeto_Ataque
            danyo = objeto_inventario.danyo_ataque()
            #self.atacar(enemigo, danyo)
            print(f"{self.nombre_jugador} lanza {objeto_inventario.nombre} a {enemigo.nombre_jugador} y provoca {danyo} HP de daño\n")
            enemigo.recibir_danyo(danyo)

        self.inventario_objetos.remove(objeto_inventario)
    #--------------------ARMAS-------------------------------------------------
    def mostrar_inventario_armas(self):
        for arma in self.inventario_armas:
            print(f"({self.inventario_armas.index(arma)}) {arma.nombre}")

    def cambiar_arma_equipada(self, posicion):
        arma_inventario : rpg_arma.Arma = self.inventario_armas[posicion]
        self.inventario_armas.remove(arma_inventario)
        self.inventario_armas.append(self.arma_equipada)
        self.arma_equipada = arma_inventario
    #-----------------------------------------------------------------------------

    #--------------------CONJUROS-------------------------------------------------
    def mostrar_inventario_conjuros(self):
        for indice, conjuro in enumerate(self.inventario_conjuros):
            print(f"({indice}) {conjuro}")

    def usar_conjuro(self, posicion, enemigo:Enemigo):
        conjuro_inventario = self.inventario_conjuros[posicion]
        if(conjuro_inventario.tipo_conjuro == "DAÑO"):
            #self.atacar(enemigo, conjuro_inventario.efecto_conjuro)
            #danyo = conjuro_inventario.efecto_conjuro
            print(f"{self.nombre_jugador} lanza {conjuro_inventario.nombre_conjuro} a {enemigo.nombre_jugador} y provoca {conjuro_inventario.efecto_conjuro} HP de daño\n")
            enemigo.recibir_danyo(conjuro_inventario.efecto_conjuro)
            self.magia_actual -= conjuro_inventario.magia_necesaria
            #print(f"{self.nombre_jugador} usa {conjuro_inventario.nombre_conjuro} contra {enemigo.nombre_jugador}")
    #-------------------------------------------------------------------------------------------------------------------     

    def __str__(self):
        # Extraemos solo los nombres (o la descripción completa si cambias objeto.nombre por str(objeto))
        nombres_objetos = [objeto.nombre for objeto in self.inventario_objetos]
        nombres_armas = [arma.nombre for arma in self.inventario_armas]
        
        # Formateamos las listas como texto limpio
        str_objetos = ", ".join(nombres_objetos) if nombres_objetos else "Vacío"
        str_armas = ", ".join(nombres_armas) if nombres_armas else "Vacío"
        return super().__str__() + f"\nInventario de objetos: {str_objetos} \nInventario armas: {str_armas}\n"


class Enemigo(Personaje):
    def __init__(self, nombre, vida_max, vida_actual, magia_max, magia_actual, arma_equipada : rpg_arma.Arma):
        super().__init__(nombre, vida_max, vida_actual, magia_max, magia_actual, arma_equipada)