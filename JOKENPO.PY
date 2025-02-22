#Desafio 45 Pedra papel e tesoura
from random import randint
from time import sleep

computador = randint(0, 2)
usuario = int(input('''Escolha sua jogada:
      [0] Pedra
      [1] Tesoura
      [2] Papel                '''
      ))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')


if computador == usuario:   
    print ("\033[;34mEmpate!! \033[m")

elif computador == 0 and usuario == 1:
    print ('\033[;31m COMPUTADOR VENCE!\033[m')

elif computador == 0 and usuario == 2:
    print ('\033[;32mVOCÊ VENCEU\033[m')

elif computador == 1 and usuario == 0:
    print ('\033[;32mVOCÊ VENCEU\033[m')

elif computador == 1 and usuario == 2:
    print ('\033[;31m COMPUTADOR VENCE!\033[m')

elif computador == 2 and usuario == 0:
    print('\033[;31m COMPUTADOR VENCE!\033[m')

elif computador == 2 and usuario == 1:
    print('\033[;32mVOCÊ VENCEU\033[m')