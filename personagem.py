
class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida, ataque, defesa):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa


    def cura(self, incremento= 3):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} após cura: {self.vida}')


    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    
    def atacar(self, personagem):
        """
        Ataca outro personagem reduzindo sua vida.
        """
        personagem.vida -= self.ataque - personagem.defesa
        print(f'{self.nome} atacou {personagem.nome}!')
        print(f'Vida atual de {personagem.nome}: {personagem.vida}')


    def dialogar(self, acao):
        classe = self.__class__.__name__
        if classe == 'Vilao':
            if acao == 'ataque':
                print(f'Todo mundo morre, alguns só precisam de uma ajudinha!')
            elif acao == 'defesa':
                print(f'Inquebravel erguido.')
            elif acao == 'morte':
                print(f'Então é assim que se sente o fim?...')
            elif acao == 'cura':
                print(f'Cada vida, uma joia rara.')
            else:
                print('No massacre eu floresço, como uma flor no amanhecer...')
        elif classe == 'Heroi':
            if acao == 'ataque':
                print(f'Sucumba ao seu fim!')
            elif acao == 'defesa':
                print(f'Os céus me protegem.')
            elif acao == 'morte':
                print(f'Eu não sou um rei, eu não sou um Deus, eu sou pior...')
            elif acao == 'cura':
                print(f'A brisa traz o alívio.')
            else:
                print('O ciclo da vida e da morte continua. Nós viveremos, eles morrerão...')
        else:
            print('Um coração gelado, apenas precisa de um sorriso quente.')


    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'
