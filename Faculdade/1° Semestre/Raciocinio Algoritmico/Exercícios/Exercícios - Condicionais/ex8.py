l1 = int(input("Tamanho do Primeiro Lado do Triângulo: "))
l2 = int(input("Tamanho do Segundo Lado do Triângulo: "))
l3 = int(input("Tamanho do Terceiro Lado do Triângulo: "))

if l1 + l2 < l3:
    print("Não é um triângulo!")

if l1 == l2 == l3:
    print("É um triângulo Equilátero! Possui todos os lados iguais!")

if l1 == l2 or l2 == l3 or l1 == l3:
    print("É um triângulo Isóceles! Triangulo com dois lados iguais!")

if l1 != l2 != l3:
    print("É um triângulo Escalento! Pois tem todos os lados diferentes!")
