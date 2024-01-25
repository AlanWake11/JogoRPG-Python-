from os import system, listdir
from math import ceil

from cores import cor
from songs import songs
from exceptions import erros

class Jogador:
    def __init__(self, hp, max_hp, gold, xp, xp_level_up, velocidade, level, ataque, equipamento):
        self.hp = hp
        self.max_hp = max_hp
        self.gold = gold
        self.xp = xp
        self.xp_level_up = xp_level_up
        self.velocidade = velocidade
        self.level = level
        self.ataque = ataque
        self.equipamento = equipamento
        
        self.equipamentos = {
            'Espada de Madeira' : {
                'ataque' : 5,
                'valor' : 50
            },
            'Espada de Ferro' : {
                'ataque' : 10,
                'valor' : 150
            },
            'Espada de Diamente' : {
                'ataque' : 20,
                'valor' : 300 
            }
        }
        
        self.pocoes = {
            'Poção': {
                'hp' : 10,
                'valor' : 10
            },
            'Super Poção': {
                'hp' : 30,
                'valor' : 50
            },
            'Poção Maxima': {
                'hp' : self.max_hp,
                'valor' : 300
            }
        }

        self.inventario = [[],[]]
        self.lista_equipamentos = []
        self.lista_pocoes = []

        for k in self.equipamentos.keys():
            self.lista_equipamentos.append(k)

        for k in self.pocoes.keys():
            self.lista_pocoes.append(k)
    
    def level_up(self):
        system('cls')

        self.level += 1

        self.xp_level_up *= 2
        
        self.max_hp = self.max_hp + (self.max_hp * 10/100)
        self.max_hp = ceil(self.max_hp)
        self.pocoes['Poção Maxima']['hp'] = self.max_hp

        self.hp = self.max_hp

        self.ataque = self.ataque + (self.ataque * 10/100)
        self.ataque = ceil(self.ataque)

        self.velocidade += (self.velocidade * 10/100)
        self.velocidade = ceil(self.velocidade)

        
        print(f'{cor.cores[4]}{"LEVEL UP!!!":^50}{cor.cores[0]}')
        print(f'\nHP: {self.max_hp}')
        print(f'Ataque: {self.ataque}')

        input()
    
    def inventario_equipamento(self):
        while True:
            try:
                system('cls')
                
                if len(self.inventario[0]) > 0:
                    print(f'Equipando: {self.equipamento}' if self.equipamento != '' else 'Equipando: Vazio')
                    print()
                    
                    print('═' * 40)
                    print(f'     Espadas {"ATK":>20}')
                    print('═' * 40)
                    for i, v in enumerate(self.inventario[0]):
                    
                        print(f'[{i+1}] {v:<20} {self.equipamentos[v]['ataque']:>7}')
                    
                    self.indice = int(input('\n\nQual vai equipar [999 para voltar]: '))

                    if self.indice == 999:
                        break
                    
                    self.indice -= 1
                    
                    if self.indice > len(self.inventario[0]) or self.indice < 0:
                        erros.notificar_erro(ValueError)
                    
                    elif self.inventario[0][self.indice] == self.equipamento:
                        system('cls')
                        print(f'{cor.cores[2]}Você já está equipado à esse equipamento{cor.cores[0]}')
                        input('\nENTER para voltar\n')
                    
                    elif self.lista_equipamentos[self.indice] != self.equipamento:
                        if self.equipamento == '':
                            self.equipamento = self.inventario[0][self.indice]
                            self.ataque += self.equipamentos[self.equipamento]['ataque']
                        else:
                            self.ataque -= self.equipamentos[self.equipamento]['ataque']
                            
                            self.equipamento = self.inventario[0][self.indice]                  
                            self.ataque += self.equipamentos[self.equipamento]['ataque']

                        print(f'\nAtaque Atual: {self.ataque}')
                        input('\nENTER para continuar\n')
                        break

                else:
                    print(f'{cor.cores[2]}Você não tem nenhum equipamento no momento...{cor.cores[0]}')
                    input('\nENTER para voltar\n')
                    break
                        
                    
            except ValueError:
                erros.notificar_erro(ValueError)

    def usar_pocao(self, indice_pocao):
        self.inventario[1].remove(self.lista_pocoes[indice_pocao - 1])
        pocao_escolhido = self.lista_pocoes[indice_pocao - 1]
        self.hp += self.pocoes[pocao_escolhido]['hp']
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        system('cls')
        songs.efeito_sonoro(1)
        print(f'\nUsou {pocao_escolhido}!')
        print(f'{cor.cores[4]}Recuperou {self.pocoes[pocao_escolhido]["hp"]} {cor.cores[0]}')
        input('\nENTER para continuar')
                
    def monstrar_informacoes(self):
        print('═' * 40)
        print(f'{cor.cores[1]}HP: {cor.cores[0]}{self.hp}')
        print(f'{cor.cores[2]}GOLD: {cor.cores[0]}{self.gold}')
        print(f'{cor.cores[3]}XP: {cor.cores[0]}{self.xp} | Faltam {self.xp_level_up - self.xp}')
        print(f'{cor.cores[4]}Level: {cor.cores[0]}{self.level}')
        print('═' * 40)
    
    def resetar_jogo(self):
        arquivos_na_pasta = listdir()

        executaveis = [arquivo for arquivo in arquivos_na_pasta if arquivo.lower().endswith('.exe')]

        if executaveis:
            arquivo_a_executar = executaveis[0]
            system(arquivo_a_executar)

        else:
            print("Nenhum arquivo .exe encontrado na pasta.")
            input()

