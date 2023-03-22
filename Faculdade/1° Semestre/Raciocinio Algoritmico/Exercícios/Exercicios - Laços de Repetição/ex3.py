num1 = int(input("Digite um número inteiro e positivo: "))
num2 = int(input("Digite um número inteiro e positivo: "))
for i in range(num1, (num2 + 1)):
    print(i)
    primo = True
    for c in range(i):
        if (c != 0 and c != 1):
            if (i % c == 0):
                primo = False
    if (primo):
        print("Os números nesse intevalos", i, "são primos")