def qtdPartidas(vitorias, derrotas):
    return vitorias - derrotas

def definirPatente(qtdTotal):
    if qtdTotal <= 10:
        patente = "Ferro"
    elif qtdTotal >= 11 and qtdTotal <= 20:
        patente = "Bronze"
    elif qtdTotal >= 21 and qtdTotal <= 50:
        patente = "Prata"
    elif qtdTotal >= 51 and qtdTotal <= 70:
        patente = "Ouro"
    elif qtdTotal >= 71 and qtdTotal <= 80:
        patente = "Platina"
    elif qtdTotal >= 81 and qtdTotal <= 90:
        patente = "Ascendente"
    elif qtdTotal >= 91 and qtdTotal <= 100:
        patente = "Imortal"
    else:
        patente = "Radiante"
    return patente

num_players = int(input("Digite o número de jogadores: "))

for i in range(1, num_players + 1):
    nomeHeroi = input(f"Nome do Herói {i}: ")
    qtdVitorias = int(input("Quantidade de Vitórias: "))
    qtdDerrotas = int(input("Quantidade de Derrotas: "))

    qtdTotal = qtdPartidas(qtdVitorias, qtdDerrotas)
    print(f"Total de Partidas do Herói {nomeHeroi}: {qtdVitorias + qtdDerrotas}")

    patenteFinal = definirPatente(qtdVitorias)
    print(f'O Herói {nomeHeroi} tem o saldo de {qtdTotal} vitórias e está no nível de {patenteFinal}\n')
