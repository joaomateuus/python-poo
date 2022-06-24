class Animal():
    def __init__(self, nome, patas, alimento, ecosistema):
        self.nome = nome
        self.patas = patas
        self.alimento = alimento
        self.ecosistema = ecosistema
    
    def __str__(self) -> str:
        return f'{self.nome} {self.patas} {self.alimento} {self.ecosistema}'


class Pet(Animal):
    def __init__(self, nome, raça, patas, alimento, ecosistema, idade, tipo):
        super().__init__(nome, patas, alimento, ecosistema)
        self.idade = idade
        self.raça = raça
        self.tipo = tipo
    
    def __str__(self) -> str:
        return f'Ola eu sou um {self.tipo} meu nome é {self.nome} eu tenho {self.patas} patas gosto muito de {self.alimento} e tenho {self.idade}'

gato = Pet(tipo='gato', nome='Linux', raça='branco', patas=4, alimento='ração', idade='6 meses', ecosistema='Terrestre')
cachorro = Pet(tipo='cachorro', nome='Lola', raça='yorkshire', patas=4, alimento='ração', idade='um ano e meio', ecosistema='Terrestre')

print(gato)
print(cachorro)

class Invertebrados(Animal):
    def __init__(self, nome, alimento, ecosistema, patas, coluna):
        super().__init__(nome, alimento, ecosistema, patas)
        self.coluna = coluna
    def __str__(self):
        return f'{self.nome} {self.patas} {self.alimento} {self.ecosistema} {self.coluna}'
minhoca = Invertebrados(nome='minhoco', patas=0,  alimento='residuos', ecosistema='terrestre', coluna='nao possui')

print(minhoca)
