from fusionaskatest.spam.enviador_de_email import Enviador
from fusionaskatest.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao=None):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'aska_vic@hotmail.com', # remetente
        'Curso Python Pro',     # assunto do e-mail
        'Aprendendo com o curso', # corpo do e-mail
    )

