import socket

HOST = "127.0.0.1"
PORTA = int(input('[CLIENTE] Entre com a porta do servidor: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORTA))

enviar = input("manda ai: ")
sock.sendall({enviar.encode('utf-8')})
dados = sock.recv(2048)
print(f"Mensagem enviada {dados}")