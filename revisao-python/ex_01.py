combustivel = input("Escolha o combustivel: digite A para álcool ou G para Gasolina\n")
qtd_litros = int(input("Digite quantos litros foram vendidos?\n"))

if combustivel == "A" and qtd_litros < 21:
    total = (qtd_litros * 1.90) - 0.03
    print(f"O valor a ser pago pelo cliente é de R$: {total:.2f}")
elif combustivel == "A" and qtd_litros > 20:
    total = (qtd_litros * 1.90) - 0.05
    print(f"O valor a ser pago pelo cliente é de R$: {total:.2f}")
elif combustivel == "G" and qtd_litros < 21:
    total = (qtd_litros * 2.50) - 0.04
    print(f"O valor a ser pago pelo cliente é de R$: {total:.2f}")
elif combustivel == "G" and qtd_litros > 20:
    total = (qtd_litros * 2.50) - 0.06
    print(f"O valor a ser pago pelo cliente é de R$: {total:.2f}")
else:
    print("Opção inválida!")