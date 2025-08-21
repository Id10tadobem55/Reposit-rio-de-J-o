# Criando a principal função do jogo
def jogo():
    global vezes_jogadas  # Criação do contador para saber quantas vezes o jogador jogou o Quiz
    vezes_jogadas += 1 
    pontos = 0 # Criação do contador de pontos
    acertos = 0 # Criação do contador de acertos
    erros = 0 # Criação do contador de erros

    # Adicionando as perguntas do Quiz
    perguntas = [
        {
            "pergunta": "1) “Aglomerante é um material ativo, ligante, em geral pulverulento, sua função é formar uma pasta que promove a união entre os grãos do agregado”. Com essa definição, marque qual desses é um aglomerante:",
            "alternativas": ["a) Pedras", "b) Brita", "c) Gesso", "d) Seixo rolado", "e) Água"],
            "resposta correta": "c"
        },
        {
            "pergunta": "2) Elemento de transição entre a edificação e o solo:",
            "alternativas": ["a) Pilar", "b) Estaca", "c) Sapata", "d) Fundação", "e) Viga"],
            "resposta correta": "d"
        },
        {
            "pergunta": "3) “Consiste na colocação (ou recolocação) e compactação de solo em uma área específica.” A frase refere-se à(ao):",
            "alternativas": ["a) Aterro", "b) Corte", "c) Levantamento topográfico", "d) Escavações", "e) Tapumes"],
            "resposta correta": "a"
        },
        {
            "pergunta": "4) Na edificação, qual é o elemento da estrutura posicionado horizontalmente?",
            "alternativas": ["a) Pilar", "b) Laje", "c) Sapata de divisa", "d) Escoramentos", "e) Viga"],
            "resposta correta": "e"
        },
        {
            "pergunta": "5) Qual desses NÃO faz parte dos componentes principais do revestimento da PAREDE?",
            "alternativas": ["a) Emboço", "b) Rodapé", "c) Substrato", "d) Chapisco", "e) Rejunte"],
            "resposta correta": "b"
        },
        {
            "pergunta": "6) Qual desses NÃO faz parte da cobertura (telhado) da edificação?",
            "alternativas": ["a) Rincão", "b) Água furtada", "c) Beiral", "d) Espigão", "e) Soleira"],
            "resposta correta": "e"
        }
    ]
    
    # Pergunta 1
    print("\n" + perguntas[0]["pergunta"])
    print(perguntas[0]["alternativas"][0])
    print(perguntas[0]["alternativas"][1])
    print(perguntas[0]["alternativas"][2])
    print(perguntas[0]["alternativas"][3])
    print(perguntas[0]["alternativas"][4])
    resposta_usuario = input("Digite a letra da sua resposta: ").lower()
    if resposta_usuario == perguntas[0]["resposta correta"]:
        acertos += 1
        pontos += 5
        print(" Resposta correta! +5 pontos")
    else:
        erros += 1
        print(" Resposta incorreta.")

    # Pergunta 2
    print("\n" + perguntas[1]["pergunta"])
    print(perguntas[1]["alternativas"][0])
    print(perguntas[1]["alternativas"][1])
    print(perguntas[1]["alternativas"][2])
    print(perguntas[1]["alternativas"][3])
    print(perguntas[1]["alternativas"][4])
    resposta_usuario = input("Digite a letra da sua resposta: ").lower()
    if resposta_usuario == perguntas[1]["resposta correta"]:
        acertos += 1
        pontos += 5
        print(" Resposta correta! +5 pontos")
    else:
        erros += 1
        print(" Resposta incorreta.")

    # Pergunta 3
    print("\n" + perguntas[2]["pergunta"])
    print(perguntas[2]["alternativas"][0])
    print(perguntas[2]["alternativas"][1])
    print(perguntas[2]["alternativas"][2])
    print(perguntas[2]["alternativas"][3])
    print(perguntas[2]["alternativas"][4])
    resposta_usuario = input("Digite a letra da sua resposta: ").lower()
    if resposta_usuario == perguntas[2]["resposta correta"]:
        acertos += 1
        pontos += 5
        print(" Resposta correta! +5 pontos")
    else:
        erros += 1
        print(" Resposta incorreta.")

    # Pergunta 4
    print("\n" + perguntas[3]["pergunta"])
    print(perguntas[3]["alternativas"][0])
    print(perguntas[3]["alternativas"][1])
    print(perguntas[3]["alternativas"][2])
    print(perguntas[3]["alternativas"][3])
    print(perguntas[3]["alternativas"][4])
    resposta_usuario = input("Digite a letra da sua resposta: ").lower()
    if resposta_usuario == perguntas[3]["resposta correta"]:
        acertos += 1
        pontos += 5
        print(" Resposta correta! +5 pontos")
    else:
        erros += 1
        print(" Resposta incorreta.")

    # Pergunta 5
    print("\n" + perguntas[4]["pergunta"])
    print(perguntas[4]["alternativas"][0])
    print(perguntas[4]["alternativas"][1])
    print(perguntas[4]["alternativas"][2])
    print(perguntas[4]["alternativas"][3])
    print(perguntas[4]["alternativas"][4])
    resposta_usuario = input("Digite a letra da sua resposta: ").lower()
    if resposta_usuario == perguntas[4]["resposta correta"]:
        acertos += 1
        pontos += 5
        print(" Resposta correta! +5 pontos")
    else:
        erros += 1
        print(" Resposta incorreta.")

    # Pergunta 6
    print("\n" + perguntas[5]["pergunta"])
    print(perguntas[5]["alternativas"][0])
    print(perguntas[5]["alternativas"][1])
    print(perguntas[5]["alternativas"][2])
    print(perguntas[5]["alternativas"][3])
    print(perguntas[5]["alternativas"][4])
    resposta_usuario = input("Digite a letra da sua resposta: ").lower()
    if resposta_usuario == perguntas[5]["resposta correta"]:
        acertos += 1
        pontos += 5
        print(" Resposta correta! +5 pontos")
    else:
        erros += 1
        print(" Resposta incorreta.")
    
    #Exibiçaõ do resultado final
    print("\n--- Resultado da Partida ---")
    print(f"Nome do jogador: {nome_jogador}")
    print(f"Total de pontos: {pontos}")
    print(f"Total de acertos: {acertos}")
    print(f"Total de erros: {erros}")
    print(f"Total de vezes jogadas: {vezes_jogadas}")


# Inicialização do Quiz
vezes_jogadas = 0
nome_jogador = input("Digite seu nome: ")

continuar = "sim"  # valor inicial para entrar no laço

while continuar == "sim":
    jogo()  # Continua jogando
    continuar = input("\nDeseja jogar novamente? (sim/não): ")

print("\nObrigado por jogar!!! Espero que tenha gostado, até a próxima!")