import random
numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

for nums in numeros:
    print("O números sorteados foram {}".format(numeros))
print(f"O maior valor sorteado foi: {max(numeros)}")
print(f"O menor valor sorteado foi: {min(numeros)} ")