cedula1 = 0
cedula5 = 0
cedula20 = 0
cedula50 = 0
cedula100 = 0

while True:
    saque = int(input("Qual o valor do saque? "))
    if saque == 0:
        print("Saque cancelado.")
        break

    elif saque < 10 or saque > 600:
        print("Valor inválido! O saque deve ser entre 10 e 600 reais.")
    
    else:
        cedula100 = saque // 100
        saque = saque % 100
        cedula50 = saque // 50
        saque = saque % 50
        cedula10 = saque // 10
        saque = saque % 10
        cedula5 = saque // 5
        saque = saque % 5
        cedula1 = saque

        notas = [(cedula100, 100), (cedula50, 50), (cedula10, 10), (cedula5, 5), (cedula1, 1)]
        print("Notas fornecidas:")
        for quantidade, valor in notas:
            if quantidade > 0:
                print(f"{quantidade} nota(s) de {valor} real(is)")