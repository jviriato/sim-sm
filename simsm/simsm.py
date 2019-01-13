#!/usr/bin/env python3
# coding=utf-8

import requests, json, argparse, subprocess
from pprint import pprint
from datetime import datetime
from terminaltables import AsciiTable
from colorama import init, Fore, Style

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

def getData(sentido, periodo, request = True, faixa_velha = False, faixa_nova = False):
    data_list = []
    if request == False:
        print('Fazendo a requisição...')
        data = 'sentido=' + str(sentido) + '&' + 'periodo=' + str(periodo)

        subp = subprocess.Popen(['curl', '-4', '--data', data, URL], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        curlstdout, curlstderr = subp.communicate()
        data = json.loads(curlstdout.decode('UTF-8'))
    
    else:
        print('Fazendo a requisição através da biblioteca Requests...')
        r = requests.post(URL, data={'sentido': sentido, 'periodo': periodo})
        data = json.loads(r.text)

    pprint('Atualizado em: ' + data['atualizado'])
    for i in range(len(data['dados'])):
        data_list.append([data['dados'][i]['obs'], data['dados'][i]['hora']])
    
    if faixa_velha == True:
        for data in data_list[:]:
            if data[0] == 'Faixa nova':
                data_list.remove(data)

    if faixa_nova == True:
        for data in data_list[:]:
            if data[0] == 'Faixa velha':
                data_list.remove(data)


    printTable(data_list)
    

def printTable(data_list):
    dt = datetime.now()

    table_data = [
        ['Via', 'Horário']
    ]

    eh_horario_atual = False
    for data in data_list:
        data_bus = datetime.strptime(data[1], '%H:%M')
        data_bus = data_bus.replace(year=dt.year, month=dt.month, day=dt.day)
        if(datetime.now() < data_bus and eh_horario_atual == False):
            data[0] = Fore.GREEN + data[0] + Fore.RESET
            data[1] = Fore.GREEN + data[1] + Fore.RESET
            eh_horario_atual = True
        table_data.append(data)

    table_instance = AsciiTable(table_data)
    print(table_instance.table)
    print(Fore.GREEN + 'Horário: ' + str(dt.hour) + ':' + str(dt.minute))


def verificaWeekDay(arg_dia):
    if arg_dia == 'hoje':
        #segunda = 0
        domingo_weekday = 6
        sabado_weekday  = 5
        if datetime.today().weekday() == domingo_weekday:
            return 'domingo'
        elif datetime.today().weekday() == sabado_weekday:
            return 'sabado'
        else:
            return 'util'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("linha", type=str, help="Linha do ônibus. Exemplo: universidade, bombeiros, circular")
    parser.add_argument("saida", type=str, help="De onde o ônibus sairá. Exemplo: bairro, centro, ufsm")
    parser.add_argument("dia", type=str, help="Hoje: hoje Dias úteis: util Sábado: sabado Domingos e feriados: domingo")
    parser.add_argument('-fv', '-faixa-velha', help='Para listar somente ônibus que passam pela faixa velha.' , action='store_true')
    parser.add_argument('-fn', '-faixa-nova', help='Para listar somente ônibus que passam pela faixa nova.' , action='store_true')
    parser.add_argument('-re', '-request', help='Utilização da biblioteca requests ao invés de cURL.)', action='store_true')
    args = parser.parse_args()
    init()
    dia = verificaWeekDay(args.dia)
    if args.linha == 'universidade' and args.saida in ['bairro', 'ufsm', 'campus', 'universidade'] and dia == 'util':
        getData(UFSM_CENTRO, DIAS_UTEIS, args.re, args.fv,  args.fn)
    if args.linha == 'universidade' and args.saida in ['bairro', 'ufsm', 'campus', 'universidade'] and dia == 'sabado':
        getData(UFSM_CENTRO, SABADO, args.re, args.fv,  args.fn)
    if args.linha == 'universidade' and args.saida in ['bairro', 'ufsm', 'campus', 'universidade'] and dia == 'domingo':
        getData(UFSM_CENTRO, DOMINGO, args.re, args.fv,  args.fn)

    if args.linha == 'universidade' and args.saida == 'centro' and dia == 'util':
        getData(CENTRO_UFSM, DIAS_UTEIS, args.re, args.fv,  args.fn)
    if args.linha == 'universidade' and args.saida == 'centro' and dia == 'sabado':
        getData(CENTRO_UFSM, SABADO, args.re, args.fv,  args.fn)
    if args.linha == 'universidade' and args.saida == 'centro' and dia == 'domingo':
        getData(CENTRO_UFSM, DOMINGO, args.re, args.fv,  args.fn)
    
    if args.linha == 'bombeiros' and args.saida in ['ufsm', 'campus', 'universidade'] and dia == 'util':
        getData(UFSM_BOMBEIROS, DIAS_UTEIS, args.re, args.fv,  args.fn)
    if args.linha == 'bombeiros' and args.saida in ['ufsm', 'campus', 'universidade'] and dia == 'sabado':
        getData(UFSM_BOMBEIROS, SABADO, args.re, args.fv,  args.fn)
    if args.linha == 'bombeiros' and args.saida in ['ufsm', 'campus', 'universidade'] and dia == 'domingo':
        getData(UFSM_BOMBEIROS, DOMINGO, args.re, args.fv,  args.fn)

    if args.linha == 'bombeiros' and args.saida in ['bairro', 'bombeiros'] and dia == 'util':
        getData(BOMBEIROS_UFSM, DIAS_UTEIS, args.re, args.fv,  args.fn)
    if args.linha == 'bombeiros' and args.saida in ['bairro', 'bombeiros'] and dia == 'sabado':
        getData(BOMBEIROS_UFSM, SABADO, args.re, args.fv,  args.fn)
    if args.linha == 'bombeiros' and args.saida in ['bairro', 'bombeiros'] and dia == 'domingo':
        getData(BOMBEIROS_UFSM, DOMINGO, args.re, args.fv,  args.fn)

if __name__ == "__main__":
    main()
