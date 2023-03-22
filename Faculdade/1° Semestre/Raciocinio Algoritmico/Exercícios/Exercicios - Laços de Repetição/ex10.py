paisa = 5000000
paisb = 7000000
anos = 0
while paisa < paisb:
    paisa += paisa * 0.03
    paisb += paisb * 0.02
    anos += 1
print("É necessario {} anos para o país A ultrapassar o país B no indice populacional!" .format(anos))