from random import  randint
from time import sleep
def titulo():
    sleep(1)
    print('Jogo de adivinhação contra a maquina')
    print()
    sleep(1)
    print('Carregando..')
    sleep(1)
try:
 nome_jogador   = str(input('Escolha o nome do jogador: '))
 nome_maquina   = str(input('Escolha o nome da maquina: '))
 numero_chances = int(input('Escohla o número de chances: '))
 chances = numero_chances
except ValueError:
   print('Opção invalida! Tente novamente!')
def jogo(chances):
    nome_maquiana = randint(0, 21)
    while True:
        print()
        print('O número é entre 0 a 20! Tente acerta-lo! Você tem exatamente {} tentativas.'.format(numero_chances))
        num = int(input('Escolha o número: '))
        if num != nome_maquiana:
            print()
            print()
            print('Número diferente do escolhido! Tente novamente')
            print()
            print()
            chances -= 1
            print('Tentativas restantes ', chances)
            if chances == 0:
                print('Game over! {} Venceu!'.format(nome_maquina))
                break
        elif num == nome_maquiana:
            print('Acertou! Parabens, {}!'.format(nome_jogador))
            break
#Jogo
titulo()
jogo(chances)