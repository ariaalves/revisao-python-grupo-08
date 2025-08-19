import requests

cep = input("Digite o seu CEP:")

url = f"https://viacep.com.br/ws/{cep}/json/"


response = requests.get(url)
data = response.json()

zonas_sp = {
    "Vila Maria Alta": "Zona Norte",
    "Tatuapé": "Zona Leste",
    "Vila Mariana": "Zona Sul",
    "Barra Funda": "Zona Oeste",
    "Bela Vista": "Centro",
    "Vila Yara": "Cidade Vizinha"
}

cidade = "São Paulo"

if data["localidade"] == cidade:
        bairro = data["bairro"]
        zona = zonas_sp[bairro]
        print(f"Bairro: {bairro}, {zona} de {cidade}")
else:
        print(f"CEP pertence a outra cidade: {data['localidade']}")





