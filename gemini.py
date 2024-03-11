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

    X = """This story needs to be told in three paragraphs. Name the main character, 
    describe who he is and describe the environment in which he is located. 
    It is essential that the story is cohesive and coherent."""
    y = TEXT_PROMPT + X
    response = model.generate_content(y)
    #print(response.text)

    with open('./historia_gemini.txt', 'w') as f:
        f.write(response.text)

    return


def translate_history():
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    with open('./historia_gemini.txt', 'r') as history:
        TEXT_PROMPT = history.read()

        response = model.generate_content(f'traduza o seguinte texto: {TEXT_PROMPT}')

    with open('./historia_traduzida.txt', 'w') as f:
        f.write(response.text)
    return 


