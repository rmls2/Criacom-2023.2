# Criacom-2023.2
projeto final da disciplina de Criatividade computacional do período 2023.2 



## Ativar e rodar o ambiente virtual 

```
python3 -m venv .venv
```
ativando o ambiente virtual no Windows

```
.venv\Scripts\Activate
```

no windows ao ativar o ambiente virtual vc verá uma pequena diferença no terminal (.venv), isso indicará que o ambiente está ativado.

![image](https://github.com/Bruno0205/MultimidiaMashup/assets/104790677/7cce9a61-4c15-45f3-8e4c-8f8f56b5ac90)

 No linux para ativar o ambiente virtual se usa: 

```
source .venv/bin/activate
```

## instalar as dependencias 

dentro do ambiente virtual instale as dependencias projeto

```
pip install -r requirements.txt  

```

## rode o projeto 

dentro do ambiente virtual coloque o comando: 

```
streamlit run app.py
```

o servidor stramlit será iniciado o projeto rodará localmente. Ao acessar o link da aplicação, uma tela parecida com essa será exibida para você.


![image](https://github.com/rmls2/Criacom-2023.2/assets/93690581/c3f87d6f-42d9-4318-962c-75bf871fd74d)


## API keys 

no campo de API, você precisará gerar suas chaves. Abaixo está os sites dos modelos e lá você irá encontrar formas de gerar suas chaves.
a API do clipdrop (gerador de imagem) disponibiliza 100 créditos (1 por imagem) gratuitamente e API do Gemini é ilimitada. 

* https://clipdrop.co/apis/
* https://aistudio.google.com/app/apikey
* https://ai.google.dev/tutorials/python_quickstart
