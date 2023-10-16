
n1 = int(input("Primeiro valor:\n"))
n2 = int (input("Segundo valor:\n"))
while True:
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    resp = int(input(">>>>>> Qual é a sua opção?\n"))
    if resp == 1:
        soma = n1 + n2
        print("A soma entre {} + {} = {}".format(n1, n2, soma))
    if resp == 2:
        mult = n1 * n2
        print("A multiplicação entre {} * {} = {}" .format(n1, n2, mult))
    if resp == 3:
        if n1 >= n2:
            print("O número {} é maior que o número {}!" .format(n1, n2))
        if n2 > n1:
            print("O número {} é maior que o número {}!".format(n2, n1))
        else:
            print("Os números {} e {} são iguais.".format(n1, n2))
    if resp == 4:
        print("Informe novos números!")
        n1 = int(input("Primeiro valor:\n"))
        n2 = int (input("Segundo valor:\n"))
    if resp == 5:
        print("Finalizando!")
        break
    else:
        print("Tente novamente!")
print("Fim do programa! Volte sempre!")