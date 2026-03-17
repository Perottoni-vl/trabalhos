contador_5_0 = 0

for i in range(20):

    nota = float(input("Digite a nota do aluno: "))
    if nota >= 5.0:
        contador_5_0 += 1

print("A quantidade de alunos com nota 5.0 ou maior é:", contador_5_0)