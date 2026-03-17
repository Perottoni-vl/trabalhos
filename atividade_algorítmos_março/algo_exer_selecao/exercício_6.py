ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

if ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
    print("O triângulo é escaleno.")
else:
    print("O triângulo não é escaleno.")