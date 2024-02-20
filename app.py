import streamlit as st
import os
import requests
import time 

def main():
    st.title("Criacom.AI")
    
    # Mensagem de boas-vindas
    st.write("Bem-vindo, usuário!")
    
    # Caixa de texto
    _input = st.text_input("Digite algo aqui:")

    if st.button("Submeter"):

        with open('inputusuario.txt', 'w') as f:
            f.write(_input)
        with open('inputusuario.txt', 'r') as f:
            text = f.read()
    

        TEXT_PROMPT = text
        YOUR_API_KEY = '1a0dedf4a23ed1c317f26d256369383a75ddb850aa923fd67d0cfd36751b2ea62d6575828c5d3abcacab570e0cbeda95'


        r = requests.post('https://clipdrop-api.co/text-to-image/v1',
        files = {
        'prompt': (None, TEXT_PROMPT, 'text/plain')
        },
        headers = { 'x-api-key': YOUR_API_KEY}
        )


        if (r.ok):
            # Salva a imagem retornada
            with open('./images/image.jpg', 'wb') as f:
                f.write(r.content)
            print("Imagem salva com sucesso!")
        else:
            r.raise_for_status()

# Diretório onde a imagem está localizada
    image_dir = "images"
    image_files = os.listdir(image_dir)

    if image_files:
        selected_image = image_files[0]
        image_path = os.path.join(image_dir, selected_image)
        st.image(image_path, caption="Imagem selecionada", use_column_width=True)
    else:
        st.write("Nenhuma imagem encontrada na pasta 'imagens'.")


if __name__ == "__main__":
    
    main()
