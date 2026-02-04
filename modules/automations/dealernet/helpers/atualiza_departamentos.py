from modules.core.database import Database


def run(departamento_html):

    #trata os dados do html para inserir na tabela

    db = Database() # instancia a classe do banco de dados


    db.close() # fecha conexão com banco