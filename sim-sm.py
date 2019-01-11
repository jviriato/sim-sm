#!/usr/bin/env python3

import requests, json
from pprint import pprint
from datetime import datetime
from terminaltables import AsciiTable

# Constantes utilizadas no site SIM SM 
URL = 'http://www.simsm.com.br/ajax/buscarHorariosRotasNovo/'

UFSM_CENTRO     = 251
CENTRO_UFSM     = 250

UFSM_BOMBEIROS  = 248
BOMBEIROS_UFSM  = 249

UFSMCIRC_CENTRO = 252
CENTRO_UFSMCIRC = 253

DIAS_UTEIS      = 0
SABADO          = 1
DOMINGO         = 2

def getData(sentido, periodo):
    print('Fazendo a requisição...')
    # r = requests.post(URL, data={'sentido': sentido, 'periodo': periodo})
    # data = json.loads(r.text)

    data = json.load(open('via.json', 'r'))

    data_list = []
    pprint('Atualizado em: ' + data['atualizado'])
    for i in range(len(data['dados'])):
        data_list.append([data['dados'][i]['obs'], data['dados'][i]['hora']])
    
    printTable(data_list)

def printTable(data_list):
    table_data = [
        ['Via', 'Horário']
    ]
    for i in data_list:
        table_data.append(i)
    # table_data.append(['oi', 'limao'])
    print(data_list)

    # table_data.append(data_list)
    table_instance = AsciiTable(table_data, 'UFSM -> CENTRO')
    print(table_instance.table)
    dt = datetime.now()
    print('Horário: ' + str(dt.hour) + ':' + str(dt.minute))

def main():
    getData(UFSM_CENTRO, DIAS_UTEIS)


if __name__ == "__main__":
    main()