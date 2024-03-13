import streamlit as st
import os
import requests
import time 
from api_keys import YOUR_API_KEY
from gemini import generate_history, translate_history
import time

descricao_paragrafo = []
qtd_imagens = 0

def main():  

    # Using "with" notation
    with st.sidebar:
        st.header("Chaves das API's")
        clipdrop_key = st.text_input('Chave da API Clipdrop', type="password")
        gemini_key = st.text_input('Chave da API GEMINI', type="password")
        prompt_clip = clipdrop_key
        st.header("Imagens e estilos")

        estilo_imagem = st.text_input("Selecione o estilo das imagens que serão geradas. ex: realista, desenho, etc")
        numero_imagens = st.slider("selecione a quantidade de imagens que deseja gerar para a história.", min_value=1, max_value=8, value=0)
        qtd_imagens = numero_imagens
        estilo = estilo_imagem
        
    st.title("TOON CRAFT")
    st.subheader("Dê asas a sua imaginação com o Toon Craft")
    st.write("O criador de histórias usando um único prompt de texto.")
    st.write('')

    # Caixa de texto
    _input = st.text_input("escreva a história que deseja gerar:")
    descricao_personagem = st.text_input("Descreva o que é ou quem é seu personagem principal")
    descricao_personagem_principal = descricao_personagem

    with open('inputusuario.txt', 'w') as f:
            f.write(_input)
    submit_button = st.button('submeter história') 

    if submit_button:

        generate_history(gemini_key, qtd_imagens)
        translate_history(gemini_key)

        count_paragrafo = 1        
        with open('./historia_traduzida.txt', 'r') as historia:
            for paragrafo in historia:
                TEXT_PROMPT = paragrafo.strip()
                ESTILO = estilo
                PERSONAGEM = descricao_personagem_principal
                PRE_PROMPT = f'generate an image about {PERSONAGEM} in the {ESTILO} style and use the following scenario as a basis: '
                PROMPT = PRE_PROMPT + TEXT_PROMPT 
 
                if paragrafo.strip() != '':

                    descricao_paragrafo.append(TEXT_PROMPT)
                    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
                    files = {
                    'prompt': (None, PROMPT, 'text/plain')
                    },
                    headers = { 'x-api-key': prompt_clip}
                    )

                    if (r.ok):
                        with open(f'./images/image_{count_paragrafo}.jpg', 'wb') as f:
                            f.write(r.content)
                        print("Imagem salva com sucesso!")
                        count_paragrafo+=1
                        time.sleep(1)
                    else:
                        r.raise_for_status()

    if st.toggle('exibir história'):
        descricao_paragrafos = ler_descricoes_de_arquivo("./historia_gemini.txt")

        for i in range(1,qtd_imagens+1):
            st.subheader(f"parte {i}")
            st.image(f"./images/image_{i}.jpg")
            st.write(descricao_paragrafos[i-1])                

def ler_descricoes_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            descricao_paragrafos = [linha.strip() for linha in arquivo.readlines() if linha.strip()]

        return descricao_paragrafos
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return None
    

if __name__ == "__main__":
    main()
   
    


  


