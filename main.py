pontos = 0
certos = 0

perguantas = ["Quantos graos de areia tem na terra: ", "quanto e 30 + 37: ", "Qual é a cor do cavalo branco de Napoleao: ", "Qual e o rio mais azedo do mundo: ", "Quantos tempo durou a guerra dos 100 anos: "]
respostas = ["+ de 2", "67", "branco", "solimoes", "100"]

for i in range(5):
    resposta = input(perguantas[i]).lower()
    if resposta == respostas[i]:
        print("Resposta correta!")
        pontos += 1
        certos += 1
    else:
        print(f"Errou! proxima pergunta.")

print(f"Você marcou {pontos} ponto!, acertando {certos} perguntas.")
if pontos == 5:
    print("Parabéns você acertou todas as perguntas.")
elif pontos >= 2:
    print("Você deu seu maximo, na proxima você consegue.")
else:
    print("Você realmente tentou né?")

