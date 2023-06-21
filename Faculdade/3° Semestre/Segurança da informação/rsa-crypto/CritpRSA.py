# Atenção: É necessário instalar o pacote pycryptodome (!pip install pycryptodome)
# Criptografia RSA 1024 bytes usando a biblioteca library

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time

inicio = time.time()
keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
print(f"Chave Pública:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Chave Privada: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

plaintext = "RSA: algoritmo dos professores do MIT: Rivest, Shamir e Adleman"
msg = bytes(plaintext,'utf-8')
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Cifrado: ", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decifrado: ', decrypted)
fim = time.time()
tempo_decorrido = fim - inicio

print("Tempo decorrido: ", tempo_decorrido, " segundos")