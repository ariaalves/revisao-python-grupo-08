lista = []
sum = 0
media = 0
acima = []
while True:
    num = int(input("Digite um número (-1 para sair): "))
    if num != -1:
        lista.append(num)
    else:
        break

for a in range(len(lista)):
    sum += lista[a]

media = sum / len(lista)

for a in range(len(lista)):
    if lista[a] > media:
        acima.append(lista[a])


print(f"Foram digitados um total de {len(lista)} números.")
print(f"Números na lista: {lista}")
print(f"Números na lista: {lista[::-1]}")
print(f"Soma dos números: {sum}")   
print(f"Média dos números: {media}") 
print(f"Números acima da média: {acima}")
