def cadastrar_usuario():
    while True:
        try:
            nome = input("digite seu nome: ")
            cpf = input("digite seu CPF: ")
            senha = input("digite sua senha: ")
            return nome, cpf, senha
        except ValueError:
            print("algo deu errado tente novamente")

def fazer_login(usuarios):
    cpf_l = input("digite seu CPF: ")
    senha_l = input(" crie uma senha: ")

    for usuario in usuarios:
        if cpf_l == usuario[1] and senha_l == usuario[2]:
            print("Login feito com sucesso!")
            return True
        
    print("CPF ou senha incorreta. Tente novamente.")
    return False

def main():
    usuarios = []
    while True:
        print("1. Cadastrar usuario")
        print("2. Fazer login")
        print("3. Sair")

        opcao = input("Escolha uma opção")

        if opcao == "1":
            novo_usuario = cadastrar_usuario()
            if len(novo_usuario [1]) == 11 and novo_usuario[1].isdigit():
                usuarios.append(novo_usuario)
                print("Usuario cadastrado com sucesso!")
            else:
                print("CPF inválido. O CPF deve conter apenas números e ter 11 dígitos")

        elif opcao == "2":
            if fazer_login(usuarios):
                break

            else:
                print("Opcao invalida!")