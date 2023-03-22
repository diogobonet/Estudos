times = ("Corinthians", "Palmeiras", "São Paulo", "Atlético-MG", "Botafogo", "Santos", "Fluminense", "Coritiba", 
        "America-MG", "Avaí", "Internacional", "Athletico-PR", 
        "Bragantino", "Flamengo", "Goiás", "Cuiaba", "Atletico-GO", "Juventude", "Ceará", "Fortaleza")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Lista de Times no Brasileirão: {}".format(times))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Os 5 primeiros são: {times[0:6]}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Os 4 ultimos são: {times[-4:]}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Times ordenados em Ordem Alfabética: {}".format(sorted(times)))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("O Atletico-GO está na posição {}° do Brasileirão!".format(times.index("Atletico-GO") + 1))