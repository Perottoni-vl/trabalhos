contador = 0
soma_notas = 0

for i in range(10):
    nota = float(input("Digite a nota do aluno : "))
    
    if nota > 5.0 and nota < 7.0:
        contador += 1
        soma_notas += nota
        media = soma_notas / contador

print("A média das notas dos alunos com nota maior que 5.0 ou menor que 7.0 é:", media)