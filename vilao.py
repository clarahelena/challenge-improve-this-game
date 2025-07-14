from personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, ataque, defesa):
        super().__init__(nome, idade, vida, ataque, defesa)


    def maldicao(self, personagem):
        personagem.vida - 1
        print(f'Maldição usada em {self.nome}! Dano por rodada.')

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
