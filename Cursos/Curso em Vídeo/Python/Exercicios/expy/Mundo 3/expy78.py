valores = []
mai = 0
men = 0

for v in range(0,5):
    valores.append(int(input(f"Digite um valor para a posição {v}:")))
    if v == 0:
        mai = men = valores[v]
    else:
        if valores[v] > mai:
            mai = valores[v]
        if valores[v] < men:
            men = valores[v]
    
print("-="*35)
print(f"O maior valor digitado foi {mai} e está nas posição:", end="")
for i, v in enumerate(valores):
    if v == mai:
        print(f"{v}...")
print(f"O menor valor digitado foi {men} e está nas posição: ", end="")
for i, v in enumerate(valores):
    if v == men:
        print(f"{v}...")