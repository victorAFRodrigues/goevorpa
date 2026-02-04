from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from modules.utils.browser_automation import SeleniumElement
from time import sleep

def run(driver, data):
    SE = SeleniumElement

    def click(by, value):
        SE(driver, by, value).action("click")


    try:
        parcelas = data["parcelas"]

        if(len(parcelas) < 2):
            return True

        click("xpath", '//*[@id="PARCELA"]')
        click("xpath", '//*[@id="INSERT"]')

        i = 0

        for parcela in parcelas:
            sleep(1)
            print(f"Preenchendo parcela {i + 1} de {len(parcelas)}")

            
            # encontra as linhas da tabela de parcelas
            rows = SE(driver, "xpath", '//*[@id="GridparcelaContainerTbl"]/tbody/tr', 20).find_many() # SE(table, "css", 'tr').find_many()
              
            # preenche os campos da parcela
            SE(rows[i], "css", 'td[colindex="17"] div input').action("write", parcela['data_vencimento'])
            SE(rows[i], "css", 'td[colindex="19"] input').action("write", parcela['valor'])
            Select(SE(rows[i], "css", 'td[colindex="20"] select').find()).select_by_value(parcela['tipo_titulo'])

            # SE(rows[i], "css", 'td[colindex="20"] select option[value="'+parcela['tipo_titulo']+'"]').action("click")


            # verfica se há mais de uma parcela para cadastrar
            if len(parcelas) > 1 and i < len(parcelas) - 1:
                i += 1

                # clica para inserir uma nova parcela
                click("xpath", '//*[@id="INSERT"]')
                print('rodando processo de cadastro de parcelas novamente...')
                
        click("xpath", '//*[@id="BTNCONFIRMAR"]')
        print('parcelas cadastradas com sucesso!')
        return True

    except NoSuchElementException:
        print("Estrutura da tabela não encontrada ou alterada.")
        return False
    

    
