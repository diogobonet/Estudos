num = []
for c in range(5):
    num.append(int(input(f"Digite um número na posição {c}:")))
    num.sort()
print(f"A lista de forma ordenada ficou como: {num}")