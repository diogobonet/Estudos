import socket # Importar o socket

# Deinindo 
HOST = input('[SERVIDOR] Entre com o IP HOST do servidor: ')
PORTA = int(input('[SERVIDOR] Entre com a porta do servidor: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPV4 e TCP
while True:
    try:
        sock.bind((HOST, PORTA))
        break
    except:
        sock.bind((HOST, PORTA))
        continue

print(f"Servidor se conectando ao ip {HOST}:{PORTA}! Aguardando servidor de cliente se conectar...")

while True:
    dados = sock.recvfrom(1024)

    print(f"Mensagem recebida ({dados})")
    
    if not dados:
        print("O servidor não recebeu os dados do cliente.py!")
        break
