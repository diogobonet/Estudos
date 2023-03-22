for i in range(1 , 5+1):
    num = int(input("Digite o {}º número: ".format(i)))
for c in range(4):
    for i in range(4):
        if num[i] > num[i + 1]:
                num[i+1], num[i] = num[i], num[i+1]
print(*num)