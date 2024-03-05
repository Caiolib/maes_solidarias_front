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
    url = 'http://127.0.0.1:8000/bazar/items/'
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

#eventos



# Função para criar um novo evento
def criar_evento(data):
    url = 'http://127.0.0.1:8000/events/'  
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Função para obter todos os eventos
def obter_eventos():
    url = 'http://127.0.0.1:8000/events/'  
    response = requests.get(url)
    return response.json()

# Função para obter um evento único pelo ID
def obter_evento_unico(id):
    url = f'http://127.0.0.1:8000/events/unique/{id}'  
    response = requests.get(url)
    return response.json()

# Função para deletar um evento
def deletar_evento(id):
    url = f'http://127.0.0.1:8000/events/unique/{id}'  
    response = requests.delete(url)
    return response.json()

# Função para atualizar um evento
def atualizar_evento(id, data):
    url = f'http://127.0.0.1:8000/events/unique/{id}'  
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, json=data, headers=headers)
    return response.json()

# Funçoes para usuario

def cadastrar_usuario(data):
    response = requests.post('http://127.0.0.1:8000/usuario/', json=data)
    return response.json(), response.status_code

def deletar_usuario(user_id):
    data = {'user': user_id}
    response = requests.delete('http://127.0.0.1:8000/usuario/', json=data)
    return response.json(), response.status_code

def atualizar_usuario(user_id, update_data):
    data = {'user': user_id}
    data.update(update_data)
    response = requests.put('http://127.0.0.1:8000/usuario/', json=data)
    return response.json(), response.status_code

def listar_usuarios():
    response = requests.get('http://127.0.0.1:8000/usuario/')
    return response.json(), response.status_code