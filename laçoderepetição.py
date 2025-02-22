#contagem regressiva
from time import sleep

print('Contagem regressiva para os fogos:')

for ci in range (10,0, -1):
    
    print (ci)
    sleep(1)


#todos os numeros pares de 1 a 50

print('todos os números pares são:')
for count in range (0, 50, 2):

    print(count)


#multiplos de 3 e intervalo de 1 a 500
for c in range (0, 500):
    if c % 3==0:
        print(c)
soma = 0 
soma = soma + c
print('A soma de todos os valores é {}'.format(soma))


#tabuada 
numero = int(input("Digite um número inteiro para ver sua tabuada:"))
for c in range(0, 11):
    mult = c*numero
    print("{} x {} = {}".format(numero, c, mult))


#
soma = 0
for c in range(1, 7):
    num = int(input("Digite um número:"))
    if num % 2 ==0:
        soma = soma + num
    else:
        num ==0
print ("A soma dos números pares digitados é {}".format(soma))


#termos de PA

termo = int(input("Digite o primero termo:"))
razão = int(input("Digite a razão:"))
decimo = termo + (10-1) * razão
for c in range(termo, decimo, razão):
    print(c)

#numeros primos 
num = int(input("Digite um número:"))
if num % num ==0 and num / 1 == num:
    print("É um número primo")
else:
    print("Não é um número primo")