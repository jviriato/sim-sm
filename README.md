# 🚌 sim-sm 🚌
Aplicação em CLI para ver os horários de ônibus em [SIM - SM](http://simsm.com.br/horarios/).

### Instalação
Basta executar o seguinte comando no terminal: 
```bash
pip install sim-sm
```

### Utilização
O programa deve conter três argumentos: linha, saída, e dia. Exemplo:

Linha universidade, saindo da UFSM no dia de hoje
```bash
sim-sm universidade ufsm hoje
```
\
Você também pode filtrar por faixa velha/nova:
```bash
sim-sm universidade ufsm hoje -fn
```

  
Linha bombeiros, saindo do bairro no sábado
```bash
sim-sm bombeiros bairro sabado
```

### Docs
```bash
usage: sim-sm.py [-h] [-fv FV] [-fn FN] linha saida dia

positional arguments:
  linha                 Linha do ônibus. Exemplo: universidade, bombeiros,
                        circular
  saida                 De onde o ônibus sairá. Exemplo: bairro, centro, ufsm
  dia                   Hoje: hoje Dias úteis: util Sábado: sabado Domingos e
                        feriados: domingo

optional arguments:
  -h, --help            show this help message and exit
  -fv FV, -faixa-velha FV
                        Para listar somente ônibus que passam pela faixa
                        velha.
  -fn FN, -faixa-nova FN
                        Para listar somente ônibus que passam pela faixa nova.
```

### Dependências
O programa usa as seguintes bibliotecas:
* [terminaltables](https://github.com/Robpol86/terminaltables)

### Contribua
Caso queira adicionar uma nova função, encontrou um bug ou sugestão, faça um pull request ou abra uma issue. :)

**To do:**
* Identificar feriados
* Adicionar todas as linhas do site SIM - SM (No momento tem apenas as linhas que vão até o campus)

### Licença
MIT © José Victor Viriato
