try:
    with open('config.yaml.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError as ex:
    print(f'Erro ao encontrar arquivo! {ex}')
    with open('configyaml.txt', 'w') as arquivo:
        conteudo_inicial = 'config: default.\n'
        arquivo.write(conteudo_inicial)
        print(f"O arquivo foi criado e o conteúdo inicial foi escrito.")
