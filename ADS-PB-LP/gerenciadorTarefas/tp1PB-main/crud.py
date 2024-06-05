from util import *
def adicionarTarefa(tarefas):
    titulo = receberNomeTarefa()
    descricao = receberDescricaotarefa()
    data_dermino = receberDataTermino()
    tarefas.append([titulo, descricao, data_dermino])

def atualizarTarefa(tarefas):
    if not tarefas:
        print('Não existe tarefa')
        return
    id_tarefa = receberIdTarefa(tarefas)
    tarefas[id_tarefa].append('status: Concluído')
    print(f'\n\n{tarefas}\n\n')

def excluirTarefa(tarefas):
    if not tarefas:
        print('Não existe tarefa')
        return
    id_tarefa = receberIdTarefa(tarefas)
    del(tarefas[id_tarefa])
    print(f'\n\n{tarefas}\n\n')

def listarTarefas(tarefas):
    if not tarefas:
        print('Não existe tarefa')
        return
    for i in range(1,len(tarefas)):
        if len(tarefas[i]) < 4:
            print(f'\t\t\t\tTarefas pendentes\n\n{i}. {tarefas[i]}\n\n')


