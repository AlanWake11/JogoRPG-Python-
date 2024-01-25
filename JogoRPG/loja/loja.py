from classes import classes
from os import system

from cores import cor
from songs import songs
from exceptions import erros


def weapons_shop(jogador):
    try:    
        system('cls')
        contador = 1
        print(f'     Espadas {"ATK":>20}{"Custo":>15}')
        print('═' * 60)
        
        for equipamento, valor in jogador.equipamentos.items():
            print(f' [{contador}] {equipamento:<18} {valor["ataque"]:^15} {valor["valor"]:>5} Golds', end=' ')
            print(f'{cor.cores[1]}X{cor.cores[0]}' if jogador.gold < valor["valor"] else f'{cor.cores[4]}✓{cor.cores[0]}')
            contador += 1
        
        indice = int(input('\nQual item comprar [999 para voltar]: '))

        if indice == 999:
            pass

        elif indice > len(jogador.equipamentos) or indice < 1:
            erros.notificar_erro(ValueError)
        
        else:
            equipamento_escolhido = jogador.lista_equipamentos[indice - 1]

            if equipamento_escolhido in jogador.inventario[0]:
                print(f'{cor.cores[2]}Você já tem esse equipamento!{cor.cores[0]}')
                input('ENTER para continuar\n')
            

            elif jogador.gold >= jogador.equipamentos[equipamento_escolhido]['valor']:
                jogador.gold -= jogador.equipamentos[equipamento_escolhido]['valor']
                jogador.inventario[0].append(equipamento_escolhido)
                
                songs.efeito_sonoro(0)
                print(f'\n{cor.cores[5]}Compra efetuada com sucesso!{cor.cores[0]}')
                
                input('\nENTER para continuar')
            
            else:
                system('cls')
                print(f'{cor.cores[2]}GOLD insuficiente...{cor.cores[0]}')
                input('\nENTER para voltar')

    
    except ValueError:
        erros.notificar_erro(ValueError)

def potion_shop(jogador):
    try:
        system('cls')
        contador = 1
        
        print(f'     Poções {cor.cores[1]}{"HP":>12}{cor.cores[0]} {"Custo":>15}')
        print('═' * 50)
        for k, v in jogador.pocoes.items():

            print(f'[{contador}] {k:<15} {v["hp"]:^7} {v["valor"]:>8} Golds', end=' ')
            print(f'{cor.cores[1]}X{cor.cores[0]}' if jogador.gold < v["valor"] else f'{cor.cores[4]}✓{cor.cores[0]}')
            contador += 1

        indice = int(input('\nQual item vai comprar [999 para voltar]: '))
        
        if indice == 999:
            pass

        elif indice > len(jogador.pocoes) or indice < 1:
            raise ValueError('Indice não encontrado')
        
        else:
            pocao_escolhido = jogador.lista_pocoes[indice - 1]

            if jogador.gold >= jogador.pocoes[pocao_escolhido]['valor']:
                jogador.gold -= jogador.pocoes[pocao_escolhido]['valor']
                jogador.inventario[1].append(pocao_escolhido)
                
                songs.efeito_sonoro(0)
                print(f'\n{cor.cores[5]}Compra efetuada com sucesso!{cor.cores[0]}')
                input('\nENTER para continuar')
            else:
                system('cls')
                print(f'{cor.cores[2]}GOLD insuficiente...{cor.cores[0]}')
                input('\nENTER para continuar')
    
        
        
    except ValueError:
        erros.notificar_erro(ValueError)


def shop():
    try:
        jogador = classes.jogador
        
        songs.musica(3)
        system('cls')
        
        print(f'{"Loja" :^50}')
        escolha = int(input(f'\n[ 1 ] Equipamentos {"[ 2 ] Poções":>25} \n\n[ 3 ] Voltar \n\nSua escolha: '))
        
        if escolha < 1 or escolha > 3:
            erros.notificar_erro(ValueError)


    except ValueError:
        erros.notificar_erro(ValueError)

    else:
        if escolha == 1:
            weapons_shop(jogador)   
        elif escolha == 2:
            potion_shop(jogador)
        else:
            pass
