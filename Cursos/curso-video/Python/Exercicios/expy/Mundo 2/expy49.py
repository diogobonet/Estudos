num = int(input("Digite a tabuada que você quer ver: "))
for c in range(1, 11):
    tabuada = num * c
    print("{} X {} = {}".format(num, c, tabuada))