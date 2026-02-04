from datetime import datetime
from modules.utils.browser_automation import SeleniumElement

def run(driver, data):
    # Define variaveis importantes no inicio da execução
    today = datetime.now()
    year, month, day = today.year, today.month, today.day
    date = f'{day:02d}{month:02d}{year:04d}'

    SE = SeleniumElement

    def click(by, value):
        SE(driver, by, value).action("click")

    def write(by, value, text):
        SE(driver, by, value).action("write", text)
        

    try: 
        driver.switch_to.default_content() 
        SE(driver, "xpath", '//*[@id="vNOTAFISCAL_NUMERO"]', 5).find()
        write("xpath", '//*[@id="vNOTAFISCAL_DATACHEGADA"]', date)
        write("xpath", '//*[@id="vNOTAFISCAL_DATAMOVIMENTO"]', date)

        # preenche condição de pagamento e agente cobrador
        click("css", 'select[id="vNOTAFISCAL_CONDICAOPAGAMENTOCOD"] option[value="'+data["condicao_pagamento"]+'"]')
        driver.switch_to.default_content()
        click("css", 'select[id="vAGENTECOBRADOR_CODIGO"] option[value="10"]')

        # preenche os demais campos da capa da nota
        driver.switch_to.parent_frame()
        # write("xpath", '//*[@id="vNOTAFISCAL_OBSERVACAO"]', data['observacao'])
        driver.switch_to.default_content() 

        if data['codigo_verificacao'] != '':
            try:
                write("xpath", '//*[@id="vNOTAFISCAL_CHAVENFE"]', data['codigo_verificacao'])
            except:
                pass
            driver.switch_to.default_content()

        print("Capa da nota preenchida com sucesso!")
        return True
        
    except Exception as e:
        raise Exception(f"Não foi possivel preencher a capa da nota, erro: {e}")
