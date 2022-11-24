import os

palavra_secreta = "lose"
letras_acertadas = ""
tentativas = 0

while True:
    letra = input("Digite uma letra: ").lower()
    tentativas += 1

    if len(letra) > 1:
        print("Digite apenas uma letra! ")
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += "*"

    print("Palavra Formada: ",palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("PARABÉNS! VOCÊ GANHOU O JOGO")
        print("A palavra Secreta era:", palavra_secreta)
        print(f"Total de tentativas {tentativas}")
        break
