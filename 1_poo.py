class Animal():
    def __init__(self, nome, patas, alimento, ecosistema ):
        self.nome = nome
        self.patas = patas
        self.alimento = alimento
        self.ecosistema = ecosistema
    
    def __str__(self) -> str:
        return f'{self.nome} {self.patas} {self.alimento} {self.ecosistema}'

cachorro = Animal(nome='Beto', patas=4, alimento='ração', ecosistema='terrestre')

print(cachorro)
