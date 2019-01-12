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

Linha bombeiros, saindo do bairro no sábado
```bash
sim-sm bombeiros bairro sabado
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
