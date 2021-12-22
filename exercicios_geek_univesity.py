"""
Faça um programa qeu receba dois numeros e mostre qual o maior deles
"""

num1 = int(input("Digite o primeiro Número: " ))
num2 = int(input("Digite o segundo Númro: "))

if num1 > num2:
    print("O primeirto número é maior que o segundo numero")
else:
    print("O segundo número  é maior que o primeiro número")

--------------------------------------------------------------
"""Exercicio 2"""
"""Receba um numero e calcule a raiz quadrada do mesmo se for positivo, se for negativo exiba uma mensagem de erro"""
num = int(input("Digite um número "))

if num >= 0:
    raiz = num ** (1/2)
    print("A raiz do número é {}".format(raiz))
else:
    print("Número inválido")

---*---------------------------------------------------------
    """Exercicio 03"""
    num = int(input("Digite um número "))

if num > 0:
    raiz = num ** (1/2)
    print("A raiz é {}".format(raiz))
else:
    elevado = num ** 2
    print("O numero elevado ao quadrado é {}".format(elevado))

--------------------------------------------------------------

# Exercicio 4

num = int(input("Digite um número "))

if num > 0:
    quadrado = num ** 2
    raiz = num ** (1/2)
    print("O número {} ao quadra é {} e a raiz e {}".format(num, quadrado, raiz))
else:
    print("Digite um número positivo")
-------------------------------------------------------------

# Exercicio 5

num = int(input("Digite um número"))

if num % 2 == 0:
    print("O número {} é par".format(num))
else:
    print("O numero é impar")

---------------------------------------------------------------

# Exerício 6

