soma_notas = 0
for i in range(10):
    nota = float(input("Digite a nota do aluno: "))
    soma_notas += nota
    media = soma_notas / 10
print("A média das notas é:", media)