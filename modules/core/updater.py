from modules.core.api import Api
from modules.utils.general import DotEnv
from modules.core.logger import setup_logger

class EnvUpdate:
    def __init__(self):
        self.api = Api()
        self.env = DotEnv()
        self.logger = setup_logger("EnvUpdate")
        
    def __enter__(self):
        self.logger.info("Iniciando EnvUpdate...")

        self.logger.info("Realizando busca de variaveis dinamicas do GOEVO...")

        APP_DATA = self.api.getVariables('?Grupolelacteste/RPAManager/AtualizarVariaveis')

        self.logger.info("Busca Realizada com sucesso! Atualizando variaveis de ambiente...")

        for key, value in {
            "SEARCH_TIMEOUT": APP_DATA['searchTimeout'],
            "APPLICATION":  APP_DATA['application']['system'],
            "SYSTEM_URL":  APP_DATA['application']['systemUrl'],
            "USER":  APP_DATA['application']['user'],
            "PASSWORD":  APP_DATA['application']['password'],
        }.items():
            self.env.set(key, value)

        self.logger.success('Variaveis atualizadas com sucesso!')

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == "__main__":
    # Rodar como modulo  
    # Command: & C:/Projetos/goevo_rpa/.venv/Scripts/python.exe -m modules.core.updater
    with EnvUpdate():
        pass

    