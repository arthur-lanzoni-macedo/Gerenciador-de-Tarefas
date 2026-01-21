import os

# NOME DO PROJETO
def nome_projeto():
    print("*" * 25)
    print(("𝓖𝓮𝓻𝓮𝓷𝓬𝓲𝓪𝓭𝓸𝓻 𝓭𝓮 𝓣𝓪𝓻𝓮𝓯𝓪𝓼"))
    print("*" * 25)

tarefas = []

# TITULOS
def titulos(texto):
    os.system("cls")
    print(texto)
    print()

# OPÇÕES
def opcoes():
        print("\nMenu de Opções: ")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

# ESCOLHER OPÇÃO
def escolha_opcao():
    
    while True:
        opcao = int(input("\nEscolha uma opção: "))
        if opcao == 1:
            adicionando()
        elif opcao == 2:
            listando()
        elif opcao == 3:
            print("concluindo tarefa")
        elif opcao == 4:
            print("removendo")
        elif opcao == 5:
            finalizar_app()
        else:
            opcao_invalida()

# OPÇÃO INVÁLIDA     
def opcao_invalida():
    print("\n⚠️ Opção inválida! Pressione Enter para tentar novamente.")
    input()
    voltar_ao_menu()

# FINALIZAR APP
def finalizar_app():
    print("\n👋 Saindo do sistema... Até logo!")
    exit()

# SCRIPT VOLTAR
def voltar():
    print("\n⌨️  Pressione [Enter] para voltar ao menu... 🔙")
    input()
    voltar_ao_menu()

# VOLTAR AO MENU  
def voltar_ao_menu():
    os.system("cls")
    nome_projeto()
    opcoes()

# ADICIONAR
def adicionando():
    titulos("✨ ADICIONAR NOVA TAREFA")
    
    print("1- Adicionar Tarefa")
    tarefas_adicionada = input("Digite uma tarefa: ")
    
    tarefas.append(tarefas_adicionada)
    print("\n✅ Tarefa adicionada com sucesso! ✨")
    voltar()
    
# LISTAR
def listando():
    titulos("📋 SUA LISTA DE TAREFAS")
    
    if tarefas:
        for numero, tarefa in enumerate(tarefas, start=1):
            print(f"{numero:02d} → {tarefa}")
    else:
        print("\n⚠️  Atenção: Nenhuma tarefa encontrada.")
        print("Dica: Que tal adicionar algo novo? 📝")
    voltar()
    
nome_projeto()
opcoes()
escolha_opcao()