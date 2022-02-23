from Ficha import *

class Tablero:
#Defina aquí los atributos de Tablero
    casillas = 25 #Número total de casillas del tablero
    turno = 1 #Turno dependiendo del jugador
    posicion1 = 0 #Atributo donde guardar la posición del jugador
    posicion2 = 0
    posicion3 = 0
    posicion4 = 0



    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno


    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos

    def __init__(self):
        self.jugador1 = Ficha(input("Digite el color: "))
        self.jugador2 = Ficha(input("Digite el color: "))
        self.jugador3 = Ficha(input("Digite el color: "))
        self.jugador4 = Ficha(input("Digite el color: "))
        return

    def juego(self):
        while True:
            if self.turno == 1: #El numero del turno va de acorde al numero del jugador
                ficha1 = self.jugador1.getColor()
                print(input(f"\nLa ficha {ficha1}, digite enter para lanzar el dado: "))
                self.posicion1 += self.jugador1.avanzar() #Sumar la posición anterior y la nueva una vez se lanzan los dados
                self.turno += 1 #Se incrementa el turno para darle paso al otro jugador
                print(f"La ficha {ficha1} esta en la casilla: " + str(self.posicion1))
                if self.posicion1 >= self.casillas: #Verifica si llego o supero el total de casillas, para ser el ganador
                    #ficha1 = self.jugador1.getColor()
                    print(f"\nGanó la ficha color {ficha1}")
                    break
            if self.turno == 2:
                ficha2 = self.jugador2.getColor()
                print(input(f"\nLa ficha {ficha2}, digite enter para lanzar el dado: "))
                self.posicion2 += self.jugador2.avanzar()
                self.turno += 1
                print(f"La ficha {ficha2} esta en la casilla: " + str(self.posicion2))
                if self.posicion2 >= self.casillas:
                    ficha2 = self.jugador2.getColor()
                    print(f"\nGanó la ficha color {ficha2}")
                    break
            if self.turno == 3:
                ficha3 = self.jugador3.getColor()
                print(input(f"\nLa ficha {ficha3}, digite enter para lanzar el dado: "))
                self.posicion3 += self.jugador3.avanzar()
                self.turno += 1
                print(f"\nLa ficha {ficha3} esta en la casilla: " + str(self.posicion3))
                if self.posicion3 >= self.casillas:
                    ficha3 = self.jugador3.getColor()
                    print(f"Ganó la ficha color {ficha3}")
                    break
            if self.turno == 4:
                ficha4 = self.jugador4.getColor()
                print(input(f"\nLa ficha {ficha4}, digite enter para lanzar el dado: "))
                self.posicion4 += self.jugador4.avanzar()
                self.turno = 1
                print(f"La ficha {ficha4} esta en la casilla: " + str(self.posicion4))
                if self.posicion4 >= self.casillas:
                    ficha4 = self.jugador4.getColor()
                    print(f"\nGanó la ficha color {ficha4}")
                    break

        return ""

#Inicializador del juego

game = Tablero() #El juego esta diseñado para 4 participantes
game.juego() #llamada al juego con las fichas creadas
