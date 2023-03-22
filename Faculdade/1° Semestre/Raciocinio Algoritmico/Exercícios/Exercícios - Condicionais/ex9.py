valor = float(input("Quanto você quer sacar? (min: R$10 | max: R$600)\n"))
notas100 = 100
notas50 = 50
notas10 = 10
notas5 = 5
notas1 = 1


if valor < 10 or valor > 600:
    print("O valor de saque mínimo é de R$10. E o máximo é de R$600! Tente novamente!")

    if valor >= 100:
        notas100 = valor % 100
        notas50 = notas100 % 50
        notas10 = notas50 % 10
        notas5 = notas10 % 5
        notas1 = notas5 % 1
    
    if valor <= 100:
        notas100 = valor % 100
        notas50 = notas100 % 50
        notas10 = notas50 % 10
        notas5 = notas10 % 5
        notas1 = notas5 % 1

print("Você recebe {} notas de R$100" .format(notas100))
print("Você recebe {} notas de R$50" .format(notas50))
print("Você recebe {} notas de R$10" .format(notas10))
print("Você recebe {} notas de R$5" .format(notas5))
print("Você recebe {} notas de R$1" .format(notas1))
    


    
    


    


