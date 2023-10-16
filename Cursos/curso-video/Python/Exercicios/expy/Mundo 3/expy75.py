nums = (int(input("Digite um número:")), int(input("Digite um número:")), int(input("Digite um número:")), int(input("Digite um número:")))
print(f"Você digitou os valores {nums}")
print(f"O valor 9 foi digitado {nums.count(9)} vez!")
if 3 in nums:
    print(f"O valor 3 está na posição {nums.index(3) + 1}!")
for n in nums:
    if n % 2 == 0:
        print("Os valores pares digitados foram", n)