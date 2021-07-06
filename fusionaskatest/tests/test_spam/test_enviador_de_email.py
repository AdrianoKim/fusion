import pytest as pytest

from fusionaskatest.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['aska_vic@hotmail.com', 'aska.pereira@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'askakimzera@gmail.com',
        'Testando TDD',
        'Primeiro desenvolvimento de testes.'
    )
    assert remetente in resultado  # quero que o email esteja no texto que apresenta o resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'aska']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
        remetente,
        'askakimzera@gmail.com',
        'Testando TDD',
        'Primeiro desenvolvimento de testes.'
    )