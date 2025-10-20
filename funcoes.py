def define_posicoes (linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else: 
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota (frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    for chave, valor in frota.items():
        for i in range(len(valor)):
            for j in range(len(valor[i])):
                x = valor[i][j][0]
                y = valor[i][j][1] 

                tabuleiro[x][y] = 1
    return tabuleiro

def afundados (frota, tabuleiro):
    navios_afundados = 0
    for lista_navios in frota.values():
        for navio in lista_navios:
            total_posicoes = 0
            for posicao in navio:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] == 'X':
                    total_posicoes += 1
            if total_posicoes == len(navio):
                navios_afundados += 1
    return navios_afundados