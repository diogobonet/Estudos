import random
num = int(input("Em que numero eu pensei? "))
random = random.randint(0, 5)
if num == (random):
    print("VOCÊ GANHOU! Eu escolhi {} e você acertou!" .format(num))
else:
    print("Você perdeu! Eu escolhi {} e você escolheu {}" .format(random, num))
    