soma_idades = 0

for i in range(1, 11):
    idade = int(input(f"Digite a idade do aluno {i}: "))
    
    if idade > 25:
        soma_idades += idade

print("A soma das idades dos alunos com mais de 25 anos é:", soma_idades)
        