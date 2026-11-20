import random
import rpg_objeto
import rpg_arma
import rpg_conjuro
import rpg_personaje

def elegir_nombre():
    
    while(True):
        nombre = input("Elige el nombre de tu jugador:\n")

        if nombre.isalpha():
            return nombre
        
        else:
            print("Formato erróneo de nombre\n")

    

def elegir_arma():

    while(True):
        try:
            print("" \
            "1. Espada [10 - 15 (danyo)]\n" \
            "2. Garrote [8 - 17 (danyo)]\n" \
            "3. Daga [11 - 13 (danyo)]\n")

            opcion = int(input("Elige un arma:\n"))

            match opcion:

                case 1:
                    arma_jugador = rpg_arma.Arma("ESPADA", 10, 15,0.1,0.3,2)                    
                    
                case 2:

                    arma_jugador = rpg_arma.Arma("GARROTE", 8, 17,0.0, 0.5,2)

                case 3:
                    arma_jugador = rpg_arma.Arma("DAGA", 11, 13,0.3,0.5,2)

                case _:
                    print("No has seleccionado ningun arma\nVuelve a intentarlo")

            print(f"Has seleccionado {arma_jugador.nombre}")
            return arma_jugador

        except:
            print("Formato erroneo\n")


def crear_personaje():
    
    nombre = elegir_nombre()
    arma_jugador = elegir_arma()
    sin_arma = rpg_arma.Arma("PUÑETAZOS", 1, 3,0,0.3,5)
    vida_max = 80
    vida_actual = 80
    magia_max = 15
    magia_actual = 15
    inventario_objetos = []
    inventario_armas = [sin_arma]
    inventario_conjuros = []
    return rpg_personaje.Jugador(nombre, vida_max, vida_actual, magia_max, magia_actual, arma_jugador, inventario_objetos, inventario_armas, inventario_conjuros)


def combate_personaje(jugador: rpg_personaje.Jugador, enemigo: rpg_personaje.Enemigo):
 
    enCombate = True
    while(True):
        print("\n\t(1) Atacar\t(2) Consultar Estado\t(3) Inventario\t(4) Huir\n")
        try:
            opcion = int(input())

            match opcion:
                case 1:
                    print("\n\t---Atacar---\n")
                    
                    danyo = jugador.arma_equipada.danyo_aleatorio()
                    danyo = jugador.arma_equipada.calcular_probabilidad_critico(danyo)
                    jugador.atacar(enemigo, danyo)
                    enemigo.recibir_danyo(danyo)
                    if(enemigo.vida_actual <= 0):
                        print(f"{jugador.nombre_jugador} ha vencido a {enemigo.nombre_jugador}\n")


                case 2:
                    print("\n\t---Consultar estado---\n")
                    print(jugador)
                    print(enemigo)

                    #Volver al menú de combate
                    continue

                case 3:
                    print("\n\t---Inventario---\n")
                    print("\t (1) OBJETOS \t (2) ARMAS\t (3) CONJUROS")
                    try:
                        opcion = int(input())
                        if(opcion == 1):
                            jugador.mostrar_inventario_objetos()
                            try:
                                posicion = int(input())
                                jugador.usar_objeto(posicion, enemigo)
                                #objeto_inventario = jugador.inventario_objetos[posicion]
                                #objeto_inventario.curar(jugador)
                                #jugador.inventario_objetos.remove(objeto_inventario)

                            except:
                                
                                #Volver al menú de combate
                                continue
                            
                        if(opcion == 2):
                            jugador.mostrar_inventario_armas()
                            try:
                                posicion = int(input())
                                jugador.cambiar_arma_equipada(posicion)

                            except:
                                
                                #Volver al menú de combate
                                continue

                        if(opcion == 3):
                            jugador.mostrar_inventario_conjuros()
                            try:
                                posicion = int(input())
                                jugador.usar_conjuro(posicion, enemigo)
                                

                            except:
                                
                                #Volver al menú de combate
                                continue
                    except:
                        
                        #Volver al menú de combate
                        continue

                case 4:
                    print("\n\t---Huir---\n")
                    print(f"{jugador.nombre_jugador} es pusilánime y ha huido\n")
                    enCombate = False
                    
                case _:
                    print()
                    continue

            return enCombate
        except:
            print()

def combate_enemigo(enemigo: rpg_personaje.Enemigo, jugador: rpg_personaje.Jugador):

    danyo = enemigo.arma_equipada.danyo_aleatorio()
    #danyo = enemigo.arma_equipada.calcular_probabilidad_critico(danyo)
    enemigo.atacar(jugador, danyo)
    jugador.recibir_danyo(danyo)

    if(jugador.vida_actual <= 0):
        print(f"{enemigo.nombre_jugador} ha vencido a {jugador.nombre_jugador}\n")


#OBJETOS
pocion_curacion = rpg_objeto.Objeto_Curacion("Pocion", 45, "PV")
pocion_magia = rpg_objeto.Objeto_Magia("Poción mágica", 10, "PM")
bomba_incendiaria = rpg_objeto.Objeto_Ataque("Bomba incendiaria", 13, "Ataque")


#ARMAS ENEMIGOS

latigo = rpg_arma.Arma("LATIGO", 5, 12,0.3, 0.5,2)
lanza = rpg_arma.Arma("LANZA", 3, 27,0.3,0.5,2)
arco_maestro = rpg_arma.Arma("ARCO", 7, 32,0.3,0.5,2)
escalibur = rpg_arma.Arma("ESCALIBUR", 23, 25,0.3,0.5,2)

'''
latigo = rpg_arma.Arma("LATIGO", 5, 12, 0, 4, 1.15)
lanza = rpg_arma.Arma("LANZA", 3, 27, 0, 5, 1.15)
arco_maestro = rpg_arma.Arma("ARCO", 7, 32, 0, 6, 1.15)
escalibur = rpg_arma.Arma("ESCALIBUR", 23, 25, 0, 3, 1.15)
'''
armas = [latigo, lanza, arco_maestro,escalibur]

#ENEMIGOS
goblin = rpg_personaje.Enemigo("GOBLIN", 60, 60, 10, 10, latigo)
limo = rpg_personaje.Enemigo("LIMO", 23, 23, 30, 30, lanza)
trol = rpg_personaje.Enemigo("TROL", 120, 120, 0, 0, arco_maestro)
encapuchado = rpg_personaje.Enemigo("ENCAPUCHADO", 80, 80, 13, 13, "")
encapuchado.arma_equipada = random.choice(armas)

enemigos : list[rpg_personaje.Enemigo] = [goblin, limo, trol, encapuchado]

#CONJUROS
fuego = rpg_conjuro.Conjuro("Llama Ardiente", "DAÑO", 24, 5)

#EJECUCION
player = crear_personaje()
player.inventario_objetos.append(pocion_curacion)
player.inventario_objetos.append(pocion_curacion)
player.inventario_objetos.append(pocion_magia)
player.inventario_objetos.append(bomba_incendiaria)
player.inventario_armas.append(escalibur)
player.inventario_conjuros.append(fuego)
print(player)
#print(arma_jugador)


enemigo = random.choice(enemigos)
print(f"Ha aparecido un {enemigo.nombre_jugador}")
enCombate = True
while(player.vida_actual > 0 and enemigo.vida_actual > 0 and enCombate):
    
    enCombate = combate_personaje(player, enemigo)
    if(enemigo.vida_actual > 0 and enCombate):
        combate_enemigo(enemigo, player)
        if(player.vida_actual <= 0):
            break




    



    

    


