from utils import load_data, load_template, build_response
from urllib.parse import unquote_plus
import json


def add_annotation(dic_annotation):
    with open('data/notes.json', 'r') as file:
        list_of_dicts = json.load(file)

    with open('data/notes.json', 'w') as file:
        list_of_dicts.append(dic_annotation)
        json.dump(list_of_dicts, file, ensure_ascii=False, indent=4)


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            split = chave_valor.split('=')
            key = unquote_plus(split[0])
            value = unquote_plus(split[1])
            params[key] = value

        add_annotation(params)
        # return build_response(code='303',reason='See Other', headers='Location: /')
        # return 'HTTP/1.1 303 See Other Location: /\n\nHello World'

        # Cria uma lista de <li>'s para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes).encode()
