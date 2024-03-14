import textwrap
from api_keys import GOOGLE_API_KEY
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def generate_history(GOOGLE_API_KEY, qtd_imagens, user_input):

    genai.configure(api_key=GOOGLE_API_KEY)

    """ for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name) """

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


x = translate_inputs('motocicleta', 'maçã')
print(type(x))
print(x[0])