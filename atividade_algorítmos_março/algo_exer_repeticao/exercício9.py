contador = 0

for i in range(20):
    idade = int(input("Digite a idade da pessoa: "))
    if idade == 30:
        contador += 1

print("A quantidade de pessoas com 30 anos é:", contador)