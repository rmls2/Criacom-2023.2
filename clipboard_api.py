import requests

YOUR_API_KEY = '1a0dedf4a23ed1c317f26d256369383a75ddb850aa923fd67d0cfd36751b2ea62d6575828c5d3abcacab570e0cbeda95'
PRE_TEXT = "make the following story in comic style and without any text bubbles"
TEXT_PROMPT = '<prompt do outro script>'



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

