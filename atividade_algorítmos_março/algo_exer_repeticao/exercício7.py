contador_5_0 = 0

soma_notas = 0

for i in range(10):
    nota = float(input("Digite a nota do aluno: "))
    soma_notas += nota
    if nota >= 5.0:
        contador_5_0 += 1

print("A soma das notas é:", soma_notas, "e a quantidade de alunos com nota 5.0 ou maior é:", contador_5_0)
 