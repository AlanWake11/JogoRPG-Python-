from os import system

from cores import cor
from songs import songs

def notificar_erro(erro):
    system('cls')
    if erro == ValueError:
        print(f'{cor.cores[1]}Erro: Digite um valor válido{cor.cores[0]}')
    
    else:
        print(erro)
        
    songs.efeito_sonoro(3)
    input('\nENTER para continuar')