# Nome: Diogo Bonet Sobezak | Data: 19/04
import os
import datetime
import stat

data_hora = datetime.datetime.now()

if os.path.isfile('permissao.txt'):
    print("Este arquivo já foi criado")
else:
    with open('permissao.txt', 'w'):
        pass

with open('permissao.txt', 'a') as f:
    f.write(f'{data_hora}\n')
os.chmod('permissao.txt', stat.S_IRUSR)