
## folha: algo_exer_selecao

# 1
numero = int(input("Digite um número inteiro: "))

if numero == 0:
    print("Igual a Zero")
else:
    print("Diferente de Zero")


# 2
numero = int(input("Digite um número entre 1 e 9: "))
if numero <= 9 and numero >= 1:
    print("Valor na faixa.")
else:
    print("Valor fora da faixa.")


# 3 triângulo retângulo
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

# 4 triângulo equilátero
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))   
ladoC = int(input("Digite o terceiro lado: "))

if ladoA == ladoB == ladoC:
    print("O triângulo é equilátero.")
else:
    print("O triângulo não é equilátero.")

# 5 triângulo isósceles
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

if ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("O triângulo é isósceles.")
    else
    print("O triângulo não é isósceles.")

