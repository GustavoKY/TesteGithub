from random import randint
from time import sleep

vida_jogador = 100
vida_inimigo = 100
velocidade_jogador = randint(20, 50)
velocidade_inimigo = randint(20, 50)
turno_jogador = 0
turno_inimigo = 0

while vida_jogador > 0 and vida_inimigo > 0:
    turno_jogador += velocidade_jogador
    turno_inimigo += velocidade_inimigo
    if turno_jogador >= 100:
        ataque_jogador = randint(0, 100)
        print('Jogador atacou Inimigo')
        vida_inimigo -= ataque_jogador
        print(f'Inimigo perdeu {ataque_jogador} pontos de vida')
        print(f'HP Inimigo: {vida_inimigo}')
        if vida_inimigo <= 0:
            break
        turno_jogador = 0
        sleep(1.0)
    if turno_inimigo >= 100:
        ataque_inimigo = randint(0, 100)
        print('Inimigo atacou Jogador')
        vida_jogador -= ataque_inimigo
        print(f'Jogador perdeu {ataque_inimigo} pontos de vida')
        print(f'HP Jogador: {vida_jogador}')
        if vida_jogador <= 0:
            break
        turno_inimigo = 0
        sleep(1.0)
if vida_jogador > 0:
    if vida_jogador < 40:
        print('O jogador venceu, mas ficou muito machucado')
    elif vida_jogador <= 80:
        print('O jogador venceu, mas ficou levemente machucado')
    else:
        print('O jogador venceu facilmente')
if vida_inimigo > 0:
    print('O inimigo venceu')
