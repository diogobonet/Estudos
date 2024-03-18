import socket

HOST = "127.0.0.1"
PORTA = int(input('[CLIENTE] Entre com a porta do servidor: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORTA))

sock.sendall(str.encode("Estou enviando uma mensagem!"))
dados = sock.recv(2048)
print(f"Mensagem enviada {dados}")