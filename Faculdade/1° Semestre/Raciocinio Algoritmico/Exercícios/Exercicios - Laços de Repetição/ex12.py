numerobin = input('Insira número binário:\n')
leit = len(numerobin)
m = 1
numerodecimal = 0

for i in range(leit-1, -1, -1):
    numerodecimal += int(numerobin[i]) * m
    m *= 2

print('Número decimal: {}'.format(numerodecimal))