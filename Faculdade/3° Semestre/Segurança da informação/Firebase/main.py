import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDwWmqCL9OxWk_Twy0XJWWxrIoSYEV6Klo",
  "authDomain": "informationsecurity-44c91.firebaseapp.com",
  "projectId": "informationsecurity-44c91",
  "databaseURL": "https://" + "<ID_APP>" + ".firebaseio.com",
  "storageBucket": "informationsecurity-44c91.appspot.com",
  "messagingSenderId": "141389318821",
  "appId": "1:141389318821:web:96b617eb3d034ae08d5b4c",
  "measurementId": "G-1MKEV6E82C"
}

# Inicializa a aplicação
firebase = pyrebase.initialize_app(firebaseConfig);

# Cria o usuário
auth = firebase.auth()

email = input("Email: ")
senha = input("Senha: ")

usuario = auth.create_user_with_email_and_password(email, senha)
print("Email e senha criados com Sucesso! Token", usuario)
