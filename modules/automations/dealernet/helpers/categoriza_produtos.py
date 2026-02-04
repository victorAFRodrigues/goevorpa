from random import uniform, randint
from modules.utils.browser_automation import SeleniumElement
from time import sleep



def run(driver, data):
    # procura na tabela o elemento com o nome do arquivo da nota e clica na opção de atualizar os itens da nota
    SE = SeleniumElement

    def hclick(by, value):
        el = SE(driver, by, value)
        for i in range(randint(3,4)):
            el.action("click")
            sleep(uniform(0.05, 0.07))

    try:
        
        SE(driver, 'xpath', '//*[@id="vITEMAVULSO_CODIGO"]', timeout=5).action('write', '5')
        # SE(driver, 'xpath', '//*[@id="vITEMAVULSO_CODIGO"]', timeout=5).action('write', Json(data).get('CATEGORIA_ITEMS'))
        SE(driver, 'xpath', '//*[@id="CONFIRM"]', timeout=10).action('click')
        # hclick('xpath', '//*[@id="BTNCONFIRMAR"]')

        try:
            hclick('xpath', '//*[@id="BTNCONFIRMAR"]')
        except:
            SE(driver, 'xpath', '//*[@id="BTNCONFIRMAR"]', timeout=10).action('click')
            pass

        sleep(5)
        SE(driver, 'xpath', '//*[@id="BTNPROCESSAR"]', timeout=10).action('click')
        # Aguarda um tempo maior para identificar o botão processar
        # SE(driver, 'xpath', '//*[@id="BTNPROCESSAR"]', timeout=10).action('click')
        print('Categorização dos produtos da nota concluído!')

        return True
    
    except Exception as e:
        raise Exception(f"Erro ao categorizar os produtos da nota, erro: {e}")