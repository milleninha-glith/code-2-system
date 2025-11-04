print("** MINI SISTEMA DE USUÁRIO **\n")

def cadastro_new_user():
    print("CADASTRO DE NOVOS USUÁRIOS: \n")
    new_username = input("Digite seu username: ")
    new_password = input("Olá", new_password, "! Digite sua nova senha: ")

    new_password = input(new_username, ", Confirme sua senha: ")

    while new_password != nova_senha:
        new_password = input("Tente novamente! Digite sua nova senha: ")
    print (new_username, ", Você foi cadastrado!")

def user_cadastrado():
    nome_cad = "vini"
    senha_cad = "123"

    username_cad = input("Digite seu usuário cadastrado: ")
    password_cad = input("Digite sua senha cadastrada: ")

    if username_cad == nome_cad:
        while password_cad != senha_cad:
                password_cad = input("Tente novamente! Digite sua senha cadastrada: ")
        print("Usuário Logado no MINI SYSTEM")
    else:
        print("Usuário não cadastrado!")
        def definir_opcao(){ 
      opcao_inicial = int(input("Digite 1 para fazer LOGIN ou Digite 2 para CADASTRO: \n"))
if opcao_inicial == 1 or opcao_inicial == 2:
    if opcao_inicial == 1:
        user_cadastrado()
    else:
        cadastro_new_user()
else:
    print("Opção não encontrada! Tente novamente mais tarde.")
 }

