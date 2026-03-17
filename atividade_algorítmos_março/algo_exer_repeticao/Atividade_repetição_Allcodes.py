
## folha: algo_exer_repeticao

#exercício_1
soma_idades = 0
for i in range(30):
    idade = int(input("Digite a idade da pessoa: "))
    soma_idades += idade

print("A soma das idades é:", soma_idades)  

#exercício_2
soma_idades = 0
for i in range(50):
    idade = int(input("Digite a idade da pessoa: "))
    soma_idades += idade #não entendi esse comando, o que ele faz?

media = soma_idades // 50
print("A média das idades é:", media)

#exercício_3

for i in range(100):
    idade = int(input("Digite a idade da pessoa: "))
    
    if idade == 30:
        contador_30 += 1
        print("A quantidade de pessoas com 30 anos é:", contador_30) #código q eu fiz, mas está errado
##código corrigido por IA:
contador_30 = 0

for i in range(100):
    idade = int(input(f"Digite a idade do aluno {i}: "))
    
    if idade == 30:
        contador_30 += 1

print("Quantidade de alunos com 30 anos:", contador_30)

#exercício_4
contador_5_0 = 0

for i in range(20):
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 5.0:
        contador_5_0 += 1

print("A quantidade de alunos com nota 5.0 ou maior é:", contador_5_0) #esse já consegui me virar

#exercício_5
soma_notas = 0

for i in range(10):
    nota = float(input("Digite a nota do aluno: "))
    soma_notas += nota
    
print("A soma das notas é:", soma_notas)

#exercício_6
soma_notas = 0

for i in range(10):
    nota = float(input("Digite a nota do aluno: "))
    soma_notas += nota
    media = soma_notas / 10 #dá pra colocar outro comando no lugar do "10", porém eu quis fazer 
    #da forma que eu já sei.

print("A média das notas é:", media)

#exercício_7
contador_5_0 = 0

soma_notas = 0

for i in range(10):
    nota = float(input("Digite a nota do aluno: "))
    soma_notas += nota
    if nota >= 5.0:
        contador_5_0 += 1

print("A soma das notas é:", soma_notas, "e a quantidade de alunos com nota 5.0 ou maior é:", contador_5_0)
 
 #exercício_8
soma_idades = 0

for i in range(1, 11):
    idade = int(input(f"Digite a idade do aluno {i}: "))
    
    if idade > 25:
        soma_idades += idade

print("A soma das idades dos alunos com mais de 25 anos é:", soma_idades) #não dei conta de fazer esse.

#exercício_9
contador = 0

for i in range(20):
    idade = int(input("Digite a idade da pessoa: "))
    if idade == 30:
        contador += 1

print("A quantidade de pessoas com 30 anos é:", contador)

#exercício_10
contador = 0
soma_idades = 0

for i in range(10):
    idade = int(input("Digite a idade do aluno : "))
    
    if idade > 25 and idade < 40:
        contador += 1                  #essa função aloca os inputs que passaram a verificação.
        soma_idades += idade           #essa função soma as idades que passaram a verificação.
        media = soma_idades / contador

print("A média das idades dos alunos com mais de 25 anos ou menos de 40 anos é:", media)

#exercício_11
#mesmo raciocínio do exercício_10, só que com o tipo de varível diferente.

contador = 0
soma_notas = 0

for i in range(10):
    nota = float(input("Digite a nota do aluno : "))
    
    if nota > 5.0 and nota < 7.0:
        contador += 1
        soma_notas += nota
        media = soma_notas / contador

print("A média das notas dos alunos com nota maior que 5.0 ou menor que 7.0 é:", media) #esse eu consegui.

#exercício_12
#esse eu fiz na IA. Porém, aprendi alguma coisa.
numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print("O fatorial de", numero, "é:", fatorial)

#exercício_13
#esse eu também fiz na IA, mas entendi o raciocínio.
numero = int(input("Digite um número: "))

if numero <= 1:
    print("Não é primo")       #aqui ele mata se o número pode ser primo ou não.
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("Não é primo")
            break              #aqui ele também mata (verifica) se o número é primo ou não.
    else:
        print("É primo")       #se o número passar por todas as verificações, ele é primo.