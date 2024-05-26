# Script-NFC-e

## Objetivo
Este script foi desenvolvido para auxiliar e automatizar a coleta de informações sobre os itens comprados em um mercado, por meio da NFC-e.

## Necessidade
Surgiu a necessidade devido a um projeto pessoal focado em estatísticas e análise exploratória de dados com Python. O objetivo desse projeto é analisar os gastos pessoais em produtos do mercado.

## Utilização

Ao realizar a compra de produtos em um mercado, é emitida a Nota Fiscal do Consumidor Eletrônica (NFC-e). Se a compra for realizada em Santa Catarina, é possível visualizar a NFC-e por meio do [portal](https://sat.sef.sc.gov.br/tax.net/Sat.Dfe.NFCe.Web/Consultas/ConsultaPublicaNFe.aspx).  

A chave para consulta é disponibilizada no **Cupom Fiscal** entregue pelo Caixa após o pagamento da compra. Que pode ser escaneado para obter o link direto da NFC-e.  

Esse link será utilizado como argumento na execução do programa.

    - python3 script.py <link>

Que irá gerar um arquivo **.csv** separando em colunas por:
- Nome do mercado
- Produto
- Quantidade
- Medição
- Valor Unitário
- Valor Total
- Data

## Possíveis Melhorias

1. Passar a chave da NFC-e como parâmetro no sistema;
2. Acrescentar as colunas no header do arquivo;
3. Incluir mais colunas mediante necessidade;
4. Criar nova coluna de "Categoria" e desenvolver um sistema que automaticamente inclua o item em sua categoria (Carne, Frios e etc.).