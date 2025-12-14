class Personagem:
    def __init__(self, nome):
        self.nome = nome 
        self._vida = 100

    @property
    def vida(self):
        return self._vida 
    
    @vida.setter
    def vida(self, valor):
        self._vida = valor

        # Se a vida ficar negativa 
        if valor < 0:
            self._vida = 0
        elif valor > 100:
            self._vida = 100
        else:
            self._vida = valor
    
    def tomar_dano(self, valor):
        self.vida -= valor

    def curar(self, cura):
        self.vida += cura 
    
p = Personagem("Dany")

p.tomar_dano(30)
print(p.vida)  # 70

p.curar(50)
print(p.vida)  # 100

p.tomar_dano(200)
print(p.vida)  # 0
        
