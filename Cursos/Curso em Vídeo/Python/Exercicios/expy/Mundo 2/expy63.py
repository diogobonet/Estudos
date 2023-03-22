print("-"*30)
print("Sequencia de Fibonacci")
print("-"*30)
quant = int(input("Quantos termos você quer mostrar? "))
start1 = 0
start2 = 1
cont = 3    
print("{} -> {}".format(start1, start2), end = "")
while cont <= quant:
    conta = start1 + start2
    cont += 1
    print(" -> {}".format(conta), end = "")
    start1 =  start2
    start2 = conta
print(" -> FIM")
