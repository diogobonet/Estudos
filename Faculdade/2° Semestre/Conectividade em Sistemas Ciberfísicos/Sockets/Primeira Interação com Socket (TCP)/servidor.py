#Importar biblioteca da API
import socket

#HOST = '127.0.0.1' : loopback
HOST = 'localhost'
PORTA = 50001

# CRIAÇÃO DE NOSSO SOCKET
# Inicialização com tipo de endereçamento e IP e PROTOCOLO
# IPv4: AF_INET
# TCP SOCCK_STREAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# VINCULAR HOST E PORTA 
sock.bind((HOST, PORTA))

# ENTRAR NO MODO DE ESCUTA
sock.listen()
print("Aguardando servidor...")

# RETORNA A PORTA E UM ENDEREÇO 
# QUANDO O CLIENTE SE CONECTA:
conn, ender = sock.accept()
print(f"Conectando em {ender}")

# Recebimento dos dados do cliente
# Loop de recebimento
while True:
    dados = conn.recv(1024) # Tamanho do buffer
    if not dados:
        print("Fechando conexão")
        conn.close()
        break
    # Enviar confirmação de resposta
    conn.sendall(dados)