from datetime import datetime

from modules.automations.dealernet.helpers import atualiza_naturezas_operacao
from modules.core.database import Database
from modules.utils.browser_automation import SeleniumElement
from selenium.webdriver.support.ui import Select


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

    def fill(field, action):
        """
            Executa uma verificação para saber se o preenchimento ocorreu com sucesso, caso não joga
            uma exception personalizada indicando qual campo deu problema.

            Params:
                - **field (str):** Nome do campo que está sendo validado
                - **action (lambda):** Função lambda que será executada dentro do fluxo de validação
        """
        try:
            action()
        except Exception as e:
            raise Exception(f"[{field}] {e.msg}") from e

    try: 
        # insere uma nova nf
        click("xpath", '//*[@id="INSERT"]')

        # reseta o contexto de visualização do selenium
        driver.switch_to.default_content()

        # preenche linha 1 do formulario
        write("xpath", '//*[@id="vNOTAFISCAL_NUMERO"]', data['numero_nf'])
        write("xpath", '//*[@id="vNOTAFISCAL_SERIE"]', data['serie'])
        write("xpath", '//*[@id="vNOTAFISCAL_DATAMOVIMENTO"]', date)

        # preenche linha 2 do formulario
        write("xpath", '//*[@id="vNOTAFISCAL_DATAEMISSAOD"]', data['data_emissao'])
        write("xpath", '//*[@id="vNOTAFISCAL_DATACHEGADA"]', date)

        # preenche linha 3 do formulario
        Select(
            SE(driver, "css", 'select[id="vNOTAFISCAL_GRUPOMOVIMENTO"]').find()
        ).select_by_value('COM')

        # preenche linha 4 do formulario
        write("xpath", '//*[@id="vNOTAFISCAL_PESSOACOD"]', data['codigo_fornecedor'])
        driver.switch_to.default_content()
        Select(
            SE(driver, "css", 'select[id="vNOTAFISCAL_DEPARTAMENTOCOD"]').find()
        ).select_by_value(data['rateio'][0]["departamento"])

        # preenche linha 5 do formulario
        click("xpath", '//*[@id="NATOPE"]')
        natureza_operacao = str(int(data["natureza_operacao"]))
        Select(
            SE(driver, "css", '#vNOTAFISCAL_NATUREZAOPERACAOCOD').find()
        ).select_by_value(natureza_operacao)

        click("xpath", '//*[@id="CONFIRMAR"]')

        driver.switch_to.default_content()
        try:
            write("xpath", '//*[@id="vNOTAFISCAL_CONTAGERENCIALCOD"]', data["conta_gerencial"])
        except:
            pass

        try:
            Select(
                SE(driver, "css", 'select[id="vNOTAFISCAL_INDICADORPRESENCA"]').find()
            ).select_by_value("0")
        except:
            pass


        driver.switch_to.default_content()

        # preenche linha 6 do formulario
        click('xpath', '//*[@id="TIPODOC"]')
        try:
            Select(
                SE(driver, "css", 'select[id="vNOTAFISCAL_TIPODOCUMENTOCOD"]').find()
            ).select_by_value(
                data["tipo_documento"])  # data["tipo_documento"] # 36 | o codigo era 36 ante uns meses atras
        except:
            pass


        click("xpath", '//*[@id="CONFIRMAR"]')
        driver.switch_to.default_content()

        # preenche condição de pagamento e agente cobrador
        Select(
            SE(driver, "css", 'select[id="vNOTAFISCAL_CONDICAOPAGAMENTOCOD"]').find()
        ).select_by_value(data["condicao_pagamento"])

        driver.switch_to.default_content()
        Select(
            SE(driver, "css", 'select[id="vAGENTECOBRADOR_CODIGO"]').find()
        ).select_by_value("10")



        # preenche os demais campos da capa da nota
        write("xpath", '//*[@id="vNOTAFISCAL_OBSERVACAO"]', data['observacao'])
        write("xpath", '//*[@id="vNOTAFISCAL_VALORTOTALDIGITADO"]', data['valor_total'])

        if (data['codigo_verificacao'] != ''):
            try:
                write("xpath", '//*[@id="vNOTAFISCAL_CHAVENFE"]', data['codigo_verificacao']) # antes era vNOTAFISCAL_CODIGOVERIFICACAO
            except:
                pass
                # write("xpath", '//*[@id="vNOTAFISCAL_CODIGOVERIFICACAO"]', data['codigo_verificacao'])


        print("Capa da nota preenchida com sucesso!")
        return True
        
    except Exception as e:
        raise Exception(f"Não foi possivel preencher a capa da nota, erro: {e}")
