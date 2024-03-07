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

    response = model.generate_content(TEXT_PROMPT)
    #print(response.text)

    with open('./historia_gemini.txt', 'w') as f:
        f.write(response.text)

    return f