class Monstros:
    def __init__(self, hp, hp_inicial, ataque, velocidade, gold, xp):
        self.monstruario = {
            'Gosma': {
                hp : 5,
                hp_inicial : 5,
                ataque : 1,
                velocidade : 1,
                gold : 1,
                xp : 1
                
            },
            'Zombi': {
                hp : 15,
                hp_inicial : 15,
                ataque : 3,
                velocidade : 5,
                gold : 5,
                xp : 5
            },
            'Orc' : {
                hp : 25,
                hp_inicial : 25,
                ataque :6,
                velocidade : 10,
                gold : 10,
                xp : 10
            },
            'Golem' : {
                hp : 75,
                hp_inicial : 75,
                ataque : 15,
                velocidade : 7,
                gold : 25,
                xp :20
            },

            'Dragão' : {
                hp : 200,
                hp_inicial : 200,
                ataque : 50,
                velocidade : 30,
                gold : 100,
                xp : 100
            }
            
        }

        self.lista_monstros = []
        for k in self.monstruario.keys():
            self.lista_monstros.append(k)   

    def resetar_hp(self):
        for monstro, atributos in self.monstruario.items():
            atributos['hp'] = atributos['hp_inicial']
    
    def mostrar_informacoes(self):
        contador = 0
        print(f'   Monstros {cor.cores[1]}{"HP":>8}{cor.cores[0]}{"ATK":>8}{cor.cores[2]}{"GOLD":>8}{cor.cores[0]}{cor.cores[3]}{"XP":>8}{cor.cores[0]}')
        print('═' * 50)
        for k,v in self.monstruario.items():
            contador += 1
            
            print(f'[{contador}] {k:<8}', end=' ')
            print(f'{v["hp"]:>6}', end=' ')
            print(f'{v["ataque"]:>7}', end=' ')
            print(f'{v["gold"]:>7}', end=' ')
            print(f'{v["xp"]:>7}')
        
            
             
jogador = Jogador(hp = 30, gold = 0, xp = 0, max_hp = 30, xp_level_up = 10, velocidade = 1, level = 1, ataque = 1, equipamento = '')
monstros = Monstros('hp', 'hp_inicial', 'ataque', 'velocidade', 'gold', 'xp')
