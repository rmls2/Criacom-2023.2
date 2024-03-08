import streamlit as st
import os
import requests
import time 
from api_keys import YOUR_API_KEY
from gemini import generate_history


descricao_paragrafo = []

def main():
    st.title("Criacom.AI")
    st.write("criatividade e acessibilidade (shoraste?)!")
    # Caixa de texto
    _input = st.text_input("escreva a história que deseja gerar:")
    with open('inputusuario.txt', 'w') as f:
            f.write(_input)
    
    if _input:
        generate_history()
        
        count_paragrafo = 1        
        with open('./historia_gemini.txt', 'r') as historia:
            for paragrafo in historia:
                TEXT_PROMPT = paragrafo.strip()

                if paragrafo.strip() != '':

                    descricao_paragrafo.append(paragrafo.strip())
                    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
                    files = {
                    'prompt': (None, TEXT_PROMPT, 'text/plain')
                    },
                    headers = { 'x-api-key': YOUR_API_KEY}
                    )

                    if (r.ok):
                        with open(f'./images/image_{count_paragrafo}.jpg', 'wb') as f:
                            f.write(r.content)
                        print("Imagem salva com sucesso!")
                        count_paragrafo+=1
                    else:
                        r.raise_for_status()
                

        #Diretório onde a imagem está localizada
        #image_dir = "images"
        #image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Paragrafo 1")
            st.image("./images/image_1.jpg")
            st.write(descricao_paragrafo[0])
        with col2:
            st.header("Paragrafo 2")
            st.image("./images/image_2.jpg")
            st.write(descricao_paragrafo[1])

        with col3:
            st.header("Paragrafo 3")
            st.image("./images/image_3.jpg")
            st.write(descricao_paragrafo[2])


if __name__ == "__main__":
    main()
