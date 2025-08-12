nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
    print(f"Primeira nota: {nota1:.2f}\nSegunda nota: {nota2:.2f}\nMédia: {media:.2f}\nConceito: A\nSituação: APROVADO")
elif media >= 7.5 and media < 9.0:
    print(f"Primeira nota: {nota1:.2f}\nSegunda nota: {nota2:.2f}\nMédia: {media:.2f}\nConceito: B\nSituação: APROVADO")
elif media >= 6.0 and media < 7.5:
    print(f"Primeira nota: {nota1:.2f}\nSegunda nota: {nota2:.2f}\nMédia: {media:.2f}\nConceito: C\nSituação: APROVADO")
elif media >= 4.0 and media < 6.0:
    print(f"Primeira nota: {nota1:.2f}\nSegunda nota: {nota2:.2f}\nMédia: {media:.2f}\nConceito: D\nSituação: REPROVADO")
elif media >= 0 and media < 4.0:
    print(f"Primeira nota: {nota1:.2f}\nSegunda nota: {nota2:.2f}\nMédia: {media:.2f}\nConceito: E\nSituação: REPROVADO")
else:
    print("Alguma das notas que você digitou não é válida. Por favor, digite novamente!")