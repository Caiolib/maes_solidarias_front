import requests

#Rotas Categoria
def criar_categoria(nome):
    url = 'http://127.0.0.1:8000/bazar/categoria/'
    headers = {'Content-Type': 'application/json'}
    data = {'nome': nome}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def listar_categorias():
    url = 'http://127.0.0.1:8000/bazar/categoria/'
    response = requests.get(url)
    return response.json()

def remover_categoria(id):
    url = f'http://127.0.0.1:8000/bazar/categoria/{id}/'
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url, headers=headers) 
    return response.json()


#Rotas Produto
def criar_produto(nome, descricao, preco, estoque, total_vendido, categoria):
    url = 'http://seu-endereco-django.com/items/'
    headers = {'Content-Type': 'application/json'}
    data = {
        'nome': nome,
        'descricao': descricao,
        'preco': preco,
        'estoque': estoque,
        'total_vendido': total_vendido,
        'categoria': categoria
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def listar_produtos():
    url = 'http://127.0.0.1:8000/bazar/items/'
    response = requests.get(url)
    return response.json()

def atualizar_produto(nome, novo_nome=None, descricao=None, preco=None, estoque=None, total_vendido=None, categoria=None):
    url = 'http://127.0.0.1:8000/bazar/items/'
    headers = {'Content-Type': 'application/json'}
    data = {
        'nome': nome,
        'novo_nome': novo_nome,
        'descricao': descricao,
        'preco': preco,
        'estoque': estoque,
        'total_vendido': total_vendido,
        'categoria': categoria
    }
    response = requests.put(url, json=data, headers=headers)
    return response.json()

def remover_produto(id):
    url = f'http://127.0.0.1:8000/bazar/items/{id}/'  
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url, headers=headers)
    return response.json()