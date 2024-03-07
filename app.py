import streamlit as st
import os
import requests
import time 
from api_keys import YOUR_API_KEY
from gemini import generate_history

def main():
    st.title("Criacom.AI")
    st.write("criatividade e acessibilidade (shoraste?)!")
    # Caixa de texto
    _input = st.text_input("descrição da imagem:")
    with open('inputusuario.txt', 'w') as f:
            f.write(_input)
    
    if _input:
        generate_history()
        
    count_paragrafo = 1
    if st.button("Gerar imagens"):
        
        with open('./historia_gemini.txt', 'r') as historia:
            for paragrafo in historia:
                TEXT_PROMPT = paragrafo.strip()
                
                if paragrafo.strip() != '':

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
                    time.sleep(0.05)
            

    #Diretório onde a imagem está localizada
    image_dir = "images"
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    #on = st.toggle('exibir imagens geradas')

    #show_images = st.checkbox('Exibir imagens')

    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        st.image(image_path, caption=image_file, use_column_width=True)
    if st.button('exibir história'):
        with open('./historia_gemini.txt', 'r') as hist:
            st.write(hist.read())

if __name__ == "__main__":
    main()
