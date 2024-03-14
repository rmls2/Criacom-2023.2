import streamlit as st
import os
import requests
import time 
import time
from elevenlabs import play, save
from elevenlabs.client import ElevenLabs
import google.generativeai as genai

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

    user_input = _input
    submit_button = st.button('submeter história') 

    if submit_button:

        generate_history(gemini_key, qtd_imagens, user_input)
        translate_history(gemini_key)

        count_paragrafo = 1        
        with open('./historia_traduzida.txt', 'r') as historia:
            for paragrafo in historia:
                TEXT_PROMPT = paragrafo.strip()
                t = translate_inputs(estilo=estilo, personagem=descricao_personagem_principal, api_key=gemini_key)
                PRE_PROMPT = f'generate an image about {t[1]} in the {t[0]} style and use the following scenario as a basis: '
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
        audio_files = list_audio_files('./audios_elevenlabs')

        for i in range(len(descricao_paragrafos)):
            st.subheader(f"parte {i+1}")
            st.image(f"./images/image_{i+1}.jpg")
            st.write(descricao_paragrafos[i])
            if len(audio_files) != len(descricao_paragrafos):
              pass
            else:
                audio_path = os.path.join('./audios_elevenlabs', audio_files[i])
                audio_bytes = open(audio_path, "rb").read()
                st.audio(audio_bytes, format='audio/mp3')                

def ler_descricoes_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            descricao_paragrafos = [linha.strip() for linha in arquivo.readlines() if linha.strip()]

        return descricao_paragrafos
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return None

def create_voice_for_text_to_voice(x: list):
    for i in x:
        client = ElevenLabs(api_key="f5fd5ed78d745f4ab6ca714fc4546a79")

        audio = client.generate(
        text= x[i],
        voice="Rachel",
        model="eleven_multilingual_v2"
        )

        # Converta o gerador em bytes concatenando-o
        audio_bytes = b"".join(audio)

        #play(audio_bytes)
        save(audio_bytes, './audios_elevenlabs/part_' + str(x.index(i)) + '.mp3')

def list_audio_files(folder_path):
    audio_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3") or file.endswith(".wav")]
    return audio_files

def generate_history(GOOGLE_API_KEY, qtd_imagens, user_input):

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    POSPROMPT = f"""Esta história precisa ser contada em {qtd_imagens} parágrafos e cada parágrafo precisa ter no máximo 100 caracteres. 
                    É essencial que a história seja coesa e coerente."""
    TEX_PROMPT = user_input + POSPROMPT
    response = model.generate_content(TEX_PROMPT)
    #print(response.text)

    with open('./historia_gemini.txt', 'w') as f:
        f.write(response.text)

    return


def translate_history(GOOGLE_API_KEY):

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    with open('./historia_gemini.txt', 'r') as history:
        TEXT = history.read()

        response = model.generate_content(f'traduza para o inglês o seguinte texto: {TEXT}')

    with open('./historia_traduzida.txt', 'w') as f:
        f.write(response.text)
    return 


def translate_inputs(estilo, personagem, api_key):
    l = []
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(f'traduza para o inglês as seguintes palavras: {estilo}\n{personagem}')

    l = response.text.split('\n')
    l2 = list(map(str.lower, l))
    
    return l2

if __name__ == "__main__":
    main()
   
    


  


