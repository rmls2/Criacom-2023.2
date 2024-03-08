import textwrap
from api_keys import GOOGLE_API_KEY
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def generate_history():

    genai.configure(api_key=GOOGLE_API_KEY)

    """ for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name) """

    model = genai.GenerativeModel('gemini-pro')

    with open('./inputusuario.txt', 'r') as input_:
        TEXT_PROMPT = input_.read()

    X = 'Crie essa história usando três parágrafo. Para cada parágrafo descreva quem é o personagem principal e qual sua característica físicas principal e as característica do ambiente em que ele está inserido.'
    y = TEXT_PROMPT + X
    response = model.generate_content(y)
    #print(response.text)

    with open('./historia_gemini.txt', 'w') as f:
        f.write(response.text)

    return

generate_history() 

