import json

try:
    with open("biblioteca.json", "r", encoding="utf-8") as arquivo:
        biblioteca = json.load(arquivo)
except FileNotFoundError:
    biblioteca = []

#Definindo funções]#

def salvar_dados():
    with open("biblioteca.json", "w", encoding="utf-8") as arquivo:
        json.dump(biblioteca, arquivo, ensure_ascii=False, indent=4)


def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano de publicação: ")
    
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": "Sim"
    }
    
    biblioteca.append(livro)
    salvar_dados()
    print("Livro cadastrado com sucesso!")

def listar_livros():
    for livro in biblioteca:
        print(livro)

def buscar_livro():
    titulo_busca = input("Digite o título do livro a ser buscado: ")
    
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo_busca:
            print(livro)
            return
    
    print("Livro não encontrado.")
  

def emprestar_livro():
    titulo_busca = input("Digite o título do livro que deseja emprestar: ").lower()
    
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo_busca:
            if livro["disponivel"] == "Sim":
                livro["disponivel"] = "Não"
                salvar_dados()
                print("Livro emprestado com sucesso!")
            else:
                print("Este livro já está emprestado.")
            return
            
    print("Livro não encontrado.")

def devolver_livro():
    titulo_busca = input("Digite o título do livro que deseja devolver: ").lower()
    
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo_busca:
            if livro["disponivel"] == "Não":
                livro["disponivel"] = "Sim"
                salvar_dados()
                print("Livro devolvido com sucesso!")
            else:
                print("Este livro já está disponível na biblioteca.")
            return
            
    print("Livro não encontrado.")

def remover_livro():
    titulo_busca = input("Digite o título do livro que deseja remover: ").lower()
    
    for i, livro in enumerate(biblioteca):
        if livro["titulo"].lower() == titulo_busca:
            biblioteca.pop(i)
            salvar_dados()
            print("Livro removido com sucesso!")
            return
            
    print("Livro não encontrado.")

#Menu#

opcao= ""

while opcao != "7":
    print("\n--- MENU BIBLIOTECA ---")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro")
    print("4. Emprestar livro")
    print("5. Devolver livro")
    print("6. Remover livro")
    print("7. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        emprestar_livro()
    elif opcao == "5":
        devolver_livro()
    elif opcao == "6":
        remover_livro()
    elif opcao == "7":
        print("Saindo do programa...Até mais!")
    else:
        print("Opção inválida. Tente novamente.")

        print("Opção inválida. Tente novamente.")
