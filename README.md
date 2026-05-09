# Sistema de Automação Contábil - DRE (Python)

Este projeto é uma aplicação em Python desenvolvida para automatizar a classificação de contas contábeis e o cálculo de resultados financeiros utilizando uma DRE (Demonstração do Resultado do Exercício). O sistema processa dados de um arquivo Excel, classifica automaticamente as contas e gera relatórios tanto no terminal quanto em um novo arquivo `.xlsx`.

# Funcionalidades

* Processamento Direto de Excel: Lê dados contábeis de arquivos `.xlsx`.
* Classificação Automática: Classifica as contas contábeis entre:
  - Receita
  - Despesa
  - Custo
  - Imposto
  - Estorno
  - Outros
* Tratamento de Dados: Remove linhas vazias e organiza automaticamente os dados da planilha.
* Cálculo Financeiro Automatizado:
  - Total de Receitas
  - Total de Despesas
  - Total de Outros
  - Resultado Operacional
  - Resultado Líquido
* Relatório Automatizado: Gera uma nova planilha Excel contendo todas as classificações e um resumo financeiro no final do arquivo.

# Pré-requisitos

Para executar este projeto, você precisará do Python instalado e da biblioteca `pandas`, utilize:

```bash
pip install pandas openpyxl
```

# Estrutura de Arquivos

Para que o programa funcione corretamente, os arquivos devem estar organizados da seguinte forma:

- `main.py`: Script principal do sistema.
- `Arquivos Lista de Contas - Alunos.xlsx`: Base de dados original.
- `BaseAtualizada.xlsx`: Arquivo gerado automaticamente pelo sistema.

# Lógica de Decomposição Funcional

O projeto foi desenvolvido utilizando decomposição funcional, onde cada função possui uma única responsabilidade:

## `classificar_conta`

Responsável por identificar automaticamente a classificação de cada conta contábil.

## `obter_dados_processados`

Realiza a leitura do Excel, remove linhas inválidas, organiza os dados e aplica a classificação das contas.

## `calcular_balanco`

Calcula:
- receitas totais
- despesas totais
- outros valores
- resultado operacional
- resultado líquido

## `classificar_itens`

Exibe no terminal todas as contas com:
- nome da conta
- classificação
- valor

## `verificar_balanco`

Mostra no terminal os resultados financeiros calculados pelo sistema.

## `gerar_novo_arquivo`

Gera o arquivo `BaseAtualizada.xlsx` contendo:
- contas classificadas
- valores
- resumo financeiro ao final da planilha

## `menu`

Controla a navegação principal do sistema utilizando menu interativo no terminal.

# Menu de Opções

## Opção 1 — Mostrar classificação e valores

Exibe no terminal:
- nome da conta contábil
- classificação atribuída
- valor correspondente

## Opção 2 — Calcular Balanço

Mostra no terminal:
- total de receitas
- total de despesas
- total de outros
- resultado operacional
- resultado líquido

## Opção 3 — Gerar Novo Arquivo

Cria automaticamente o arquivo `BaseAtualizada.xlsx` contendo:
- todas as contas classificadas
- resumo financeiro ao final da planilha

## Opção 4 — Sair

Encerra a execução do sistema.

# Imagens do Programa em Execução

## Menu Principal

![Menu](./prints%20do%20projeto/1.png)

## Classificação das Contas (Opção 1)

![Classificação](./prints%20do%20projeto/2.png)

## Resultado do Balanço (Opção 2)

![Balanço](./prints%20do%20projeto/3.png)

## Arquivo Excel Gerado (Opção 3)

![Gerada](./prints%20do%20projeto/4.png)

![Planilha](./prints%20do%20projeto/5.png)
