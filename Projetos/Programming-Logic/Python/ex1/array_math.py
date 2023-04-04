string = input("Digite um número: ").split()
numeros = [float(valor) for valor in string]

def sum_array(a):
    soma = 0
    num = []
    if (num == ""):
        num.extend(a)
        return 0
    else:
        num.extend(a)
        for num in a:
            soma += num
        print(soma)

sum_array(numeros)