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