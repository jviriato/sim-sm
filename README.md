# 🚌 simsm 🚌
Veja os horários do [SIM - SM](http://simsm.com.br/horarios/) no seu terminal.

### Instalação
Basta executar o seguinte comando no terminal: 
```bash
pip install simsm
```

### Utilização
O programa deve conter três argumentos: linha, saída, e dia. Exemplo:

Linha universidade, saindo da UFSM no dia de hoje
```bash
simsm universidade ufsm hoje
```
\
Você também pode filtrar por faixa velha/nova:
```bash
simsm universidade ufsm hoje -fn
```
\
Linha bombeiros, saindo do bairro no sábado
```bash
simsm bombeiros bairro sabado
```

### Docs
```bash
usage: simsm [-h] [-fv] [-fn] [-re] linha saida dia

positional arguments:
  linha              Linha do ônibus. Exemplo: universidade, bombeiros,
                     circular
  saida              De onde o ônibus sairá. Exemplo: bairro, centro, ufsm
  dia                Hoje: hoje Dias úteis: util Sábado: sabado Domingos e
                     feriados: domingo

optional arguments:
  -h, --help         show this help message and exit
  -fv, -faixa-velha  Para listar somente ônibus que passam pela faixa velha.
  -fn, -faixa-nova   Para listar somente ônibus que passam pela faixa nova.
  -re, -request      Utilização da biblioteca requests ao invés de cURL.)
```

### Contribua
Caso queira adicionar uma nova função, encontrou um bug ou sugestão, faça um pull request ou abra uma issue. :)

**To do:**
* Identificar feriados
* Adicionar todas as linhas do site SIM - SM (No momento tem apenas as linhas que vão até o campus)

### Licença
MIT © José Victor Viriato
