import streamlit as st
import os
import requests
import time 
from api_keys import YOUR_API_KEY
from gemini import generate_history, translate_history

descricao_paragrafo = []

def main():  

    # Using "with" notation
    with st.sidebar:
        st.title("Chaves das API's")
        clipdro_key = st.text_input('Chave da API Clipdrop', type="password")
        gemini_key = st.text_input('Chave da API GEMINI', type="password")
        prompt_clip = clipdro_key
        
    st.title("Criacomp_AI")
    st.subheader("Dê asas a sua imaginação com o Criacomp_AI")
    st.write("O criador de histórias usando um único prompt de texto.")

    # Caixa de texto
    _input = st.text_input("escreva a história que deseja gerar:")
    with open('inputusuario.txt', 'w') as f:
            f.write(_input)
    submit_button = st.button('submeter história') 

    if submit_button:

        generate_history(gemini_key)
        translate_history(gemini_key)

        count_paragrafo = 1        
        with open('./historia_traduzida.txt', 'r') as historia:
            for paragrafo in historia:
                TEXT_PROMPT = paragrafo.strip()

                if paragrafo.strip() != '':

                    descricao_paragrafo.append(TEXT_PROMPT)
                    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
                    files = {
                    'prompt': (None, TEXT_PROMPT, 'text/plain')
                    },
                    headers = { 'x-api-key': prompt_clip}
                    )

                    if (r.ok):
                        with open(f'./images/image_{count_paragrafo}.jpg', 'wb') as f:
                            f.write(r.content)
                        print("Imagem salva com sucesso!")
                        count_paragrafo+=1
                    else:
                        r.raise_for_status()
                

def ler_descricoes_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            descricao_paragrafos = [linha.strip() for linha in arquivo.readlines() if linha.strip()]

        return descricao_paragrafos
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return None
    
def exibir_historia():
    if st.toggle('exibir história'):
        descricao_paragrafos = ler_descricoes_de_arquivo("./historia_gemini.txt")

        #col1, col2, col3 = st.columns(3)

        #with col1:
        st.subheader("Paragrafo 1")
        st.image("./images/image_1.jpg")
        st.write(descricao_paragrafos[0])
        #with col2:
        st.subheader("Paragrafo 2")
        st.image("./images/image_2.jpg")
        st.write(descricao_paragrafos[1])

        #with col3:
        st.subheader("Paragrafo 3")
        st.image("./images/image_3.jpg")
        st.write(descricao_paragrafos[2])

if __name__ == "__main__":
    main()
    exibir_historia()
    


  


