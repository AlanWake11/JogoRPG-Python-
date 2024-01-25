from os import system
import pygame

from exceptions import erros
from cores import cor
from classes import classes
from songs import songs
from batalha import batalha
from loja import loja


pygame.init()

jogador = classes.jogador
monstros = classes.monstros 

while True:
    try:
        system('cls')
        songs.musica(0)
        
        jogador.monstrar_informacoes()   
    
        modo_de_jogo = int(input('\n[ 1 ] Monstros \n[ 2 ] Equipamentos \n[ 3 ] Poções \n[ 4 ] Loja \n\nSua escolha: '))
        if modo_de_jogo < 1 or modo_de_jogo > 4:
            erros.notificar_erro(ValueError)
            
    except ValueError:
        erros.notificar_erro(ValueError)

    else:
        if modo_de_jogo == 1:
            while True:
                try:
                    system('cls')
                    monstros.mostrar_informacoes()
                    
                    monster_choice = int(input("\nQual irá lutar [999 para voltar]: "))
                        
                    if monster_choice == 999:
                        break
                    
                    elif monster_choice <= 0 or monster_choice > len(monstros.monstruario):
                        erros.notificar_erro(ValueError)
                    
                    else:
                        batalha.batalha(monster_choice)
                        break

                
                except ValueError:
                    erros.notificar_erro(ValueError)
                    
        
        elif modo_de_jogo == 2:
            jogador.inventario_equipamento()
        
        elif modo_de_jogo == 3:
            while True:
                try:
                    system('cls')
                    contador1 = contador2 = contador3 = 0
                    
                    if len(jogador.inventario[1]) > 0:
                        for p in jogador.inventario[1]:
                            if p == 'Poção':
                                contador1 += 1
                            elif p == 'Super Poção':
                                contador2 += 1
                            else:
                                contador3 += 1
                        
                        print(f'Poções {"Quantidade":>27}')
                        print('═' * 40)
                        print(f'[ 1 ] Poção {contador1:>17}')
                        print(f'[ 2 ] Super Poção {contador2:>11}')
                        print(f'[ 3 ] Poção Maxima {contador3:>10}')
                        
                        indice_pocao = int(input('\nPoção que irá usar [999 para voltar]: '))
                        
                        if indice_pocao == 999:
                            break
                        elif indice_pocao < 1 or indice_pocao > 3:
                            erros.notificar_erro(ValueError) 
                        else:    
                            jogador.usar_pocao(indice_pocao)
                            break
                            
                            
                    else:
                        print(f'{cor.cores[2]}Não há poções no seu inventario...{cor.cores[0]}')
                        input('\nENTER para voltar')
                        break
                                    
            
                except ValueError:
                    erros.notificar_erro(ValueError)

            
        else:
            loja.shop()
        
