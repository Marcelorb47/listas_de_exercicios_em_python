# 1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Alo Mundo')
--------------------------------------------------------------------
# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num = int(input('Digite um numero: '))
print(f'O número digitado foi {num}')
---------------------------------------------------------------
# Faça um Programa que peça dois números e imprima a soma.
num = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
print(f'A soma dos números digitados é {num + num2}')
------------------------------------------------------------
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input(f'Digite a nota 1 '))
nota2 = float(input(f'Digite a nota 1 '))
nota3 = float(input(f'Digite a nota 1 '))
nota4 = float(input(f'Digite a nota 1 '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média das notas é {media}')
--------------------------------------------------------------

# 5 Faça um Programa que converta metros para centímetros.

metros = float(input('Digite a medida em metros a ser convertida '))

centi = metros * 100

print(f'A medida em centimetros é {centi}')

--------------------------------------------------------------

# 6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input('Digite o raio do circulo '))

area = 3.14 * (raio**2)
print(f'A área do circulo é {area}')

------------------------------------------------------------

# 7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input('Digite o valor do lado do quadrado '))

area = lado **2

print(f'O valor da área do quadrado é {area} e o dobro {area*2}')
----------------------------------------------------------------
# 8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.

valor_hora = float(input('Digite o valor que você ganha por hora '))
hora_trabalhada = float(input('Digite quantas hora você trabalhou no mês '))

salario = valor_hora * hora_trabalhada
print(f'O seu salario esse mês é {salario}')

----------------------------------------------------------------

# 9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#
#     C = 5 * ((F-32) / 9).
fahrenheit = float(input('Digite o grau em Fahrenheit '))

celsius = 5 *((fahrenheit - 32)/ 9)
print(f'O grau em Celsius é {celsius}')

----------------------------------------------------------------

# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input('Digite primeiro número inteiro: '))
num2 = int(input('Digite segundo número inteiro: '))
num3 = float(input('Digite o número real: '))

produto_metade = (num1 * 2) + (num2 / 2)
triplo = (num1 * 3) + num3
elevado = num3 ** 3

print(f'o produto do dobro do primeiro com metade do segundo {produto_metade}')
print(f'A soma do triplo do primeiro com o terceiro é {triplo} ')
print(f'o terceiro elevado ao cubo {elevado}')

------------------------------------------------------------------------

# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite a sua altura: '))

peso_ideal = (72.7 * altura) - 58

print(f'Seu peso ideal é {peso_ideal}kg')

----------------------------------------------------------------------------

# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite a sua altura '))
sexo = input('Qual o seu sexo biológico? m/f ')

if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso_ideal}')
elif sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O seu peso ideal é {peso_ideal}')
else:
    print('Sexo não reconhecido')

# 66.31700000000001

-----------------------------------------------------------------------------

# 14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
# regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso
# (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Qual foi o peso do pescado hoje: '))

if peso > 50.00:
    excesso = peso - 50.00
    multa = excesso * 4.00
    print(f'O execesso de peso é {excesso} e a multa é R${multa} reais ')
else:
    print('Não houve exesso de peso')

--------------------------------------------------------------------------------------

# 15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#    salário bruto.
#    quanto pagou ao INSS.
#    quanto pagou ao sindicato.
#    o salário líquido.
#    calcule os descontos e o salário líquido, conforme a tabela abaixo:

ganho_por_hora = float(input('Digite quantos você ganha por hora: '))
horas_trabalhadas = float(input('Quantas horas vc trabalhou esse mês: '))

salario_bruto = ganho_por_hora * horas_trabalhadas
imposto_renda = (salario_bruto/100) * 11
inss = (salario_bruto / 100) * 8
sindicato = (salario_bruto / 100) * 5
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f'+ Salário bruto: R${salario_bruto}')
print(f'- IR 11%: R${imposto_renda}')
print(f'- INSS (8%): R${inss}')
print(f'- Sindicato (5%): R${sindicato}')
print(f'Sálario Lquido: R${salario_liquido}')

-------------------------------------------------------------------------------

import math
# 16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros_quadrados = float(input('Digite o tamanho em metros quadrados da area a ser pintada: '))

cobertura = 18 * 3
latas = math.ceil(metros_quadrados / cobertura)
preco = latas * 80

print(f'Você ira precisar de {latas} com o preço total de {preco}')

--------------------------------------------------------------------------------

# 17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     A) comprar apenas latas de 18 litros;
#     b) comprar apenas galões de 3,6 litros;
#     c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
#     sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

metros_quadrados = float(input('Qual o tamanha da área a ser pintada em M²: '))

cobertura = metros_quadrados / 6

lata = (cobertura / 18)
galao = (cobertura / 3.6)
misto = lata / galao
pereco_lata = lata * 80.00
preco_galao = galao * 25.00
latas = 0


-----------------------------------------------------------------------------------
