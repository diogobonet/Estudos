ano_atual = 2022
nascimento = int(input("Informe o ano em que você nasceu: "));
idade = ano_atual - nascimento;
resp = input("Você já fez aniversário esse ano? (Sim ou Não) ");
if resp == "Não":
    idade -= 1
print("Sua idade é {}!" .format(idade));