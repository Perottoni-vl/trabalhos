contador = 0
soma_idades = 0

for i in range(10):
    idade = int(input("Digite a idade do aluno : "))
    
    if idade > 25 and idade < 40:
        contador += 1
        soma_idades += idade
        media = soma_idades / contador

print("A média das idades dos alunos com mais de 25 anos ou menos de 40 anos é:", media)

