import streamlit as st
import os
import requests

def main():
    st.title("Criacom.AI")
    st.write("criatividade e acessibilidade (shoraste?)!")
    # Caixa de texto
    _input = st.text_input("descrição da imagem:")
    with open('inputusuario.txt', 'w') as f:
            f.write(_input)

    if st.button("Submeter"):
        
        with open('inputusuario.txt', 'r') as f:
            text = f.read()
    
        TEXT_PROMPT = text
        YOUR_API_KEY = ''


        r = requests.post('https://clipdrop-api.co/text-to-image/v1',
        files = {
        'prompt': (None, TEXT_PROMPT, 'text/plain')
        },
        headers = { 'x-api-key': YOUR_API_KEY}
        )

        if (r.ok):
            with open('./images/image.jpg', 'wb') as f:
                f.write(r.content)
            print("Imagem salva com sucesso!")
        else:
            r.raise_for_status()

    #Diretório onde a imagem está localizada
    image_dir = "images"
    image_files = os.listdir(image_dir)

    if image_files:
        selected_image = image_files[0]
        image_path = os.path.join(image_dir, selected_image)

        on = st.toggle('exibir imagem')

        if on:
            st.image(image_path, caption=" generated image", use_column_width=True)
    else:
        st.write("Nenhuma imagem encontrada na pasta 'imagens'.")


if __name__ == "__main__":
    
    main()
