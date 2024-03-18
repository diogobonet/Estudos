num = [2, 5, 9, 1] # Lista
num[2] = 3 # Mudar um valor dentro da lista
num.append(7) # Adicionar um elemento a uma lista
num.sort() # Organizar os elementos dentro de uma lista
num.sort(reverse=True) ## Organizar os Elementos de trás para frente
num.insert(2, 2) # Inserir um número em uma posição da Lista (primeiro num: Posição) | (segundo número
# o valor)#
num.remove(2) # Remove o elemento da lista
num.pop() # Remove o ultimo valor da lista
# num.pop(2) # Remove o item que está na posição 2
print(num)
print(f"Essa lista tem {len(num)} elementos.")

if 4 in num:
    num.remove(4)
else:
    print("Não foi possivel localizar o número 4!")