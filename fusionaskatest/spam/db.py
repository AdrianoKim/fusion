from time import sleep


class Sessao:
    contador = 0
    usuarios = []
    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def listar(self):
        return self.usuarios

    def roll_back(self):
        self.usuarios.clear()

    def fechar(self):
        pass


class Conexao:

    def __init__(self):
        sleep(1) #função que insere um tempo em segundos para executar a conexao com o banco de dados

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass


class Usuario:
    def __init__(self, nome, email):
        self.email = email
        self.id = None
        self.nome = nome