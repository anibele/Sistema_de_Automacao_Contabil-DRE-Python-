import pandas as pd

# --- CONFIGURAÇÕES ---
BASE_ORIGINAL = "Arquivos Lista de Contas - Alunos.xlsx"
BASE_ATUALIZADA = "BaseAtualizada.xlsx"


#classificar_conta: Essa função recebe o nome da conta contábil
#e retorna sua classificação.
def classificar_conta(nome_conta):
    """
    Classifica a conta contábil como:
    Receita, Despesa, Custo, Imposto, Estorno ou Outros.
    """

    # Verifica se o valor é vazio ou não é texto
    if pd.isna(nome_conta) or not isinstance(nome_conta, str):
        return ""

    classificacoes = {
        "Receita": [
            "Receita Bruta de Vendas",
            "Receitas Financeiras",
            "Outras Receitas Operacionais"
        ],

        "Estorno": [
            "Devoluções de Vendas"
        ],

        "Imposto": [
            "ICMS sobre Vendas",
            "PIS/COFINS sobre Vendas"
        ],

        "Custo": [
            "Custo das Mercadorias Vendidas"
        ],

        "Despesa": [
            "Salários e Ordenados",
            "Encargos Sociais",
            "Aluguel de Imóveis",
            "Energia Elétrica e Água",
            "Despesas com Marketing",
            "Comissões de Vendedores",
            "Fretes sobre Vendas",
            "Despesas com Manutenção",
            "Depreciação e Amortização",
            "Despesas Financeiras",
            "Despesas Bancárias e Tarifas"
        ],

        "Outros": [
            "Provisão para IRPJ",
            "Provisão para CSLL"
        ]
    }

    for classificacao, lista_contas in classificacoes.items():
        for item in lista_contas:
            if item in nome_conta:
                return classificacao

    return ""


#obter_dados_processados: Essa função lê o Excel original,
#organiza os dados e adiciona a classificação.
def obter_dados_processados():
    """
    Lê o arquivo Excel original e retorna
    um DataFrame organizado e classificado.
    """

    # Ler planilha
    df = pd.read_excel(BASE_ORIGINAL)

    # Remove linhas totalmente vazias
    df = df.dropna(how='all')

    # Criar DataFrame padronizado
    df_limpo = pd.DataFrame()

    df_limpo["Conta Contábil"] = df.iloc[:, 1]
    df_limpo["Valor"] = df.iloc[:, 2]

    # Remove linha do cabeçalho que entrou como dado
    df_limpo = df_limpo[df_limpo["Conta Contábil"] != "Conta Contábil"]

    # Remove linhas vazias
    df_limpo = df_limpo.dropna(subset=["Conta Contábil"])

    # Classificar contas
    df_limpo["Classificação"] = df_limpo["Conta Contábil"].apply(classificar_conta)

    return df_limpo

#calcular_balanco: Essa função calcula os totais
#necessários para o balanço patrimonial.
def calcular_balanco(df):
    """
    Calcula os valores do balanço.
    """
    #calcula o total de receitas
    total_receitas = df[df["Classificação"] == "Receita"]["Valor"].sum()

    #calcula o total de despesas
    total_despesas = df[
        df["Classificação"].isin(["Despesa", "Custo", "Imposto", "Estorno"])
    ]["Valor"].sum()

    #cacula o total de outros
    total_outros = df[df["Classificação"] == "Outros"]["Valor"].sum()

    #calcula o resultado operacional
    resultado_operacional = total_receitas + total_despesas

    #calcula o resultado líquido
    resultado_liquido = resultado_operacional + total_outros

    return (
        total_receitas,
        total_despesas,
        total_outros,
        resultado_operacional,
        resultado_liquido
    )

def classificar_itens():
  """
    Opção 1:
    Mostra a classificação dos itens no terminal.
    """
  df = obter_dados_processados()
  print("\nContas:")
  for _, linha in df.iterrows():
        print(
            (
                "Item: "+str(linha["Conta Contábil"]),
                "Classificação: "+str(linha["Classificação"].lower()),
                "Valor: "+str(linha["Valor"])
            )
        )


#verificar_balanco: Essa função mostra no terminal
#as contas classificadas e os resultados do balanço.
def verificar_balanco():
    """
    Opção 2:
    Exibe as contas e o balanço no terminal.
    """

    df = obter_dados_processados()

    (
        total_receitas,
        total_despesas,
        total_outros,
        resultado_operacional,
        resultado_liquido
    ) = calcular_balanco(df)

    print("\nBalanço:")

    print(f"Ativos:   R$ {total_receitas:,.2f}")
    print(f"Passivos: R$ {total_despesas:,.2f}")
    print(f"Outros:  R$ {total_outros:,.2f}")

    print(f"\nResultado operacional: R$ {resultado_operacional:,.2f}")

    print(f"Resultado Líquido: R$ {resultado_liquido:,.2f}")


#gerar_novo_arquivo: Essa função gera um novo arquivo xlsx
#com as classificações preenchidas e o resumo do balanço.
def gerar_novo_arquivo():
    """
    Opção 3:
    Gera um novo arquivo xlsx com:
    - contas classificadas
    - resultado do balanço
    """

    print(f"\n Gerando {BASE_ATUALIZADA}...")

    df = obter_dados_processados()

    (
        total_receitas,
        total_despesas,
        total_outros,
        resultado_operacional,
        resultado_liquido
    ) = calcular_balanco(df)

    # Criar resumo para adicionar no final do arquivo
    resumo = [
        {"Conta Contábil": "", "Valor": "", "Classificação": ""},

        {"Conta Contábil": "Ativos",
         "Valor": total_receitas,
         "Classificação": ""},

        {"Conta Contábil": "Passivos",
         "Valor": total_despesas,
         "Classificação": ""},

        {"Conta Contábil": "Outros",
         "Valor": total_outros,
         "Classificação": ""},

        {"Conta Contábil": "Resultado Operacional",
         "Valor": resultado_operacional,
         "Classificação": ""},

        {"Conta Contábil": "Resultado Líquido",
         "Valor": resultado_liquido,
         "Classificação": ""}
    ]

    df_resumo = pd.DataFrame(resumo)

    # Juntar dados + resumo
    df_final = pd.concat([df, df_resumo], ignore_index=True)

    # Salvar Excel
    df_final.to_excel(BASE_ATUALIZADA, index=False)

    print(f"Arquivo '{BASE_ATUALIZADA}' gerado com sucesso!")

def menu():
    while True:
        print("\n--- MENU CONTÁBIL ---")
        print("1. Mostrar classificação e Valores")
        print("2. Calcular Balanço")
        print("3. Gerar Novo Arquivo")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            classificar_itens()

        elif opcao == "2":
            verificar_balanco()

        elif opcao == "3":
            gerar_novo_arquivo()

        elif opcao == "4":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
