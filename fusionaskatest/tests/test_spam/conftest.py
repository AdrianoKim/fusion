import pytest as pytest

from fusionaskatest.spam.db import Conexao


@pytest.fixture
def conexao():
    # Setup da conexao
    conexao_obj = Conexao()
    yield conexao_obj  # yield so pode ser usado dentro de uma função, funciona como um return mas retorna um generator
    # yield retorna o valor que será injetado nos testes
    # essa parte apos o yield executa a etapa de tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # Setup da sessao
    sessao_obj = conexao.gerar_sessao()  # criar uma sessao a partir da conexao
    yield sessao_obj
    # inicio do tear down
    sessao_obj.roll_back()
    sessao_obj.fechar()