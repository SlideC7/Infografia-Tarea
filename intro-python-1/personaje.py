import random
import time

class Personaje:
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad > 0

class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, habilidades):
        super().__init__(nombre, vitalidad)
        self.habilidades = habilidades
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def listar_habilidades(self):
        for h in self.habilidades:
            print(f"Puedo {h}")

 # 2. Agregar lógica de contraataque del jugador.
    def contraatacar(self, enemigo):
        print(f"{self.nombre} contraatacando a {enemigo.nombre}")
    
 # 1. Agregar logica de daño aleatorio al enemigo.
 # 3. Agregar posibilidad de daño crítico en contra ataque del jugador.
        if random.random() < 0.5:
            danio_critico = self.vitalidad // 2
            print(f"¡Golpe crítico! {enemigo.nombre} recibe {danio_critico} de daño")
            enemigo.recibir_daño(danio_critico)
        else:
            enemigo.recibir_daño(20)
            print(f"{enemigo.nombre} recibe 20 de daño")
            print(f"vitalidad {enemigo.nombre}: {enemigo.vitalidad}")


class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, dano_min, dano_max, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.ataque_esp = ataque_esp
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def atacar_jugador(self, jugador):
        dano = random.randint(self.dano_min, self.dano_max)
        print(f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {dano}")
        jugador.recibir_daño(dano)
        if random.random() < 0.1:
            print(f"{jugador.nombre} contraataca...")
            jugador.contraatacar(self)

jugador = Jugador("Pikachu", 100, ["atacar", "volar", "esquivar"])
jugador.listar_habilidades()
jugador.saludo()

enemigo = Enemigo("Raichu", 100, 10, 20, 40)


while jugador.esta_vivo():
    enemigo.atacar_jugador(jugador)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    time.sleep(2)

print(f"El jugador {jugador.nombre} ha muerto")
# EJERCICIO:
# Modificar este programa para agregar las siguientes caracteristicas:
# 1. Agregar logica de daño aleatorio al enemigo.
# 2. Agregar lógica de contraataque del jugador.
# 3. Agregar posibilidad de daño crítico en contra ataque del jugador.

