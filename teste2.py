
lista = []
with open('./inputusuario.txt', 'r') as f:
    for linha in f: 
        lista.append(linha.strip())

print(lista)