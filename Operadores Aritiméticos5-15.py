# Desafio 005 antecessor e sucessor
#n = int(input('Digite um número: '))
#a = n - 1
#s = n + 1
#print ('Analisando o valor {}, o antecessor é {} e o seu sucessor {}'.format(n, a, s))

#Desafio 006 Dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))
d = n + n
t = n + 2*n
r = n**(1/2)
print ('Analisando o valor {} seu dobro é {}, seu triplo seria {} e sua raiz quadrada {}'.format(n, d, t, r))

#Desafio 007 Média Aritmética
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
ma = (n1 + n2) /2
print ('A média do aluno é {}'.format(ma))

#Desafio 008 Metros em CM e MM
n = float(input('Escreva um valor em metros: '))
centimetros = n * 100
milimetros = n * 1000
print('O valor em centimetros seria {} e o valor em milimetros seria {}'.format(centimetros, milimetros))

#Desafio 009 Tabuada
n = int(input('Digite um número inteiro:'))
print ('{} x {} = {}'.format(n, 1, n*1))
print ('{} x {} = {}'.format(n, 2, n*2))
print ('{} x {} = {}'.format(n, 3, n*3))
print ('{} x {} = {}'.format(n, 3, n*4))
print ('{} x {} = {}'.format(n, 5, n*5))
print ('{} x {} = {}'.format(n, 6, n*6))
print ('{} x {} = {}'.format(n, 7, n*7))
print ('{} x {} = {}'.format(n, 8, n*8))
print ('{} x {} = {}'.format(n, 9, n*9))
print ('{} x {} = {}'.format(n, 10, n*10))

#Desafio 010 Conversor de moedas
n = float(input('Quanto você tem na carteira?'))
print (' {} reais = {} doláres.'.format(n, n*5,25 ))


#Desafio 011 Pintando a parede
largura = float(input('Qual é a largura da parede?'))
comprimento = float(input('Qual é o comprimento da parede?'))
área = largura * comprimento
quantidade = área/2
print ('A quantidade de tinta necessária para pintar a parede é {}'.format(quantidade))

#Desafio 012 Calculando descontos
preço = float(input('Quanto custa o produto?'))
desconto = preço*0.05
novopreço = preço - desconto
print ('O novo preço do produto com 5% de desconto é {}'.format(novopreço))

#Desafio 013 Reajuste Salarial ERRO*********************
#salario = float(input('Qual o salario?'))
#novo = salario + (salario*0,15)
#print ('O novo salario com reajuste salarial será {}'.format( novo ))

#Desafio 014 Celsius em Fahrenheit
celsius = float(input('Qual a temperatuera em Celsius?'))
fahrenheit = ((9*celsius)/5)+32
print ('A temperatura de {} celsius em farenheit é {}'.format(celsius, fahrenheit))

#Desafio 015 Aluguel de carros
km = float(input('Quantos km foram percorridos?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
total = (dias * 60) + (km * 0,15) 
print ('O total a se pagar será {}'.format(total))