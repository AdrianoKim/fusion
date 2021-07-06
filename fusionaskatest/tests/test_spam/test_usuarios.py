from fusionaskatest.spam.db import Usuario


# após as fixtures estão os testes

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Aska')  # salvar o usuario (obs: e possivel salvar mais de um usuario)
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Aska'),
                Usuario(nome='Adriano')]  # salvar o usuario (obs: e possivel salvar mais de um usuario)
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
