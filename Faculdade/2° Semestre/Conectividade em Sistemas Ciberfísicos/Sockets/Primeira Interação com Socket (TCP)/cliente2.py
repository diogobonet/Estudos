# SCRIPT PARA O CLIENTE
import socket

# INFOS DO SERVER
HOST = '127.0.0.1'
PORTA = 50001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# CONEXÃO COM O SERVIDOR (infos do server)
sock.connect((HOST, PORTA))

# ENVIAR UMA STRING DE DADOS
# str.encode() -> string codifida
sock.sendall(str.encode('RAPAZ! RATINHO!'))

# Receber do Servidor
dados = sock.recv(2048)

print(f"Mensagem ecoada do servidor {dados}")