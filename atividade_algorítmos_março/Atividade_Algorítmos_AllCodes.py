
## folha: algo_exer_selecao

#exercício_1
import math


numero = int(input("Digite um número inteiro: "))

if numero == 0:
    print("Igual a Zero")
else:
    print("Diferente de Zero")


#exercício_2
numero = int(input("Digite um número entre 1 e 9: "))
if numero <= 9 and numero >= 1:
    print("Valor na faixa.")
else:
    print("Valor fora da faixa.")


#exercício_3
# triângulo retângulo
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

maior = max(ladoA, ladoB, ladoC)

if maior == ladoA:
    cat1 = ladoB
    cat2 = ladoC
elif maior == ladoB:
    cat1 = ladoA
    cat2 = ladoC
else:
    cat1 = ladoA
    cat2 = ladoB

if maior**2 == cat1**2 + cat2**2:
    print("O triângulo é retângulo.")
else:
    print("O triângulo não é retângulo.")

#exercício_4
# triângulo equilátero
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))   
ladoC = int(input("Digite o terceiro lado: "))

if ladoA == ladoB == ladoC:
    print("O triângulo é equilátero.")
else:
    print("O triângulo não é equilátero.")


#exercício_5
# triângulo isósceles (pode conter os três lados de valores iguais)
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

if ladoA == ladoB:
    print("O triângulo é isósceles.")
elif ladoA == ladoC:
    print("O triângulo é isósceles.")
elif ladoB == ladoC:
    print("O triângulo é isósceles.")
elif ladoA == ladoB == ladoC:
    print("O triângulo não é isósceles.")
else:
    print("O triângulo não é isósceles.")


#exercício_6
# triângulo escaleno
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

if ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
    print("O triângulo é escaleno.")
else:
    print("O triângulo não é escaleno.")


#exercício_7
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))


maior = max(valor1, valor2)
menor = min(valor1, valor2)

maior/menor = valor3

print("O resultado da divisão do maior pelo menor é:", valor3)

#exercício_8 (esse eu não consegui fazer, tive que usar ferramentas externas para resolver. 
# Porém, aprendi mais sobre a linguagem Python)
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

delta = valor2**2 - 4*valor1*valor3

if delta < 0:
    print("Não Existe Valores Reais")
else:
    x1 = (-valor2 + math.sqrt(delta)) / (2*valor1)
    x2 = (-valor2 - math.sqrt(delta)) / (2*valor1)

    print("Valor de x1:", x1)
    print("Valor de x2:", x2)










