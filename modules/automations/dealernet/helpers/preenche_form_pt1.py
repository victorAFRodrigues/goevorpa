from time import sleep

from selenium.webdriver.support.select import Select

from modules.utils.browser_automation import SeleniumElement

def run(data, driver):
    SE = SeleniumElement

    def click(by, value):
        SE(driver, by, value).action("click")

    def write(by, value, text):
        SE(driver, by, value).action("write", text)

    try:
        # grupo de movimento:
        Select(
            SE(driver, "css", 'select[id="vNOTAFISCAL_GRUPOMOVIMENTO"]').find()
        ).select_by_value("COM")

        # natureza de operação:
        click("xpath", '//*[@id="NATOPE"]')
        natureza_operacao = str(int(data["natureza_operacao"]))
        Select(
            SE(driver, "css", '#vNOTAFISCAL_NATUREZAOPERACAOCOD').find()
        ).select_by_value(natureza_operacao)

        click("xpath", '//*[@id="CONFIRMAR"]')

        # reseta o contexto de visualização do selenium
        driver.switch_to.default_content()

        # tipo de pessoa:
        Select(
            SE(driver, "css", 'select[id="vPESSOA_TIPOPESSOA"]').find()
        ).select_by_value("J")

        # tipo de documento:
        click("xpath", '//*[@id="TIPODOC"]')
        Select(
            SE(driver, "css", 'select[id="vNOTAFISCAL_TIPODOCUMENTOCOD"]').find()
        ).select_by_value(data["tipo_documento"] )

        click("xpath", '//*[@id="CONFIRMAR"]')

        # reseta o contexto de visualização do selenium
        driver.switch_to.default_content()
        
        # demais campos:
        write("css", 'input[id="vNOTAFISCAL_CONTAGERENCIALCOD"]', data['conta_gerencial'] )

        print(data['rateio'][0]["departamento"])
        driver.switch_to.default_content()

        Select(
            SE(driver, "css", 'select[id="vNOTAFISCAL_DEPARTAMENTOCOD"]').find()
        ).select_by_value(data['rateio'][0]["departamento"])
        # click("xpath", f'//option[normalize-space()="{ data["departamento"] }"]')

        Select(
            SE(driver, "css", 'select[id="vNOTAFISCAL_CONDICAOPAGAMENTOCOD"]').find()
        ).select_by_value(data["condicao_pagamento"])
        # click("css", f'select[id="vNOTAFISCAL_CONDICAOPAGAMENTOCOD"] option[value="36"]')
        # click("css", f'select[id="vAGENTECOBRADOR_CODIGO"] option[value="10"]')
        Select(
            SE(driver, "css", 'select[id="vAGENTECOBRADOR_CODIGO"]').find()
        ).select_by_value('10')

        click("xpath", '//*[@id="vISUTILIZAREGRATRIBUTOICMSPISCOFINS"]')   
        click("xpath", '//*[@id="IMGPROCESSAR"]')
        sleep(4)
        err = SE(driver, 'xpath', '//*[@id="gxErrorViewer"]/div[1]', timeout=10).find_error_msg()
       
        err_msg = err.get_property('innerHTML').strip()

        if err_msg == 'Nota Fiscal Processada com Sucesso':
            print('Primeira parte do formulário de preenchimento da nota concluído!')
            return True
        
    except Exception as e:
            raise Exception(f"Não foi possivel preencher o formulário, erro: {e}")