from selenium.webdriver.support.select import Select

from modules.utils.browser_automation import SeleniumElement
from selenium.common.exceptions import NoSuchElementException
from time import sleep



def run(driver, data):
    SE = SeleniumElement

    def click(by, value):
        SE(driver, by, value).action("click")

    def write(by, value, text):
        SE(driver, by, value).action("write", text)


    try:
        if len(data['rateio']) <= 1:
            return True

        click("xpath", '//*[@id="RATEIO"]')

        SE(driver, "xpath", '//*[@id="IMGINSERT"]', timeout=8).action("click")

        sleep(2)

        n = 0

        rateio = data["rateio"]

        for rateio_i in rateio:

            # preenche os campos do rateio
            # click("css", f'select[id="vNOTAFISCALRATEIODEP_EMPRESACOD"] option[value="'+rateio_i['empresa']+'"]')
            Select(
                SE(driver, "css", 'select[id="vNOTAFISCALRATEIODEP_EMPRESACOD"]').find()
            ).select_by_value(rateio_i['empresa'])

            Select(
                SE(driver, "css", 'select[id="vNOTAFISCALRATEIODEP_DEPARTAMENTOCOD"]').find()
            ).select_by_value(rateio_i['departamento'])

            Select(
                SE(driver, "css", 'select[id="vCONTAGERENCIAL_CODIGO"]').find()
            ).select_by_value(rateio_i['conta_gerencial'])

            # click("css", f'select[id="vNOTAFISCALRATEIODEP_DEPARTAMENTOCOD"] option[value="'+rateio_i['departamento']+'"]')
            # click("css", f'select[id="vCONTAGERENCIAL_CODIGO"] option[value="'+rateio_i['conta_gerencial']+'"]')
            write("xpath", '//*[@id="vNOTAFISCALRATEIODEP_VALOR"]', rateio_i['valor'])
            click("xpath", '//*[@id="CONFIRMAR"]')

            # verfica se há mais de um item para cadastrar no rateio
            if len(rateio) > 1 and n < len(rateio) -1:
                n += 1
                SE(driver, "xpath", '//*[@id="IMGINSERT"]', timeout=8).action("click")
                print('rodando processo de cadastro de item no rateio novamente...')

        driver.switch_to.default_content()
        click("xpath", '//*[@id="FECHAR"]')
        print('rateio cadastrado com sucesso!')
            
    except NoSuchElementException:
        print("Estrutura da tabela não encontrada ou alterada.")
        return False

    