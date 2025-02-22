#Desafio 36
valorcasa = float(input('Qual o valor da casa?'))
salario = float(input('Qual é o seu salário?'))
anos = int(input('Em quantos anos você irá pagar a casa?'))

anosemmeses = anos*12
prestação = valorcasa/anosemmeses

print('Você pagará a casa em {} meses'.format(anosemmeses))
print('Você pagará {} em cada prestação'.format(prestação))

if prestação <= salario*0.7:
    print('Parabéns, sua compra foi aprovada!')
else:
    print('A prestação excedeu 30% do seu salário, a compra não poderá ser efetuada.')


#Desafio 37


#Desafio 38
primeirovalor = float(input('Digite um número qualquer:'))
segundovalor = float(input('Digite outro número:'))

if primeirovalor > segundovalor:
    print('\033[33;42m O primeiro número é maior!\033[m')
elif segundovalor > primeirovalor: 
    print('\033[35mO segundo valor é maior!\033[m')
else:
    print('\033[38;45mOs dois valores são iguais!\033[m')


#Desafio 39
idade = int(input('Qual sua idade?'))

if idade < 18:
    qntfalta = 18 - idade 
    print('Calma! Você não precisa se alistar ainda, falta {} ano (s) para você se alistar'.format(qntfalta))
elif idade > 18:
    qntpassou = idade - 18
    print('Você precisa de alistar. Já se passou {} anos.'.format(qntpassou))
else:
    print('Já é hora de se alistar!')


#Desafio 40
primeiranota = float(input('Digite a primeira nota:'))
segundanota= float(input('Digite a segunda nota:'))
media = primeiranota + segundanota /2
if media < 5:
    print('Você foi reprovado!')
elif 7 > media >=5:
    print('Você está de recuperação!')
elif media >= 7:
    print('Você passou!')

#Desafio 41
ano = int(input('Digite seu ano de nascimento:'))
idade = 2024 - ano
if idade <= 9:
    print('Sua categoria é \033[33mMIRIM\033[m')
elif 14 >= idade <= 10:
    print('Sua categoria é \033[33mINFANTIL\033[m') 
elif 19 >= idade >= 15:
    print('Sua categoria é \033[33mJÚNIOR\033[m')
elif 25 >= idade >= 20:
    print('Sua categoria é \033[33mSÊNIOR\033[m')
elif idade > 26:
    print('Sua categoria é \033[33mMASTER\033[m')

#Desafio 42
v1 = float(input('Digite o valor da primeira reta:'))
v2 = float(input('Digite o valor da segunda reta:'))
v3 = float(input('Digite o valor da terceira reta:'))
if v1+v2 < v3 or v1+v3 < v2 or v3+v2 < v1:
    print('Será possível formar um triângulo', end='')
    if v1 == v2 == v3:
        print(', será um triângulo equilátero.')
    elif v1 == v2 != v3:
        print(', será um triângulo isósceles.')
    else:
        print(', será um triângulo escaleno.')
else:
    print('Não será possível formar um triângulo')

#Desafio 43 Cálculo de IMC
altura = float(input('Qual sua altura?'))
peso = float(input('Qual seu peso?'))
imc = altura/peso

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal.')
elif 26 <= imc <= 30:
    print('Você está no sobrepeso.')
elif 31 <= imc <= 40:
    print('Você está na obesidade.')
elif imc > 41:
    print('Você está na obesidade mórbida.')
print('Seu IMC é {}'.format(imc))

#Desafio 44
preço = float(input('Qual foi o preço das compras?'))
print(''''Escolha uma opção de pagamento
              [1]Dinheiro/Cheque
              [2]Cartão á vista
              [3]Parcelamento 2x no cartão
              [4]Parcelamento 3x ou mais no cartão ''')
opção = int(input('Qual será a opção?'))
if opção == 1:
    np = preço - (preço * 10/100)
    print('O valor que deverá ser pago é {}'.format(np))
if opção == 2:
    np = preço - (preço * 5/100)
    print('O valor que deve ser pago é {}'.format(np))
if opção == 3:
    print('O valor que deve ser pago é {}'.format(preço))
if opção == 4:
    np = preço + (preço * 0.2)
    print('O valor que dever ser pago é {}'.format(np))


