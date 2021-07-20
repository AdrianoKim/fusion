from unittest.mock import Mock

import pytest as pytest

from fusionaskatest.spam.db import Usuario
from fusionaskatest.spam.main import EnviadorDeSpam


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Aska', email='aska_vic@hotmail.com'),
            Usuario(nome='Adriano', email='kimzera@hotmail.com')
        ],
        [
            Usuario(nome='Aska', email='aska_vic@hotmail.com')
        ]

    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'aska_vic@hotmail.com',  # remetente
        'Curso Python Pro',  # assunto
        'Aprendendo com o curso',  # corpo do e-mail
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Aska', email='aska_vic@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'kimzera@hotmail.com',  # remetente
        'Curso Python Pro',  # assunto
        'Aprendendo com o curso',  # corpo do e-mail
    )
    enviador.enviar.assert_called_once_with (
        'kimzera@hotmail.com',  # remetente
        'aska_vic@hotmail.com',  # destinatario
        'Curso Python Pro',  # assunto
        'Aprendendo com o curso',  # corpo do e-mail

    )
