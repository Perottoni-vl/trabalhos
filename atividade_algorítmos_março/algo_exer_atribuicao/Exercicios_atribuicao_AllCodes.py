##folha de exercícios número - 3

##exercício_1)

print("Digite as faltas do primeiro semestre: ")
faltas_1 = int(input())
print("Digite as faltas do segundo semestre: ")
faltas_2 = int(input()) 

soma_faltas = faltas_1 + faltas_2
print("A soma das faltas do aluno é: ", soma_faltas)

##exercício_2) {forma mais simples de escrever o mesmo código}

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

print("A soma das três notas é: ", nota_1 + nota_2 + nota_3)

##exercício_3)

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print("A média das três notas é: ", media)

##exercício_4) {não dei conta de fazer}

horas = float(input("Digite as horas e os minutos: "))


##exercício_5)

temp_celsius = float(input("Digite a temperatura em graus Celsius: "))
temp_fah = (temp_celsius * 1.8) + 32
print("A temperatura em graus Fahrenheit é: ", temp_fah) 

##exercício_6) 

lado_a = float(input("Digite o valor do primeiro lado: "))
lado_b = float(input("Digite o valor do segundo lado: "))
 
hipotenusa = (lado_a ** 2 + lado_b ** 2) ** 0.5 ##elevar à 0.5 é o mesmo que tirar a raiz quadrada. Não sabia kkkaka

print("O valor da hipotenusa é: ", hipotenusa)

##exercício_7)

valor_a = float(input("Digite o valor de A: "))
valor_b = float(input("Digite o valor de B: "))
valor_c = float(input("Digite o valor de C: "))
valor_d = float(input("Digite o valor de D: "))

media = (valor_a * 3 + valor_b * 4 + valor_c * 2 + valor_d * 5) / 14 

##exercicio_8) 

valor_a = float(input("Digite o valor de A: "))
valor_b = float(input("Digite o valor de B: "))
valor_c = float(input("Digite o valor de C: "))
valor_d = float(input("Digite o valor de D: "))

media = (valor_a * 7 + valor_b * 3 + valor_c * 4 + valor_d * 2) / 16 

print("O valor da média é: ", media)

##exercício_9) {nao peguei o raciocínio} 

dias_atraso = int(input("Digite o número de dias de atraso: "))         
prestacao = float(input("Digite o valor da prestação: "))
taxa_de_juros = float(input("Digite a taxa de juros diária (em %): "))

nova_prestacao = prestacao + (prestacao * (taxa_de_juros / 100) * dias_atraso) 

print("O valor da nova prestação é: ", nova_prestacao)

##exercício_10) {agora que descobri que da pra importar coisas de outras bibliotecas}

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))
pi = 3.14

volume = pi * (raio ** 2) * altura
print("O volume do cilindro é: ", volume)

##exercício_11) 

import math

raio_cone = float(input("Digite o raio da base do cone: "))
altura_cone = float(input("Digite a altura do cone: "))
pi = math.pi

area_base = pi * (raio_cone ** 2) ##famoso pirr
volume = area_base * altura_cone / 3

print("O volume do cone é: ", volume)   

##exercício_12) 

import math

raio = float(input("Digite o raio da base do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))
math.pi

area_base = math.pi * (raio ** 2)
area_lateral = 2 *math.pi * raio * altura

area_total = 2 * area_base + area_lateral

print("A área total do cilindro é: ", area_total)


