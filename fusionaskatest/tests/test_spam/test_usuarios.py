from fusionaskatest.spam.db import Usuario


# após as fixtures estão os testes

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Aska', email='aska_vic@hotmail.com')  # salvar o usuario (obs: e possivel salvar mais de um usuario)
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Aska', email='aska_vic@hotmail.com'),
        Usuario(nome='Adriano', email='aska_vic@hotmail.com')
    ]  # salvar o usuario (obs: e possivel salvar mais de um usuario)
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
