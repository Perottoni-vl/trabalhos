contador_30 = 0

for i in range(100):
    idade = int(input(f"Digite a idade do aluno {i}: "))
    
    if idade == 30:
        contador_30 += 1

print("Quantidade de alunos com 30 anos:", contador_30)
        