import requests

YOUR_API_KEY = ''
TEXT_PROMPT = """make the following story in comic style and without any text bubbles: 
Defying the rules and traditions of his kingdom, the Dark Prince embarked on a journey to understand the outside world. He learned about love, compassion, and the nuances of life beyond the walls of his kingdom. He gradually discovered that true strength is not in domination over others, but in mutual understanding and acceptance."""



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

