import requests


def buscar_avatar(usuario):
    """
    Busca avatar de um usuário do githu

    :param usuario: str com o nome do usuário no github
    :return: str com o link do avatar

    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('AskaVictoria'))