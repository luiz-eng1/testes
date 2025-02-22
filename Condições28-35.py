#Desafio 28 Jogo da Adivinhação
from random import randint
escolha = randint(0, 5)
usuario = int(input('Escolha um número de 0 a 5:'))
if usuario == escolha:
    print('Parabéns!! Você acertou!')
else:
    print('Ahh não! Você errou, tente novamente.')
print('O número escolhido foi {}'.format(escolha))

#Desafio 29 Radar Eletrônico
velocidade = float(input('Qual a velocidade do carro?'))
multa = (velocidade-80) * 7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade.')
    print('Você pagará uma multa de R${}'.format(multa))
    
else:
    print('Você está dentro do limite de velocidade.')


#Desafio 30 Par ou ímpar
numero = float(input('Digite um número:'))
resultado = numero % 2
if resultado == 0:
    print('Esse número é par!')
else:
    print('Esse número é ímpar!')


#Desafio 31 Viagem
distancia = float(input('Qual a distância da viagem??'))
if distancia < 200:
    preço = distancia * 0.50
 
else:
    preço = distancia * 0.45

print ('O preço da viagem será R$ {} '.format(preço))


#Desafio 32  Ano bissexto
ano = float(input('Me fale algum ano e falarei se é bissexto ou nãooo!'))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto.')


#Desafio 33
a = float(input('Digite o primeiro número:'))
b = float(input('Digite o segundo número:'))
c = float(input('Digite o terceiro número:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = c
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = c
print ('O menor valor digitado foi {}.'.format(menor))
print ('O maior valor digitado foi {}.'.format(maior))


#Desafio 34 Salário
salário = float(input('Qual é o salário?'))
if salário >= 1250:
    salário = (1250 * 0.10) + 1250
else: 
    salário = (1250 * 0.15) + 1250
print ('O novo salário com ajuste será {}'.format(salário))


#Desafio 35 Pode ou não formar um triângulo?
v1 = float(input('\033[32;44m Digite o valor da primeira reta:\033[m'))
v2 = float(input('Digite o valor da segunda reta:'))
v3 = float(input('Digite o valor da terceira reta:'))
if v1+v2 < v3 or v1+v3 < v2 or v2+v3 < v1:
    print ('Será possível formar um triângulo:')
else:
    print('Não será possível formar um triângulo.')