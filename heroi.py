from personagem import Personagem

class Heroi(Personagem):
    def __init__(self, nome, idade, vida, ataque, defesa):
        super().__init__(nome, idade, vida, ataque, defesa)

    
    def usar_pocao(self, incremento=4):
        self.ataque += incremento
        print(f'Poção usada, o ataque de {self.nome} foi buffado, dano atual do ataque: {self.ataque}')

    def __str__(self):
        return f'Heroi: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'