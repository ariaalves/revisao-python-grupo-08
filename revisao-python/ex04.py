totalAlunos = 0
notas = []
gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']

while True:
    acertos = 0
    respostas = []

    for a in range(10):
        resposta = input(f"Qual a resposta da questão {a + 1}? (Escolha entre: A, B, C, D, E): ").upper()
        respostas.append(resposta)

    for a in range(10):
        if respostas[a] == gabarito[a]:
            acertos += 1
    print(f"Você acertou {acertos} questões")
    notas.append(acertos)
    totalAlunos += 1
    outro = input("Outro aluno deseja fazer a prova? (s/n): ")
    if outro == 'n':
        print("Encerrando a prova.")
        break
    elif outro != 's':
        print("Opção inválida. Encerrando o sistema.")
        break

    media = sum(notas)/totalAlunos

    print(f"Total de alunos que utilizaram o sistema: {totalAlunos}")
    print(f"Maior número de acertos: {max(notas)}")
    print(f"Menor número de acertos: {min(notas)}")
    print(f"Média de acertos da turma: {media:.2f}")