pontos = 0
tentativas = 3

while tentativas >0:
    resposta = input("Quantos graos de areia tem na terra: ")

    if resposta == "+ de 2":
        print("Resposta correta!")
        pontos += 1
        break
    else:
        print(f"Errou! ainda restam {tentativas} tentativas.")
        tentativas -= 1

print(f"Você marcou {pontos} ponto!")

