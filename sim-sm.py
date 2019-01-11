#!/usr/bin/env python3

import requests, json
from pprint import pprint

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
    r = requests.post(URL, data={'sentido': sentido, 'periodo': periodo})
    # print(r.text)
    pp_json = json.loads(r.text)
    pprint(pp_json)

def main():
    getData(UFSM_CENTRO, DIAS_UTEIS)


if __name__ == "__main__":
    main()