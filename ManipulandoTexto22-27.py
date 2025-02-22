

#Desafio 22 Nome
Nome =  str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print(Nome.upper())

print(Nome.lower())

print(len(Nome))

print('Seu primeiro nome tem {} letras'.format(Nome.find(' ')))

# Desafio 23 Leia um número e mostre na tela os digitos separados
numero = int(input('Digite um número de 0 a 9999:'))
n = str(numero)
print('Analizando este numero {}'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena:{}'.format(n[1]))
print('Milhar:{}'.format(n[0]))

#Desafio 24 Se começa ou não com a palavra santo
cidade = str(input('Diga o nome de uma cidade:'))
print (cidade[:5].upper() == 'SANTO')

#Desafio 25 Tem silva no nome?
nome = str(input('Digite seu nome:')).strip()
nome = nome.lower()
print(nome.find('silva'))

#Desafio 25 Tem silva no nome? (outro jeito)
nome = str(input('Digite seu nome:'))
nome = nome.lower()
print('{}'.format('silva' in nome))

#Desafio 26 Quantas vezes aparece a letra A
frase = str(input('Escreva uma frase:')).strip()
frase = frase.lower()
print('A letra A apareceu {} vezes'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')))

#Desafio 27 Ler o nome completo e separar
nome = str(input('Digite seu nome completo:')).strip()
print('o nome separado é {}'.format(nome.split()))