soma_idades = 0
for i in range(50):
    idade = int(input("Digite a idade da pessoa: "))
    soma_idades += idade

media = soma_idades // 50
print("A média das idades é:", media)
