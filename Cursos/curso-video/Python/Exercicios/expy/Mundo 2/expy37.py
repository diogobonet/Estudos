num = int(input("Digite um número inteiro: "))
print("Escolha uma das opções abaixo para a CONVERSÃO")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
opção = str(input("Sua opção: "))
if opção == "1" or opção == "um":
    print("O número {} em binário é = {}" .format(num, bin(num)))
elif opção == "2" or opção == "dois":
    print("O número {} em OCTAL é ={}" .format(num, oct(num)))
elif opção == "3" or opção == "três" or opção == "tres":
    print("O número {} em HEXADECIMAL é ={}" .format(num, hex(num)))
else:
    print("ALGO DEU ERRADO! TENTE NOVAMENTE!")