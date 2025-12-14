import time as t
import random as ran

class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self._energia = 10

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        self._energia = valor 

        if valor > 50:
            self._energia = 0
        elif valor < 50:
            self._energia = 50
        else:
            self._energia = valor
    
    def atacar(self):
        self._energia -= 15
    
    def descansar(self):
        self._energia += 20
    
    def guerrear(self):
        if self._energia >= 50:
            print("Você está pronto para guerrear?")
            pergunta = input(">(Y/n)")
            
            if pergunta.lower() == "y":
                soldados = {
                    "joao": 20,
                    "carlos": 60,
                    "isaque": 200
                }
                
                # Hora da guerra
                t.sleep(0.9)
                print("Todos estão prontos?")
                t.sleep(1)
                print("Vamo a guerra")
                
                morte_ateatoria = ran.randint(1, 3)
                
                for nome in soldados:
                    soldados[nome] -= 40
                
                # Morte aleatória
                morto = ran.choice(list(soldados.keys()))
                print(f"💀 {morto} MORREU! HOUVE UMA BAIXA!")

                print("\nEstado final dos soldados:")
                for nome, vida in soldados.items():
                    print(f"{nome}: {max(vida, 0)} de vida")
        else:
            print("OK medroso 😑")

#Instancias
guerreiro = Guerreiro("Dany")
g = Guerreiro("Artemis")

g.atacar()      # -15 energia
print(g.energia)

g.descansar()   # +20 energia
print(g.energia)

g.atacar()
g.atacar()
g.atacar()
print(g.energia)

g.guerrear()