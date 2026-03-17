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