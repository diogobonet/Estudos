digite = input("Digite algo: ")
print("O tipo primitivo desse valor é {}!" .format(type(digite)));
print("Só tem espaços? ", digite.isspace)
print("É um número? {}" .format(digite.isalnum))
print("É alfabetico? {}" .format(digite.isalpha))
print("É maiusculo? {}" .format(digite.isupper))
print("É minusculo? {}" .format(digite.islower))
print("É capitalizado? {}" .format(digite.istitle))