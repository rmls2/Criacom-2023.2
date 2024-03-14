import os

def criar_pasta_e_arquivos():
    # Nome da pasta a ser criada
    nome_pasta = "nome_da_pasta_que_deseja_criar"
    
    # Verifica se a pasta já existe
    if not os.path.exists(nome_pasta):
        # Cria a pasta
        os.makedirs(nome_pasta)
        print(f'Pasta "{nome_pasta}" criada com sucesso!')
    else:
      print(f'A pasta "{nome_pasta}" já existe!')
    # Cria os arquivos de texto vazios
    with open(os.path.join(nome_pasta, 'historia_gemini.txt'), 'w') as arquivo_gemini:
        pass  # Nada é escrito no arquivo, então ele permanece vazio
    with open(os.path.join(nome_pasta, 'historia_traduzida.txt'), 'w') as arquivo_traduzida:
        pass  # Nada é escrito no arquivo, então ele permanece vazio
        
    print('Arquivos de texto criados com sucesso!')


# Chama a função para criar a pasta e os arquivos