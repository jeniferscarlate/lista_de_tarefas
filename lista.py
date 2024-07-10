import json
from datetime import datetime

# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma nova tarefa
def adicionarTarefa(tarefa, prioridade, data_vencimento):
    tarefas.append({"tarefa": tarefa, "concluida": False, "prioridade": prioridade, "data_vencimento": data_vencimento})
    print(f'Tarefa "{tarefa}" adicionada.')

# Função para remover uma tarefa
def removerTarefa(tarefa):
    for item in tarefas:
        if item["tarefa"] == tarefa:
            tarefas.remove(item)
            print(f'Tarefa "{tarefa}" removida.')
            return
    print(f'Tarefa "{tarefa}" não encontrada.')

# Função para marcar uma tarefa como concluída
def concluirTarefa(tarefa):
    for item in tarefas:
        if item["tarefa"] == tarefa:
            item["concluida"] = True
            print(f'Tarefa "{tarefa}" marcada como concluída.')
            return
    print(f'Tarefa "{tarefa}" não encontrada.')

# Função para listar todas as tarefas
def listarTarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    for item in sorted(tarefas, key=lambda x: (x["prioridade"], datetime.strptime(x["data_vencimento"], '%d/%m/%Y'))):
        status = "concluída" if item["concluida"] else "não concluída"
        print(f'{item["tarefa"]} - {status} - Prioridade: {item["prioridade"]} - Data de vencimento: {item["data_vencimento"]}')

# Função para listar tarefas com base no status de conclusão
def listarTarefaPorStatus(concluida=True):
    status_text = "concluídas" if concluida else "não concluídas"
    filtered_tarefas = [item for item in tarefas if item["concluida"] == concluida]
    
    if not filtered_tarefas:
        print(f'Nenhuma tarefa {status_text}.')
    for item in sorted(filtered_tarefas, key=lambda x: (x["prioridade"], datetime.strptime(x["data_vencimento"], '%d/%m/%Y'))):
        print(f'{item["tarefa"]} - Prioridade: {item["prioridade"]} - Data de vencimento: {item["data_vencimento"]}')

# Função para salvar tarefas em um arquivo
def salvarTarefas():
    with open('tarefas.json', 'w') as file:
        json.dump(tarefas, file)
    print("Tarefas salvas com sucesso.")

# Função para carregar tarefas de um arquivo
def carregarTarefas():
    global tarefas
    try:
        with open('tarefas.json', 'r') as file:
            tarefas = json.load(file)
        print("Tarefas carregadas com sucesso.")
    except FileNotFoundError:
        print("Nenhum arquivo de tarefas encontrado.")

# Menu interativo
def menu():
    carregarTarefas()
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Marcar Tarefa como Concluída")
        print("4. Listar Todas as Tarefas")
        print("5. Listar Tarefas Concluídas")
        print("6. Listar Tarefas Não Concluídas")
        print("7. Salvar Tarefas")
        print("8. Sair")
        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:
            tarefa = input("Digite o nome da tarefa para adicionar: ")
            prioridade = input("Digite a prioridade da tarefa (alta, média, baixa): ")
            data_vencimento = input("Digite a data de vencimento da tarefa (dd/mm/aaaa): ")
            adicionarTarefa(tarefa, prioridade, data_vencimento)
        elif opcao == 2:
            tarefa = input("Digite o nome da tarefa para remover: ")
            removerTarefa(tarefa)
        elif opcao == 3:
            tarefa = input("Digite o nome da tarefa para marcar como concluída: ")
            concluirTarefa(tarefa)
        elif opcao == 4:
            listarTarefas()
        elif opcao == 5:
            listarTarefaPorStatus(concluida=True)
        elif opcao == 6:
            listarTarefaPorStatus(concluida=False)
        elif opcao == 7:
            salvarTarefas()
        elif opcao == 8:
            print("Saindo...")
            salvarTarefas()
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
