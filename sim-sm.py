#!/usr/bin/env python3
# coding=utf-8

import requests, json, argparse
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
    # table_data.append(data_list)
    table_instance = AsciiTable(table_data, 'UFSM -> CENTRO')
    print(table_instance.table)
    dt = datetime.now()
    print('Horário: ' + str(dt.hour) + ':' + str(dt.minute))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("linha", type=str, help="Linha do ônibus. Exemplo: universidade, bombeiros, circular")
    parser.add_argument("saida", type=str, help="De onde o ônibus sairá. Exemplo: bairro, centro, ufsm")
    parser.add_argument("dia", type=str, help="Hoje: hoje Dias úteis: util Sábado: sabado Domingos e feriados: domingo")
    parser.add_argument('-fv', '-faixa-velha', help='Para listar somente ônibus que passam pela faixa velha.')
    parser.add_argument('-fn', '-faixa-nova', help='Para listar somente ônibus que passam pela faixa nova.')
    args = parser.parse_args()
    
    if args.linha == 'universidade' and args.saida == ('bairro' or 'ufsm') and args.dia == 'util':
        getData(UFSM_CENTRO, DIAS_UTEIS)
    if args.linha == 'universidade' and args.saida == ('bairro' or 'ufsm') and args.dia == 'sabado':
        getData(UFSM_CENTRO, SABADO)
    if args.linha == 'universidade' and args.saida == ('bairro' or 'ufsm') and args.dia == 'domingo':
        getData(UFSM_CENTRO, DOMINGO)

    if args.linha == 'universidade' and args.saida == 'centro' and args.dia == 'util':
        getData(CENTRO_UFSM, DIAS_UTEIS)
    if args.linha == 'universidade' and args.saida == 'centro' and args.dia == 'sabado':
        getData(CENTRO_UFSM, SABADO)
    if args.linha == 'universidade' and args.saida == 'centro' and args.dia == 'domingo':
        getData(CENTRO_UFSM, DOMINGO)
    
    if args.linha == 'bombeiros' and args.saida == 'ufsm' and args.dia == 'util':
        getData(UFSM_BOMBEIROS, DIAS_UTEIS)
    if args.linha == 'bombeiros' and args.saida == 'ufsm' and args.dia == 'sabado':
        getData(UFSM_BOMBEIROS, SABADO)
    if args.linha == 'bombeiros' and args.saida == 'ufsm' and args.dia == 'domingo':
        getData(UFSM_BOMBEIROS, DOMINGO)

    if args.linha == 'bombeiros' and args.saida == 'bairro' and args.dia == 'util':
        getData(BOMBEIROS_UFSM, DIAS_UTEIS)
    if args.linha == 'bombeiros' and args.saida == 'bairro' and args.dia == 'sabado':
        getData(BOMBEIROS_UFSM, SABADO)
    if args.linha == 'bombeiros' and args.saida == 'bairro' and args.dia == 'domingo':
        getData(BOMBEIROS_UFSM, DOMINGO)

if __name__ == "__main__":
    main()
