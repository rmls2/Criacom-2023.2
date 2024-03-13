import textwrap
from api_keys import GOOGLE_API_KEY
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def generate_history(GOOGLE_API_KEY, qtd_imagens):

    genai.configure(api_key=GOOGLE_API_KEY)

    """ for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name) """

    model = genai.GenerativeModel('gemini-pro')

    with open('./inputusuario.txt', 'r') as input_:
        TEXT = input_.read()

    POSPROMPT = f"""Esta história precisa ser contada em {qtd_imagens} parágrafos. Em cada parágrafo mencione o personagem principal,
     descreva quem ele é e descreva o ambiente em que está localizado. 
     É essencial que a história seja coesa e coerente."""
    TEX_PROMPT = TEXT + POSPROMPT
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


