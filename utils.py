import os
import json


def extract_route(request):
    route = request.split()[1][1:]
    return route


def read_file(path):
    extension = os.path.splitext(path)[1]
    format_text = ['.txt', '.html', '.css', '.js']
    if extension in format_text:
        with open(path, 'rt') as file:
            return file.read()

    with open(path, 'rb') as file:
        return file.read()


def load_data(json_path):
    with open('data/' + json_path) as json_file:
        data = json.load(json_file)
        return data


def load_template(template_file):
    return read_file('templates/' + template_file)


def build_response(body='HTTP/1.1', code='200', reason='OK', headers=''):
    response = [body, str(code), reason, headers]
    response = (' '.join(response)) + '\n\n'
    return response.encode()
