import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hip = math.hypot(co, ca)
print("A hipotenusa é {}" .format(hip))