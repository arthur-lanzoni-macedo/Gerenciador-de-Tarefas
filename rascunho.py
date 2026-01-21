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
        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                adicionando()
            elif opcao == 2:
                listando()
            elif opcao == 3:
                concluir()
            elif opcao == 4:
                remover()
            elif opcao == 5:
                finalizar_app()
            else:
                opcao_invalida()

        except ValueError:
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

# CONCLUIR
def concluir():
    titulos("✔️ CONCLUIR TAREFA")

    if not tarefas:
        print("\n⚠️ Atenção: Nenhuma tarefa encontrada.")
        voltar()
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"{numero:02d} → {tarefa}")

    try:
        id_concluir = int(input("\n✔️ Digite o número da tarefa que deseja concluir: "))

        if 1 <= id_concluir <= len(tarefas):
            tarefas[id_concluir - 1] = f"[✔] {tarefas[id_concluir - 1]}"
            print("\n✅ Tarefa concluída com sucesso!")
        else:
            print("\n❌ Número inválido.")

    except ValueError:
        print("\n❌ Digite apenas números.")

    voltar()

# REMOVER
def remover():
    titulos(("🗑️ REMOVER TAREFA"))
    
    if not tarefas:
        print("\n⚠️ Atenção: Nenhuma tarefa encontrada.")
        voltar()
    else:
        print("\n📋 Lista de tarefas:")
        for numero, tarefa in enumerate(tarefas, start=1):
            print(f"{numero:02d} → {tarefa}")

        id_remover = input("\n🗑️ Digite o número da tarefa que deseja remover: ")

        if id_remover.isdigit():
            id_remover = int(id_remover)

            if 1 <= id_remover <= len(tarefas):
                tarefa_removida = tarefas.pop(id_remover - 1)
                print(f"\n✅ Tarefa removida: {tarefa_removida}")
            else:
                print("\n❌ Número inválido.")
        else:
            print("\n❌ Digite apenas números.")
        voltar()

    
nome_projeto()
opcoes()
escolha_opcao()