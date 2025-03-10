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



#Palíndromos
#frase = str(input("Digite uma frase:")).strip() .upper()
#palavras = frase.split
#junto= ''.join(palavras)
#inverso = ''

#for letra in range (len[junto] -1, -1, -1):
#    inverso += junto[letra]
#if inverso == junto:
#    print("Temos um palíndromo")
#else:
#    print("Não temos um palíndromo")
#

#data de nascimento 7 pessoas
data = int(input("Qual o ano que você nasceu?"))
ano = 2025-data
for data in range (0,7):
    if ano >18:
     data = int(input("Qual o ano que você nasceu?"))
     print("Você atingiu a maioridade")
    else:
     print("Você ainda não atingiu a maioridade")




#peso de 5 pessoas
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {} pessoa". format(p)))
    if peso ==1:
        maior =p
        menor =p
    else:
        if peso > maior:

            maior = peso

        if peso < menor:

            menor = peso
print("O maior peso lido foi de {}".format(maior))
print("O menor peso lido foi de {}".format(menor))

#
somaidade = 0
mediaidade = 0
maioridadehomem = 0 
nomevelho = 0
totalmulher20 = 0 
for c in range(0, 4):
    nome = str(input("Digite seu nome:"))
    idade = int(input("Digite sua idade:"))
    sexo = str(input("Qual seu sexo?"))
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1

mediaidade = somaidade/4
print("A média da idade do grupo é de {}".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} com menor de 20 anos.".format(totalmulher20))
