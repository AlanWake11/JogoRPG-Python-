import pygame

from exceptions import erros

def musica(indice):
    caminho = [
        'songs\lista_musicas\Overworld.mp3',                               
        'songs\lista_musicas\Forest Combat.mp3',                            
        'songs\lista_musicas\Final Fantasy VII - Victory Fanfare.mp3',
        'songs\lista_musicas\Going Shopping in Seaside Town - Super Mario RPG ).mp3'
    ]
    try:    
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(caminho[indice])
        pygame.mixer.music.play(loops=-1)
    
    except:
        erros.notificar_erro(ValueError)

def efeito_sonoro(indice):
    caminho = [
        'songs\lista_efeitos_sonoros\Mario Coin Sound - Sound Effect (HD).mp3',
        'songs\lista_efeitos_sonoros\Heal.mp3',
        'songs\lista_efeitos_sonoros\Game Over - The Legend of Zelda_ Ocarina of Time.mp3',
        'songs\lista_efeitos_sonoros\Som de erro do Windows - Efeitos Sonoros HD.mp3'
    ]
    try:
        som = pygame.mixer.Sound(caminho[indice])  
        som.set_volume(0.4)
        som.play()
        

    except Exception as e:
        erros.notificar_erro(e)
        