class Animal():
    def __init__(self, nome, alimento, ecosistema):
        self.nome = nome
        self.alimento = alimento
        self.ecosistema = ecosistema
    
    def __str__(self) -> str:
        return f'{self.nome} {self.alimento} {self.ecosistema}'


class Pet(Animal):
    def __init__(self, nome, raça, alimento, ecosistema, idade, tipo):
        super().__init__(nome, alimento, ecosistema)
        self.idade = idade
        self.raça = raça
        self.tipo = tipo
    
    def __str__(self) -> str:
        return f'Ola eu sou um {self.tipo} meu nome é {self.nome} gosto muito de {self.alimento} e tenho {self.idade}'

gato = Pet(tipo='gato', nome='Linux', raça='branco', alimento='ração', idade='6 meses', ecosistema='Terrestre')
cachorro = Pet(tipo='cachorro', nome='Lola', raça='yorkshire', alimento='ração', idade='um ano e meio', ecosistema='Terrestre')

print(gato, cachorro)


class Mamimeferos(Animal):
    def __init__(self, nome, alimento, ecosistema, mamam, pelos):
        super().__init__(nome, alimento, ecosistema)
        self.mamam = mamam
        self.pelos = pelos
    def __str__(self):
        return f'{self.nome} {self.alimento} {self.ecosistema} {self.mamam} {self.pelos}'
ornitorrinco = Mamimeferos(nome = 'Perry', alimento='?', mamam='Sim, mama na infancia', ecosistema='Aquatico/Terrestre', pelos='verde')
print(ornitorrinco)

class Herbivoros(Animal):
    def __init__(self, nome, alimento, ecosistema, ingestao_adaptada, vegetariano):
        super().__init__(nome, alimento, ecosistema)
        self.ingestao_adaptada = ingestao_adaptada
        self.vegetariano = vegetariano
    
    def __str__(self):
        return f'{self.nome} {self.alimento} {self.ecosistema} {self.ingestao_adaptada} {self.vegetariano}'

grilo = Herbivoros(nome='junin', alimento='folha', ecosistema='terrestre', ingestao_adaptada='Sim', vegetariano='SIM')
tartaruga = Herbivoros(nome='tortoruga', alimento='folha', ecosistema='aquatico', ingestao_adaptada='Sim', vegetariano='SIM')

print(grilo, tartaruga)