num1 = int(input("Digite o primeiro número "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    diferenca = num1 - num2
    print("O numero {} é maior que o numero {}".format(num1, num2))
    print("Uma difrença de {}".format(diferenca))
else:
    diferenca2 = num2 - num1
    print("O numero {} é maior que o numero {}".format(num2, num1))
    print("Uma difrença de {} ".format(diferenca2))

---------------------------------------------------------------

# Exerício 7

num1 = int(input("Digite o primeiro número "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(" {} é maior que  {}".format(num1, num2))

elif num1 < num2:
    print("O {} é maior que{}".format(num2, num1))
else:
    print("Os números são iguais")

---------------------------------------------------------------

# Exerício 8

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
if nota1 > 0:
    if nota1 < 10:
        print("A primeira nota é valida")
    else:
        print("A primeira nota é invalida")
if nota2 > 0:
    if nota2 < 10:
        print("A segunda nota é valida")
    else:
        print("A segunda nota é invalida")


print("A média das notas é {}".format(media))

--------------------------------------------------------------

# Exercicio 9

salario = float(input("Digite o seu Sálario "))
emprestimo = float(input("Digite o seu empréstimo "))

por_cento = (20 * salario) / 100

if emprestimo >= por_cento:
    print("Emprestimo negado")
else:
    print("Empréstimo concedido")

--------------------------------------------------------------

# Exercicio 10

altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo: M ou F ").lower()

peso_homem = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7

if sexo == "m":
    print("O seu peso ideal é {}".format(peso_homem))
elif sexo == "f":
    print("O seu peso ideal é {}".format(peso_mulher))
else:
    print("Sexo invalido")

-------------------------------------------------------------

# Exercicio 11

altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo: M ou F ").lower()

peso_homem = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7

if sexo == "m":
    print("O seu peso ideal é {}".format(peso_homem))
elif sexo == "f":
    print("O seu peso ideal é {}".format(peso_mulher))
else:
    print("Sexo invalido")

-------------------------------------------------------------

import math

num = int(input("Digite um número"))

if num > 0:
    log = math.log(num)
    print("o Log de {} é {} ".format(num, log))
else:
    print("Número invalido")

------------------------------------------------------------

# Exercicio 13

prova1 = int(input("Digite a nota da P1 "))
prova2 = int(input("Digite a nota da P2 "))
prova3 = int(input("Digite a nota da P3 "))

p3 = prova3 * 2
media = (prova1 + prova2 + p3)/(1 + 1 + 3)

if media >= 60:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

------------------------------------------------------------

# Exercício 14

trabalho_laboratorio = float(input("Digite a nota do Trabalho de laboratório: "))
nota_avalicao_semestral = float(input("Digite a nota da avaliação semestral"))
nota_exame_final = float(input("Digite a nota do exame final "))

peso_laboratorio = trabalho_laboratorio * 2
peso_semestral = nota_avalicao_semestral * 3
peso_exame = nota_exame_final * 5
peso = 3 + 2 + 5
media = (peso_exame + peso_semestral + peso_exame)/peso

if 0 < media < 2.9:
    print(media)
    print("O aluno esta reprovado")
elif 3 < media < 4.9:
    print(media)
    print("O aluno esta de recuração")
else:
    print(media)
    print("O aluno esta aprovado")

--------------------------------------------------------------

# Exercício 15

num = int(input("Digite um número de 1 a 7 "))

domingo = 1
segunda = 2
terca = 3
quarta = 4
quinta = 5
sexta = 6
sabado = 7

if num == 1:
    print("Domingo")
elif num == 2:
    print("Segunda")
elif num == 3:
    print("Terça")
elif num == 4:
    print("Quarta")
elif num == 5:
    print("Quinta")
elif num == 6:
    print("Sexta")
elif num == 7:
    print("Sábado")
else:
    print("Numero invalido")

-------------------------------------------------------

# Exercicio 16
def mes(valor):
    mesdoano = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }
    return mesdoano.get(valor, "Não encontrei esse mês")


meses = int(input("Informe um numero referente ao meŝ"))
print(mes(meses))


--------------------------------------------------------

# Exercicio 17

base_maior = float(input("Digite o valor da base maior "))
base_menor = float(input("Digite o valor da base menor "))
altura = float(input("Digite o valor da altura "))

area = (base_menor + base_maior) * altura / 2

print(" A area é {}".format(area))

----------------------------------------------------------
# Exercício 18

operacao = input("Digite a operação desejada + - / * ")

if operacao == "+":
    num1 = int(input("Digite o primeiro numero "))
    num2 = int(input("Digite o segundo numero "))
    print("A soma é {}".format(num1 + num2))
elif operacao == "-":
    num3 = int(input("Digite o numero "))
    num4 = int(input("Digite o numero "))
    print("A subtração é {}".format(num3 - num4))
elif operacao == "/":
    num5 = int(input("Digite o primeiro numero "))
    num6 = int(input("Digite o segundo numero "))
    print("A divisão é {}".format(num5 / num6))
elif operacao == "*":
    num7 = int(input("Digite o primeiro numero "))
    num8 = int(input("Digite o segundo numero "))
    print("A multiplicação é {}".format(num7 * num8))


--------------------------------------------------------------

EXERCÍCIOS DE REPETIÇÃO

# Exercício 6
i = 1
numero = 0
while i < 11:
    numero += int(input(f'({i}/10) - Digite um número: '))
    i += 1
print(f'O resultado da media dos números digitados foi de: {numero/10}')

--------------------------------------------------------------
# Exercício 7

i = 1
num = 0
while 0 < i < 11:

    num += int(input("Digite o numero {}/10 ".format(i)))
    if num < 0:
        print("Numeros negativos serão ignorados")
    i += 1
print("Média dos numeros é {}".format(num/10))

--------------------------------------------------------------

# Exercicio 8
maior = 0
menor = 0

for i in range(1, 11):
    a = int(input("Digite um valor {}/10 ".format(i)))
    if i == 1:
        menor = a
        maior = a
    if a > maior:
        maior = a
    elif a < menor:
        menor = a
print("O menor valor é {} e o maior é {}".format(menor, maior))

------------------------------------------------------------------
""" Para imprimir a quantidade de nuúmeros impares até o numero informado"""
n = int(input("Digite um número: "))

for i in range (1, n):
    if n % 2 == 1:
        print(n)
    n -= 1
# Segunda forma

n = int(input("Digite um número: "))

for i in range(1, n+1, 2):
    print(i)

"""O exercicio pede para imprimir a quantidade de número impares que o usaurio desejar logo fica da seguinte maneiri"""
n = int(input("Insira um número "))

for n in range(1, n+n, 2):
    print(n)



------------------------------------------------------------------

# Exercicio 10

soma = 0

for i in range(0, 100, 2):
    soma = i + soma
print("A soma dos primeiros 50 num é {}".format(soma))

-------------------------------------------------------------------

# Exercicio 11

n = int(input("Digite um valor: "))
i = 0
while i < n+1:
    print(i)
    i += 1
--------------------------------------------------------------------

# Execício 12

n = int(input("Digite um valor: "))
i = 0
while n+1 != i:
    print(n)
    n -= 1
#Segunda forma
n = int(input('Insira o número: '))
for d in range(n, -1, -1):
    print(d)

------------------------------------------------

# Exercício 13

n = int(input("Digite um valor: "))
i = 0
while i < n+1:
    if i % 2 == 0:
        print(i)
    i += 1

------------------------------------------------

# Exercício 14

n = int(input("Digite um valor: "))
i = 0
while n+1 > i:
    if i % 2 == 0: #ou n % 2 == 1
        print(n)
    n -= 2

-------------------------------------------------

# Exercício 15

n = int(input("Digite um valor: "))
i = 0
while i < n+1:
    if i % 2 == 1:
        print(i)
    i += 1

-------------------------------------------------

# Exercício 16

n = int(input("Digite um valor: "))
i = 1
while i < n+1:
    if n % 2 == 1:
        print(n)
    n -= 1

-------------------------------------------------

# Exercício 17

num = int(input("Digite um número:"))
soma = 0
n = 0
while n < num:
    soma += num
    num -= 1
print(soma)

-----------------------------------------------

# Exercício 17 segunda forma para a saida comçar do numero mais baixo

num = int(input("Digite um número:"))
soma = 0
n = 0
while num+1 > n:
    print(soma)
    n += 1
print(soma)

--------------------------------------------------------------------

# Exercicio 18

qtd_de_num = int(input("Digite a quantidae de número a serem lidos "))
contador = 0
maior = 0
maior_lido = 0
while contador < qtd_de_num:
    num = int(input("Digite o numero {}/{} ".format(contador+1, qtd_de_num)))
    contador += 1
    if maior_lido < num:
        maior_lido = num
        maior = 1
    elif num == maior_lido:
        maior += 1

print("O maior numero lido foi {} e foi lido {} vezes".format(maior_lido, maior))

---------------------------------------------------------------------

# Exercicio 18

num = int(input("Digite um numero entre 100 e 999 "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
if 100 > num or num > 999:
    print("numero invalido: ")
for num in range(100, 999):
    if True:
        print("Unidade {} dezena {} centena {}".format(u, d, c))
        break

----------------------------------------------------------------------

# Exercicio 20
pares = 0
dados_lidos = 0

n = int(input("Digite um numero: "))

while n != 1000:
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        pares += 1
    dados_lidos += 1
print("Temos {} numeros pares e foram lidos {} dados".format(pares+1, dados_lidos))

------------------------------------------------------------------------

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0
multi = 1
if num1 > num2:
    for n in range(num2, num1):
        if n % 2 == 0:
            soma += n

        elif n % 2 == 1:
            multi = multi * n
    print("A soma dos números pares é {}".format(soma))
    print("A multiplicação dos impares é ".format(multi))
else:
    for n in range(num1, num2):
        if n % 2 == 0:
            soma += n
        elif n % 2 == 1:
            multi *= n
            print(soma)
    print("A soma dos números pares é {}".format(soma))
    print("A multiplicação dos impares é {} ".format(multi))

------------------------------------------------------------------------------

