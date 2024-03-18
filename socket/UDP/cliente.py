import socket

HOST = input('[CLIENTE] Entre com o IP HOST do servidor: ')
PORTA = int(input('[CLIENTE] Entre com a porta do servidor: '))
msg = input("[CLIENTE] Digite a mensagem: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

sock.connect((HOST, PORTA))

sock.send(str.encode("Estou enviando uma mensagem!"))
