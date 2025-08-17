# 5. O cardápio de uma lanchonete é o seguinte:
# Especificação Código Preço
# Cachorro Quente 100 R$ 1,20
# Bauru Simples 101 R$ 1,30
# Bauru com ovo 102 R$ 1,50
# Hambúrguer 103 R$ 1,20
# Cheeseburguer 104 R$ 1,30
# Refrigerante 105 R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule
# e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

hotdog = 100
baurusimples = 101
bauruovo = 102
hamburguer = 103
cheeseburguer = 104
refri = 105

valordog = 1.20
valorbaurusimples = 1.30
valorbauruovo = 1.50
valorhamburguer = 1.20
valorcheeseburguer = 1.30
valorrefri = 1.00

carrinho = []

while True:
    escolha = int(input(
        "Olá, escolha algo do cardápio:\n"
        "--------------------------------\n"
        "Especificação      Código   Preço\n"
        "Cachorro Quente    100      R$ 1,20\n"
        "Bauru Simples      101      R$ 1,30\n"
        "Bauru com ovo      102      R$ 1,50\n"
        "Hambúrguer         103      R$ 1,20\n"
        "Cheeseburguer      104      R$ 1,30\n"
        "Refrigerante       105      R$ 1,00\n"
        "--------------------------------\n"
        "Digite o código do produto (ou 0 para encerrar): "
    ))

    if escolha == 0:
        break

    quantidade = int(input("Digite a quantidade: "))

    if escolha == hotdog:
        carrinho.append(("Cachorro Quente", quantidade, valordog))
    elif escolha == baurusimples:
        carrinho.append(("Bauru Simples", quantidade, valorbaurusimples))
    elif escolha == bauruovo:
        carrinho.append(("Bauru com Ovo", quantidade, valorbauruovo))
    elif escolha == hamburguer:
        carrinho.append(("Hambúrguer", quantidade, valorhamburguer))
    elif escolha == cheeseburguer:
        carrinho.append(("Cheeseburguer", quantidade, valorcheeseburguer))
    elif escolha == refri:
        carrinho.append(("Refrigerante", quantidade, valorrefri))
    else:
        print("Código inválido!")

total = 0
print("\nResumo do pedido:")
for item in carrinho:
    nome, qtd, preco = item
    subtotal = qtd * preco
    total += subtotal
    print(f"{nome} x{qtd} = R$ {subtotal:.2f}")

print(f"\nTotal a pagar: R$ {total:.2f}")
