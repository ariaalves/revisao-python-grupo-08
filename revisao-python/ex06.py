# 6. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# • Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# • Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# • A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
# percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
# o programa permitindo que o usuário digite o salário inicial do funcionário.

salario_inicial = float(input("Digite o salário inicial do funcionário: "))

salario = salario_inicial
aumento = 0.015  


salario += salario_inicial * aumento  

for ano in range(1997, 2026):
    aumento *= 2
    salario *= (1 + aumento)

print(f"\nSalário atual em 2025: R$ {salario:.2f}")
