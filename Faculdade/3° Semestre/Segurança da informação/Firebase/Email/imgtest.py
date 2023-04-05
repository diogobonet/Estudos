import smtplib # importa biblioteca para trabalhar com o SMTP
from email.mime.multipart import MIMEMultipart # importando bilioteca para trabalhar com formato MIME
from email.mime.text import MIMEText # importanto biblioteca para trabalhar com o email no formato texto
from email.mime.image import MIMEImage
### Defição das varíáveis para servidor de email ###
server = 'smtp.gmail.com' # servidor SMTP
port = 587 # porta para usar STARTTLS
username = "livenowgamer@gmail.com" # username @gmail.com
password = "#" # senha - obter a senha do APP

### definição do email ###
mail_from = "livenowgamer@gmail.com" # remetente
mail_to = "livenowgamer@gmail.com" # destinatário
mail_subject = "Amamos o Gonzaga" # assunto mensagem
mail_body = "Eu queria ser adm, mas adm não posso ser, pois adm só bane, e eu quero ser banido com vc! <3" # Corpo da mensagem

### criando o email ###
mensagem = MIMEMultipart() # cria um para trabalhar com email no formato MIME
mensagem['From'] = mail_from # adicionando o remetente
mensagem['To'] = mail_to # adicionando o destinatário
mensagem['Subject'] = mail_subject # adicionando o assunto do email
mensagem.attach(MIMEText(mail_body, 'plain')) # anexando o email no formato texto simples (plain)
with open('photo.png', 'rb') as f:
    img_data = f.read()
# Crie um objeto MIMEImage com a imagem que você deseja anexar
imagem_anexada = MIMEImage(img_data, name='photo.png')
# Anexe o objeto MIMEImage à mensagem do email
mensagem.attach(imagem_anexada)
### Conexão com o servidor de email ###
connection = smtplib.SMTP(server, port) # abrindo uma conexão como o servidor
connection.starttls() # definir o protocolos de criptografia STARTTLS
connection.login(username,password) # autenticando no servidor
connection.send_message(mensagem)  # enviando mensagem
connection.quit() # Encerrando a conexão