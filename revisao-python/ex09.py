import requests

nome_moeda = {

    "USD": "dólares americanos",
    "EUR": "euros",
    "GBP": "libras esterlinas"
}

sigla = input("Digite a Sigla da moeda que voocê deseja fazer a conversão para real. \nPor exemplo: USD (Dólar), EUR (Euro), GBP (Libra Esterlina)\n").upper()

url = f"https://api.exchangerate-api.com/v4/latest/BRL"

response = requests.get(url)
data = response.json()

if sigla in data["rates"]:
    cambio = data["rates"][sigla]
    moeda_convertida = 1/cambio
    moeda = nome_moeda[sigla]

    print(f"O Real vale {moeda_convertida:.2f} de {moeda}")
else:
    print("Sigla não encontrada! Por favor, digite uma nova sigla")