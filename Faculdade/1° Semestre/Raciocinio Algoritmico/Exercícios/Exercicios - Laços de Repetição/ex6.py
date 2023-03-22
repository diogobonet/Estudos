massa = float(input("Insira a massa do objeto em Gramas: "))
seg = 0

while massa > 0.5:
    seg += 50
    massa /= 2

print("Massa: {}".format(massa))
print("Segundos: {}".format(seg))