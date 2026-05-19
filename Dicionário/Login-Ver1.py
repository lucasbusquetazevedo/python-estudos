banco_usuarios = {}

while True:
    print("\n--- SISTEMA DE ACESSO ---")
    print("1. Criar Conta")
    print("2. Fazer Login")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    # CRIAR CONTA
    if opcao == "1":
        print("\n--- CADASTRO ---")
        novo_login = input("Crie seu nome de usuário: ")
        if novo_login in banco_usuarios:
            print("Erro! Este usuário já existe.")
        else:
            nova_senha = input("Crie sua senha: ") 
            banco_usuarios[novo_login] = nova_senha
            print("Conta criada com sucesso!")
    # LOGIN
    elif opcao == "2":
        print("\n--- LOGIN ---")
        login_digitado = input("Digite seu usuário: ")

        if login_digitado in banco_usuarios:
            while True:
                senha_digitada = input("Digite sua senha: ")
                if senha_digitada == banco_usuarios[login_digitado]:
                    print(f"Acesso concedido! Bem-vindo, {login_digitado}.")
                    break
                else:
                    print("Senha incorreta! Tente novamente.")
        else:
            print("Usuário não encontrado!")
    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")