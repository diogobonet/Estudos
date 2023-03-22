import socket # Importar o socket

# Deinindo 
HOST = "127.0.0.1"
PORTA = int(input('[SERVIDOR] Entre com a porta do servidor: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4 e TCP
while True:
    try:
        sock.bind((HOST, PORTA))
        break
    except:
        sock.bind((HOST, PORTA))
        continue

sock.listen()
print(f"Servidor se conectando ao ip {HOST}:{PORTA}! Aguardando servidor de cliente se conectar...")

while True:
    conn, ender = sock.accept()
    dados = conn.recv(1024)
    print(f"Conectando no {ender}")
    conn.sendall(dados)
    print(f"Mensagem recebida ({dados.decode()})")
    print("Foram recebidos", len(dados), "bytes!")
    if not dados:
        print("O servidor não recebeu os dados do cliente.py!")
        break
