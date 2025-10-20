import funcoes
navios = [
        ["porta-aviões",4],
        ["navio-tanque",3], 
        ["navio-tanque",3], 
        ["contratorpedeiro",2], 
        ["contratorpedeiro",2], 
        ["contratorpedeiro",2], 
        ["submarino",1], 
        ["submarino",1], 
        ["submarino",1], 
        ["submarino",1]
        ]
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
i = 0
while i in list(range(10)):
    print(f"Insira as informações referentes ao navio {navios[i][0]} que possui tamanho {navios[i][1]}")
    linha = int(input("Insira a linha:"))
    coluna = int(input("Insira a coluna:"))
    if navios[i][0] != "submarino":
        orientacao = int(input("Insira a orientação:"))
        if orientacao == 1:
            orientacao = "vertical"
        elif orientacao == 2:
            orientacao = "horizontal"
        else:
            print ("Esta posição não está válida!")
            i -= 1
    else:
        orientacao = "vertical"
        

    posicoes = funcoes.define_posicoes(linha, coluna, orientacao, navios[i][1])
    frota = funcoes.preenche_frota(frota, navios[i][0], linha, coluna, orientacao, navios[i][1])
    if funcoes.posicao_valida(frota, linha, coluna, orientacao, navios[i][1]):
        print ("Esta posição não está válida!")
        i -= 1

    i += 1
print (frota)