from modules.core.database import Database

def run(naturezas_operacao: list):
    db = Database()
    data = []

    for n in naturezas_operacao:
        data.append((n['text'], n['value']))

    db.cursor.executemany("""
        INSERT INTO naturezas_de_operacao (name, code) 
        VALUES (?, ?)
    """, data)

    db.conn.commit()

    db.close()



if __name__ == '__main__':
    # teste mockado
    naturezas = [{'value': '174', 'text': 'ALUGUEL (SUBLOCAÇÃO)',                   'goevo_cod': '000000174'},
                 {'value': '50',  'text': 'AQUISIÇÃO DE SERV DE TELECOMUNICAÇÕES',  'goevo_cod': '000000050'},
                 {'value': '18',  'text': 'AQUISIÇÃO DE SERVIÇOS',                  'goevo_cod': '000000018'},
                 {'value': '49',  'text': 'AQUISIÇÃO DE SERVIÇOS DE ENERGIA',       'goevo_cod': '000000049'},
                 {'value': '199', 'text': 'COMISSÃO E-COMMERCE',                    'goevo_cod': '000000199'},
                 {'value': '135', 'text': 'COMPRA DE COMBUSTIVEL E LUBL CONSUM',    'goevo_cod': '000000135'},
                 {'value': '55',  'text': 'COMPRA DE IMOBILIZADO',                  'goevo_cod': '000000055'},
                 {'value': '4',   'text': 'COMPRA DE MATERIAL DE CONSUMO/DIVERSOS', 'goevo_cod': '000000004'},
                 {'value': '114', 'text': 'COMPRA INSUMOS E SERV P/ OFICINA',       'goevo_cod': '000000114'},
                 {'value': '224', 'text': 'COMPRA MATERIAL CONSUMO- ESTOQUE',       'goevo_cod': '000000224'},
                 {'value': '51',  'text': 'ENTRADA POR FATURA/BOLETOS',             'goevo_cod': '000000051'},
                 {'value': '22',  'text': 'FRETE DE PEÇAS',                         'goevo_cod': '000000022'},
                 {'value': '46',  'text': 'FRETE DESPESA',                          'goevo_cod': '000000046'},
                 {'value': '219', 'text': 'FRETE E-COMMERCE',                       'goevo_cod': '000000219'},
                 {'value': '163', 'text': 'MERCADORIA DE TERCEIROS COBRADO EM O.S', 'goevo_cod': '000000163'},
                 {'value': '84',  'text': 'NF COMPLEMENTAR COMPRA DE PEÇAS',        'goevo_cod': '000000084'},
                 {'value': '78',  'text': 'NF COMPLEMENTAR COMPRA VEICULO',         'goevo_cod': '000000078'}
                 ]

    [{'value': '174', 'text': 'ALUGUEL (SUBLOCAÇÃO)'}, {'value': '50', 'text': 'AQUISIÇÃO DE SERV DE TELECOMUNICAÇÕES'},
     {'value': '18', 'text': 'AQUISIÇÃO DE SERVIÇOS'}, {'value': '49', 'text': 'AQUISIÇÃO DE SERVIÇOS DE ENERGIA'},
     {'value': '199', 'text': 'COMISSÃO E-COMMERCE'}, {'value': '135', 'text': 'COMPRA DE COMBUSTIVEL E LUBL CONSUM'},
     {'value': '55', 'text': 'COMPRA DE IMOBILIZADO'}, {'value': '4', 'text': 'COMPRA DE MATERIAL DE CONSUMO/DIVERSOS'},
     {'value': '114', 'text': 'COMPRA INSUMOS E SERV P/ OFICINA'},
     {'value': '224', 'text': 'COMPRA MATERIAL CONSUMO- ESTOQUE'},
     {'value': '51', 'text': 'ENTRADA POR FATURA/BOLETOS'}, {'value': '22', 'text': 'FRETE DE PEÇAS'},
     {'value': '46', 'text': 'FRETE DESPESA'}, {'value': '219', 'text': 'FRETE E-COMMERCE'},
     {'value': '163', 'text': 'MERCADORIA DE TERCEIROS COBRADO EM O.S'},
     {'value': '84', 'text': 'NF COMPLEMENTAR COMPRA DE PEÇAS'},
     {'value': '78', 'text': 'NF COMPLEMENTAR COMPRA VEICULO'}]




    run(naturezas)