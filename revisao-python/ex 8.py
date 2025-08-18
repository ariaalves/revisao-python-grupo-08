import requests
pais = input("Digite o nome de um país (em inglês): ").strip().lower()
url = "https://restcountries.com/v3.1/name/" + pais

resposta = requests.get(url)
if resposta.status_code == 200:
    dados = resposta.json()[0] 

    nome = dados["name"]["common"]
    linguas = dados["languages"].values()
    regiao = dados["region"]
    subregiao = dados["subregion"]
    capital = dados["capital"][0]

    moedas = dados["currencies"]
    for sigla, info in moedas.items():
        sigla_moeda = sigla
        nome_moeda = info["name"]
        simbolo_moeda = info["symbol"]

    fronteiras = dados.get("borders", ["Nenhum"])

    print("\n=== Informações sobre", nome, "===")
    print("Nome:", nome)
    print("Línguas:", ", ".join(linguas))
    print("Região:", regiao)
    print("Sub-região:", subregiao)
    print("Capital:", capital)
    print("\nMoeda:")
    print(" - Sigla:", sigla_moeda)
    print(" - Nome:", nome_moeda)
    print(" - Símbolo:", simbolo_moeda)
    print("\nPaíses que fazem fronteira:", ", ".join(fronteiras))

else:
    print("Erro: país não encontrado.")
