import time

def limpar_arquivos_de_texto(*args):
    time.sleep(1)
    try:
        # Abrir o arquivo em modo de escrita ("w") para limpar seu conteúdo
         for aqv in args:
            with open(aqv, "w"):
                  pass  # Não escrever nada, apenas limpar o arquivo
         print("Conteúdos do arquivo foi removido com sucesso.")
    except Exception as e:
        print(f"Erro ao limpar o arquivo: {e}")

# Exemplo de uso:
nome_arquivos = ["./historia_traduzida.txt", "./historia_gemini.txt"]  # Substitua pelo nome do seu arquivo .txt

limpar_arquivos_de_texto(*nome_arquivos)
