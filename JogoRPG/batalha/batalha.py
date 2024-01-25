import pygame
from os import system
from time import sleep
from random import randint

from exceptions import erros
from cores import cor
from songs import songs
from classes import classes

def recompensas(monstro_escolhido, jogador,monstro):
    bonus_xp = randint(1,2) 
    bonus_gold = randint(1,2)

    jogador.xp += monstro.monstruario[monstro_escolhido]['xp'] + bonus_xp
    jogador.gold += monstro.monstruario[monstro_escolhido]['gold'] + bonus_gold
    
    songs.musica(2)

    system('cls')
    print(f'{cor.cores[4]}{"VOCÊ VENCEU!" :^50}{cor.cores[0]}')   
    print(f'\n Você recebeu {monstro.monstruario[monstro_escolhido]["gold"] + bonus_gold} gold', end=' ')
    print(f'e {monstro.monstruario[monstro_escolhido]["xp"] + bonus_xp} XP!')
    
    input('\nENTER para continuar ')
    if jogador.xp >= jogador.xp_level_up:
        jogador.level_up()


def luta(monstro_escolhido, jogador, monstro):
    while monstro.monstruario[monstro_escolhido]['hp'] > 0 and jogador.hp > 0:        
        num_randomico_jogador = randint(0,2)
        num_randomico_monstro = randint(0,2)
        
        if jogador.velocidade > monstro.monstruario[monstro_escolhido]['velocidade']:
            monstro.monstruario[monstro_escolhido]['hp'] -= (jogador.ataque + num_randomico_jogador)
            print(f'Você causa {jogador.ataque + num_randomico_jogador} de dano')
            sleep(1)
            if monstro.monstruario[monstro_escolhido]['hp'] > 0:
                jogador.hp -= (monstro.monstruario[monstro_escolhido]['ataque'] + num_randomico_monstro)
                print(f'{" " * 30}{monstro_escolhido} ataca e causa {monstro.monstruario[monstro_escolhido]["ataque"] + num_randomico_monstro}')
                sleep(1)
        else:
            jogador.hp -= (monstro.monstruario[monstro_escolhido]['ataque'] + num_randomico_monstro)
            print(f'{" " * 30}{monstro_escolhido} ataca e causa {monstro.monstruario[monstro_escolhido]["ataque"] + num_randomico_monstro}')
            sleep(1)
            if jogador.hp > 0:
                monstro.monstruario[monstro_escolhido]['hp'] -= (jogador.ataque + num_randomico_jogador)
                print(f'Você causa {jogador.ataque + num_randomico_jogador} de dano')
                sleep(1)
                if monstro.monstruario[monstro_escolhido]['hp'] <= 0:
                    break
        
def batalha(indice_monstro):
    
    jogador = classes.jogador
    monstros = classes.monstros

    while True:
        try:
            monstro_escolhido = monstros.lista_monstros[indice_monstro - 1]
            
            songs.musica(1)
            
            system('cls')
            
            print(f'{"LUTA":^50}')
            print(f'\n{"Você":>15} {"VS":>10} {cor.cores[1]}{monstro_escolhido:>13}{cor.cores[0]}\n')
            
            luta(monstro_escolhido,jogador,monstros)
            
            if jogador.hp <= 0:
                while True:
                    try:
                        system('cls')
                        pygame.mixer.music.stop()
                        songs.efeito_sonoro(2)
                        
                        print(f'{cor.cores[1]}{"GAMEOVER":^50}{cor.cores[0]}')
                        escolha = int(input(f'\n[ 1 ] Tentar Novamente {" " * 10}[ 2 ] Desistir \n\nSua escolha: '))
                        
                        if escolha == 1:
                            pygame.quit()
                            jogador.resetar_jogo()
                        
                        elif escolha == 2:
                            print('Saindo...')
                            sleep(2)
                            exit()
                        
                        else:
                            erros.notificar_erro(ValueError)
                        
                    except ValueError:
                        erros.notificar_erro(ValueError)

            else:
                recompensas(monstro_escolhido, jogador, monstros)
                
                if monstro_escolhido == monstros.lista_monstros[-1]:
                    system('cls')
                    print('PARABENS, você zerou o game!')
                    input('ENTER para sair')
                    exit()

        except ValueError:
            erros.notificar_erro(ValueError)
        
        except Exception:
            erros.notificar_erro(Exception)
        
        else:
            monstros.resetar_hp()
            break
            
                