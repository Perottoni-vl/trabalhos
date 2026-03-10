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
