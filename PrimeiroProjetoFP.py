def n_de_colunas(tab):
    """
    Input: tab(tuplo de tuplos)
    Output: inteiro
    Retorna um inteiro com o valor do numero de colunas
    """
    return len(tab[0])

def n_de_linhas(tab):
    """
    Input: tab(tuplo de tuplos)
    Output: inteiro
    Retorna um inteiro com o valor do numero de linhas
    """
    return len(tab)

def todas_posicoes_tabuleiro(tab):
    """
    Input: tab(tuplo de tuplos)
    Output: tuplo de inteiros
    Retorna um tuplo com todas as posicoes do tabuleiro
    """
    return tuple(range(1, n_de_colunas(tab)*n_de_linhas(tab) + 1))

def retorna_valores(tab, tpl):
    """
    Input: tab(tuplo de tuplos), tpl(tuplo)
    Output: tuplo
    Retorna um tuplo substituindo as posicoes de tpl pelos valores das proprias posicoes
    """
    return tuple(map(lambda x: obtem_valor(tab,x), tpl))


def sequencia(tpl_de_valores, tpl_de_posicoes, jog, pos):
    """
    Input: tpl_de_valores(tuplo de inteiros), tpl_de_posicoes(tuplo de inteiros), jog(inteiro), pos(inteiro)
    Output: inteiro
    Retorna um inteiro com o valor da maior sequencia contendo pos
    """
    total = []
    j = 0
    # tpl_de_valores é um tuplo com os valores contidos nas posicoes 
    # tpl_de_posicoes é um tuplo com as posicoes
    for i in tpl_de_valores:
        # só retornará a len do total caso a lista acabe ou (i seja diferente de numero e numero esta no total)
        if i == jog:
            #total adicionará as posições caso seja igual
            total += [tpl_de_posicoes[j]]
            if j == len(tpl_de_posicoes) - 1:
                return len(total)
        # caso i nao seja igual a jog ou retorna, caso pos esteja em total, ou reinicia total
        else:
            if pos in total:
                return len(total)
            else:
                total = []
        j += 1
    return 0




# funcao indice coluna
def icoluna(tab, pos):
    """
    Input: tab(tuplo de tuplos), pos(inteiro)
    Output: inteiro
    Retorna um inteiro com o indice da coluna da pos
    """
    return (pos - 1) % n_de_colunas(tab) 

# funcao indice linha 
def ilinha(tab, pos):
    """
    Input: tab(tuplo de tuplos), pos(inteiro)
    Output: inteiro
    Retorna um inteiro com o indice da linha da pos
    """
    return (pos - 1) // n_de_colunas(tab) 

def eh_jogador(jog):
    """
    Input: jog(inteiro)
    Output: bool
    Retorna um boliano informando se jog é jogador
    """
    jogadores = {1, -1} 
    return type(jog) == int and jog in jogadores

# funcao auxiliar
def posicao_no_tabuleiro(tab, ilinha, icoluna):
    """
    Input: tab(tuplo de tuplos), ilinha(inteiro), icoluna(inteiro)
    Output: inteiro
    Retorna um inteiro com a posicao correspondente ao indice da linha e ao indice da coluna
    """
    return ilinha * n_de_colunas(tab) + icoluna + 1

def centro_tabuleiro(tab):
    """
    Input: tab(tuplo de tuplos)
    Output: inteiro
    Retorna um inteiro com a posicao central do tabuleiro
    """
    return (n_de_linhas(tab)//2) * n_de_colunas(tab) + n_de_colunas(tab)//2 + 1

def eh_tabuleiro(tab):
    """
    Input: tab(tuplo de tuplos)
    Output: bool
    Retorna um boliano informando se tab está entre 2 e 100 e se seus elementos são 0, -1 ou 1
    """
    possiblenumbers = {-1,0,1}
    if not(type(tab) == tuple and 2 <= len(tab) <= 100):
        return False
    for i in range(len(tab)):
        if not(type(tab[i]) == tuple and 2 <= len(tab[i]) <= 100 and len(tab[i]) == len(tab[i-1])):
            return False
        for j in range(len(tab[i])):
            if not (tab[i][j] in possiblenumbers and type(tab[i][j]) == int):
                return False
    return True


def eh_posicao(pos):
    """
    Input: n(inteiro)
    Output: bool
    Retorna um boliano informando se pos é positivo e inteiro
    """
    if type(pos) == int and 1 <= pos <= 10000:
        return True
    return False

def obtem_dimensao(tab):
    """
    Input: tab(tuplo de tuplos)
    Output: tuplo de inteiros
    Retorna um tuplo com as dimensões de tab
    """
    return (len(tab), len(tab[0]))

def obtem_valor(tab, pos):
    """
    Input: tab(tuplo de tuplos), pos(inteiro)
    Output: inteiro
    Retorna um inteiro correspondente ao valor de pos
    """
    # achar o indice da linha e o da coluna
    return tab[ilinha(tab, pos)][icoluna(tab, pos)]

def obtem_coluna(tab, pos):
    """
    Input: tab(tuplo de tuplos), pos(inteiro)
    Output: tuplo de inteiros
    Retorna um tuplo com as posições da coluna de pos
    """
    # achar os elementos da coluna
    tuplo_coluna = ()
    for i in range(len(tab)):
        tuplo_coluna += (icoluna(tab, pos) + 1 + i * n_de_colunas(tab),)
    return tuplo_coluna

def obtem_linha(tab, pos):
    """
    Input: tab(tuplo de tuplos), pos(inteiro)
    Output: tuplo de inteiros
    Retorna um tuplo com as posições da linha de pos
    """
    # achar os elementos da linha
    tuplo_linha = ()
    for i in range(n_de_colunas(tab)):
        tuplo_linha += ((ilinha(tab, pos) * n_de_colunas(tab)) + 1 + i,)
    return tuplo_linha

def obtem_diagonais(tab, pos):
    """
    Input: tab(tuplo de tuplos), pos(inteiro)
    Output: tuplo contendo 2 tuplos
    Retorna a diagonal de pos no índice 0 e a antidiagonal de pos no indice 1
    """
        
    # diagonal
    diag_dir = ()
    # antidiagonal
    diag_esq = ()
    # definir variaveis que vao percorrer as diagonais
    lin_var, col_var = ilinha(tab, pos), icoluna(tab, pos)

    # achar valores da diagonal à esquerda de pos
    while lin_var >= 0 and col_var >= 0:
        diag_dir = (lin_var * n_de_colunas(tab) + col_var + 1,) + diag_dir
        lin_var -= 1
        col_var -= 1

    #reiniciar o valor das variáveis
    lin_var, col_var = ilinha(tab,pos), icoluna(tab,pos)

    # achar valores da diagonal à dir de pos
    while lin_var < n_de_linhas(tab) - 1 and col_var < n_de_colunas(tab) - 1:
        diag_dir = diag_dir + ((lin_var + 1) * n_de_colunas(tab) + col_var + 2,)
        lin_var += 1
        col_var += 1

    #reiniciar o valor das variáveis
    lin_var, col_var = ilinha(tab,pos), icoluna(tab,pos)

    # achar valores da antidiagonal à esquerda de pos
    while lin_var <= n_de_linhas(tab) -1 and col_var >= 0:
        diag_esq = (lin_var * n_de_colunas(tab) + col_var + 1,) + diag_esq
        lin_var += 1
        col_var -= 1
    
    #reiniciar o valor das variáveis
    lin_var, col_var = ilinha(tab,pos), icoluna(tab,pos)

    # achar valores da antidiagonal à direita de pos
    while lin_var > 0 and col_var < n_de_colunas(tab) - 1:
        diag_esq = diag_esq + ((lin_var - 1) * n_de_colunas(tab) + col_var + 2,)
        lin_var -= 1
        col_var += 1 

    return (diag_dir, diag_esq)

def tabuleiro_para_str(tab):
    """
    Input: tab(tuplo de tuplos)
    Output: str
    Retorna a representação do Tabuleiro em forma de str
    """
    # equivalencia
    representacao = { -1: "O", 0:"+", 1: "X"}
    # representação do tabuleiro em forma de str
    tab_em_str = ""
    # pegar linhas e seus respectivos indices
    for ilinha, linha in enumerate(tab):
        # pegar indice dos elementos
        for ielemento in range(len(linha)):
            # se for o primeiro elemnto da linha
            if ielemento == 0:
                tab_em_str += f"{representacao[linha[ielemento]]}"
            else:
                tab_em_str += f"---{representacao[linha[ielemento]]}"
        # se for a ultima linha
        if ilinha < len(tab) - 1:
            tab_em_str += f"\n|{(len(linha) - 1) * '   |'}\n"
    return tab_em_str

############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################

def dist_cheby(tab, pos_1, pos_2):
    """
    Input: tab(tuplo de tuplos), pos_1(inteiro), pos_2(inteiro)
    Output: inteiro
    Retorna um inteiro com a distancia entre as duas posicoes
    """
    return max(abs(icoluna(tab, pos_1) - icoluna(tab,pos_2)), abs(ilinha(tab, pos_1) - ilinha(tab, pos_2)))

def eh_posicao_valida(tab, pos):
    """
    Input: tab(tuplo de tuplos), pos(int)
    Output: bool
    Retorna um boliano verificando se a pos é válida
    """
    if not (eh_tabuleiro(tab) and eh_posicao(pos)):
        raise ValueError("eh_posicao_valida: argumentos invalidos")
    
    if not (pos <= len(tab) * len(tab[0])):
        return False
    return True

def eh_posicao_livre(tab,pos):
    """
    Input: tab(tuplo de tuplos), pos(int)
    Output: bool
    Retorna um boliano informando se a posição em que se deseja colocar a pedra está livre
    Levanta um erro caso algum dos argumentos nao seja válido
    """
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos)):
        raise ValueError("eh_posicao_livre: argumentos invalidos")    
    if tab[ilinha(tab, pos)][icoluna(tab, pos)] == 0:
        return True
    else: 
        return False
    
def obtem_posicoes_livres(tab):    
    """
    Input: tab(tuplo de tuplos)
    Output: tuplo de inteiros
    Retorna um tuplo com as posicoes livres
    Levanta um erro caso algum dos argumentos nao seja válido
    """
    if not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    pos_livres = ()
    # procurar elemento por elemento
    for ilinha in range(n_de_linhas(tab)):
        for ielemento in range(n_de_colunas(tab)):
            # ver se o elemento esta livre
            if tab[ilinha][ielemento] == 0:
                pos_livres += (ilinha*n_de_colunas(tab) + ielemento + 1 ,)
    return pos_livres


def obtem_posicoes_jogador(tab, jog):   
    """
    Input: tab(tuplo de tuplos), jog(int)
    Output: tuplo de inteiros
    Retorna um tuplo com as posicoes ocupadas pelo jogador
    Levanta um erro caso algum dos argumentos nao seja válido
    """
    if not (eh_tabuleiro(tab) and eh_jogador(jog)):
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")
    pos_do_jogador = ()
    # procurar elemento por elemento
    for ilinha in range(n_de_linhas(tab)):
        for ielemento in range(n_de_colunas(tab)):
            # ver se o elemento pertence ao jogador
            if tab[ilinha][ielemento] == jog:
                pos_do_jogador += (ilinha*n_de_colunas(tab) + ielemento + 1 ,)
    return pos_do_jogador

def obtem_posicoes_adjacentes(tab, pos):
    """
    Input: tab(tuplo de tuplos), pos(int)
    Output: tuplo de inteiros
    Retorna um tuplo com as posicoes adjacentes
    Levanta um erro caso algum dos argumentos nao seja válido
    """
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos)):
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    pos_adjacentes = ()
    # cria vetores para cima, baixo, esquerda e direita
    vetores = {"horizontal": {"left": 0, "parado": 0, "right":0 }, "vertical": {"up": 0, "parado": 0, "down": 0}}
    # ver se os vetores existem ou nao, vetor == 0 => nao existe (caso o elemento esteja na borda, ao menos 1 deles é igual a 0)
    # parado apenas é para manter na mesma linha ou coluna que pos
    if icoluna(tab,pos):
        vetores["horizontal"]["left"] -= 1
    if icoluna(tab,pos) < n_de_colunas(tab) - 1:
        vetores["horizontal"]["right"] += 1
    if ilinha(tab,pos):
        vetores["vertical"]["up"] -= 1
    if ilinha(tab,pos) < n_de_linhas(tab) - 1:
        vetores["vertical"]["down"] += 1
    # procurar nas 9 combinações de vetores
    for ver in vetores["vertical"]:
        for hor in vetores["horizontal"]:
            # indice da linha e da coluna de cada elemento
            ilinha_res = ilinha(tab,pos) + vetores["vertical"][ver]
            icoluna_res = icoluna(tab,pos) + vetores["horizontal"][hor]
            # caso uma combinação de vetores nao exista(por estar na borda), ele repetiria uma posicao, logo se impede a repetição
            # nao incluir a propria pos 
            if posicao_no_tabuleiro(tab,ilinha_res , icoluna_res) not in pos_adjacentes and \
                posicao_no_tabuleiro(tab,ilinha_res , icoluna_res) != pos:
                pos_adjacentes += (posicao_no_tabuleiro(tab,ilinha_res , icoluna_res),)
    return pos_adjacentes

def ordena_posicoes_tabuleiro(tab, tup):
    """
    Input: tab(tuplo de tuplos), tup(tuplo de inteiros)
    Output: tuplo de inteiros
    Retorna um tuplo com as posicoes ordenadas por proximidade ao centro
    Levanta um erro caso algum dos argumentos nao seja válido
    """
    # levantar os erros
    if not (eh_tabuleiro(tab) and type(tup) == tuple and \
             all(type(i) == int and i in todas_posicoes_tabuleiro(tab) for i in tup)):
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    c = centro_tabuleiro(tab)
    # ordenar conforme distancia 
    return tuple(sorted(tup, key= lambda x: dist_cheby(tab,c,x)))

def marca_posicao(tab,pos,jog):
    """
    Input: tab(tuplo de tuplos), pos(inteiro), jog(inteiro)
    Output: tuplo de tuplos
    Retorna um tuplo com as identico ao primeiro mas alterando o valor de uma posicao, que antes estava zerada
    Levanta um erro caso algum dos argumentos nao seja válido
    """
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_jogador(jog) and \
             eh_posicao_valida(tab,pos) and eh_posicao_livre(tab,pos)):
        raise ValueError("marca_posicao: argumentos invalidos")
    # pegar todas as linhas antes e depois
    linhas_antes = tab[:ilinha(tab,pos)]
    linhas_dps = tab[ilinha(tab,pos) + 1:]
    # slicing da linha alterada
    linha_alterada = (tab[ilinha(tab,pos)][:icoluna(tab,pos)] + (jog,) + tab[ilinha(tab,pos)][icoluna(tab,pos) + 1:],)
    #juntar
    tab = linhas_antes + linha_alterada + linhas_dps
    return tab

def eh_k(k):
    """
    Input: k(inteiro)
    Output: bool
    Retorna um boliano informando se k é um inteiro maior que 0
    """
    return type(k) == int and k > 0

def verifica_k_linhas(tab, pos, jog, k):
    """
    Input: tab(tuplo de tuplos), pos(inteiro), jog(inteiro), k(inteiro)
    Output: bool
    Retorna um boliano informando se há alguma sequencia seguida de k elementos na qual pos esteja (diagonais, vertical ou horizontal)
    Levanta um erro caso algum dos argumentos nao seja válido
    """
    if not(eh_tabuleiro(tab) and eh_posicao(pos) and eh_jogador(jog) and eh_k(k) and \
           eh_posicao_valida(tab,pos)):
        raise ValueError("verifica_k_linhas: argumentos invalidos")
    # caso exista uma sequencia maior ou igual a k return True
    if sequencia( retorna_valores(tab, obtem_coluna(tab,pos)), obtem_coluna(tab,pos), jog, pos  ) >= k or \
        sequencia( retorna_valores(tab, obtem_linha(tab,pos)), obtem_linha(tab,pos), jog, pos  ) >= k or \
        sequencia( retorna_valores(tab, obtem_diagonais(tab,pos)[0]), obtem_diagonais(tab,pos)[0], jog, pos  ) >= k or \
        sequencia( retorna_valores(tab, obtem_diagonais(tab,pos)[1]), obtem_diagonais(tab,pos)[1], jog, pos  ) >= k:
        return True
    return False


############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################

def eh_fim_jogo(tab, k):
    """
    Input: tab(tuplo de tuplos), k(inteiro)
    Output: bool
    Retorna um boliano informando se o jogo ja acabo
    """
    if not (eh_tabuleiro(tab) and eh_k(k)):
        raise ValueError("eh_fim_jogo: argumentos invalidos")
    numeros_possiveis = {1, -1}
    i = 0
    # percorrer todas as posicoes
    for pos in todas_posicoes_tabuleiro(tab):
        # caso posicao tenha tenha uma pedra
        if obtem_valor(tab, pos) in numeros_possiveis:
            #se essa pedra tive uma linha
            if verifica_k_linhas(tab, pos, obtem_valor(tab, pos), k):
                break
        else:
            # caso todas as posicoes estejam com pedra i = 0
            i = 1
    else: 
        # caso i = 0, acabou
        if not i:
            return True
        return False
    return True

def escolhe_posicao_manual(tab):
    """
    Input: tab(tuplo de tuplos)
    Output: inteiro
    Retorna um inteiro da posicao escolhida manualmente pela pessoa
    """
    if not eh_tabuleiro(tab):
        raise ValueError("escolhe_posicao_manual: argumento invalido")
    while True:
        pos = input("Turno do jogador. Escolha uma posicao livre: ")
        if pos.isdigit():
            pos = int(pos)
            if pos in obtem_posicoes_livres(tab):
                # apenas sair do loop quando pos for um inteiro e estiver um posicoes livres
                break
    return pos

def escolha_facil(tab, jog):
    """
    Input: tab(tuplo de tuplos), jog(inteiro)
    Output: inteiro
    Retorna um inteiro da posicao escolhida pelo computador na escolha facil
    """
    possiveis_proximas = []
    for pos in obtem_posicoes_jogador(tab, jog):
        # ver todas as posicoes adjacentes as pedras do jogador
        for pos_adjacente in obtem_posicoes_adjacentes(tab,pos):
            # se estiver livre, ela se torna uma posicao proxima possivel
            if pos_adjacente in obtem_posicoes_livres(tab):
                possiveis_proximas += [pos_adjacente]
    if possiveis_proximas:
        # escolher a possivel posicao mais proxima ao centro
        c = centro_tabuleiro(tab)
        return sorted(possiveis_proximas, key = lambda x: dist_cheby(tab, c, x))[0]
    if not possiveis_proximas:
        # caso nao haja nenhuma pos adjacente livre, escolher uma posicao qualquer mais  proxima do centro
        c = centro_tabuleiro(tab)
        return sorted(obtem_posicoes_livres(tab), key = lambda x: dist_cheby(tab, c, x))[0]

    
def maior_l_posicao(tab, pos, jog, k):
    """
    Input: tab(tuplo de tuplos), pos(inteiro), jog(inteiro), k(inteiro)
    Output: inteiro
    Retorna um inteiro da maior sequencia(k) que seria feita pelo jogador caso colocasse uma pedra ali
    """
    # contador conta a sequencia por linha
    contador = 1
    # maior guarda o valor do maior contador
    maior = 1
    # obtendo as linhas
    coluna = obtem_coluna(tab, pos)
    linha = obtem_linha(tab,pos)
    diagonal, anti = obtem_diagonais(tab, pos)
    for reta in [coluna, linha, diagonal, anti]:
        # vetor vai percorrer as linhas
        # vetor = -1 percorre de forma decrescente
        vetor = -1
        indice_pos = reta.index(pos)
        while 0 <= indice_pos + vetor and retorna_valores(tab, reta)[indice_pos + vetor] == jog and contador < k:
            contador +=1
            vetor -=1

        #vetor = 1 percorre de forma crescente
        vetor = 1

        while indice_pos + vetor < len(reta) and retorna_valores(tab, reta)[ indice_pos + vetor] == jog and contador < k:
            contador +=1
            vetor +=1
        
        #caso o contador seja maior que o maior, o contador se torna o maior
        if contador > maior:
            maior = contador
        contador = 1

    return maior


def funcao_ordenar_sort_l(tab, tpl, c):
    """
    Input: tab(tuplo de tuplos), tpl(tuplo), c(inteiro)
    Output: inteiro
    Retorna um tuplo que será usado como ordem de preferencia de organizaçao pelo sorted
    """
    return (tpl[0] * (-1), dist_cheby(tab, tpl[1], c ))


def maior_l_possivel(tab, jog, k):
    """
    Input: tab(tuplo de tuplos), jog(inteiro), k(inteiro)
    Output: tuplo
    Retorna um tuplo da maior sequencia(k) possivel que o jogador poderia fazer, analisando qual seria a maior sequencia por posicao,
    e a posicao que garante essa sequencia
    """
    c = centro_tabuleiro(tab)
    maior = ()
    for posicao in obtem_posicoes_livres(tab):
        # maior é um tuplo com relativos à todas as posicoes com a maior sequencia de pedras por posicao e a propria posicao
        maior += ((maior_l_posicao(tab, posicao, jog, k), posicao),)
    # maior é organizado conforme primeiramente pela maior sequencia de pedras e segundamente pela menor distancia ao centro 
    maior = sorted(maior, key = lambda x: funcao_ordenar_sort_l(tab, x, c))[0]

    return maior

    
def escolha_normal(tab, jog, k):
    """
    Input: tab(tuplo de tuplos), jog(inteiro), k(inteiro)
    Output: inteiro
    Retorna um inteiro da posicao a ser escolhida pelo computador na escolha normal
    """
    L_jogador = maior_l_possivel(tab, jog, k)
    L_oponente = maior_l_possivel(tab, jog*(-1), k)
    # compara quem tem maior sequencia
    if L_jogador[0] >= L_oponente[0]:
        # caso o jogador tenha maior ou igual sequencia, será colocado na pos do jogador
        return L_jogador[1]
    # caso o oponente tenha a maior sequencia, será colocado na posicao do oponente, para impedi-lo
    return L_oponente[1]

def escolha_dificil(tab, jog, k):
    """
    Input: tab(tuplo de tuplos), jog(inteiro), k(inteiro)
    Output: inteiro
    Retorna um inteiro da posicao a ser escolhida pelo computador na escolha dificil
    """
    adversario = jog * (-1)

    # caso o jogador possa ganhar o jogo, colocara uma peça ali
    for posicao in ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)):
        tab_simulada = marca_posicao(tab, posicao, jog)
        if verifica_k_linhas(tab_simulada, posicao, jog, k):
            return posicao
    # caso o oponente tenha uma posicao  que possa ganhar o jogo, colocará uma peça ali e o impedirá
    for posicao in ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)):
        tab_simulada = marca_posicao(tab, posicao, adversario)
        if verifica_k_linhas(tab_simulada, posicao, adversario, k):
            return posicao
        
    # simular jogos até o final com a dificuldade normal 
    # listas contendo as posicoes em que o jogo foi vencido e empado
    jogo_vencido_mais_centralizado = []
    jogos_empatados = []
    # simular para cada posicao livre
    for posicao in ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)):
        # marcar a posicao
        tab_simulada = marca_posicao(tab, posicao, jog)
        while True:
            # verifica se ainda tem posicoes livres, caso nao tenham mais posicoes livres, empate
            if not obtem_posicoes_livres(tab_simulada):
                jogos_empatados += [posicao]
                break
            # adversario joga
            prox_pos = escolhe_posicao_auto(tab_simulada, adversario, k, "normal")
            tab_simulada = marca_posicao(tab_simulada, prox_pos, adversario)
            # verifica se o adversario ganhou
            if verifica_k_linhas(tab_simulada, prox_pos, adversario, k):
                break
            # verifica se ainda tem posicoes livres, caso nao tenham mais posicoes livres, empate
            if not obtem_posicoes_livres(tab_simulada):
                jogos_empatados += [posicao]
                break
            # jogador joga:
            prox_pos = escolhe_posicao_auto(tab_simulada, jog, k, "normal")
            tab_simulada = marca_posicao(tab_simulada, prox_pos, jog)
            # verifica se o jogador ganhou
            if verifica_k_linhas(tab_simulada, prox_pos, jog, k):
                jogo_vencido_mais_centralizado += [posicao]
                break
            

    c = centro_tabuleiro(tab)

    if jogo_vencido_mais_centralizado:
        # caso hajam posicoes com jogos vencidos escolher a posicao que seja mais perto do centro
        return jogo_vencido_mais_centralizado[0]
    if jogos_empatados:
        # caso nao hajam posicoes com jogos vencidos mas hajam posicoes com jogos empatados escolher a posicao que seja mais perto do centro
        jogos_empatados = sorted(jogos_empatados, key = lambda x: dist_cheby(tab, x, c))
        return jogos_empatados[0]
    else:
        # caso perca em todos os jogos, escolher uma posicao livre ais  perto do centro
        jogos_perdidos = sorted(obtem_posicoes_livres(tab), key = lambda x: dist_cheby(tab, x, c))
        return jogos_perdidos[0]



def escolhe_posicao_auto(tab, jog, k, lvl):
    """
    Input: tab(tuplo de tuplos), jog(inteiro), k(inteiro), lvl(str)
    Output: inteiro
    Retorna um inteiro da posicao a ser escolhida pelo computador
    """
    levels = ["facil", "normal", "dificil"]

    if not(eh_tabuleiro(tab) and eh_jogador(jog) and eh_k(k) and lvl in levels and not eh_fim_jogo(tab, k)):
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")
    
    # realizar a escolha referente ao level escolhido

    if lvl == levels[0]:
        return escolha_facil(tab, jog)
    elif lvl == levels[1]:
        return escolha_normal(tab, jog, k)
    else:
        return escolha_dificil(tab, jog, k)


def jogo_mnk(cfg, jog, lvl):
    """
    Input: cfg(tuplo de inteiros), jog(inteiro), k(inteiro)
    Output: side effects(print), inteiro
    Faz um print do strs e retorna o valor da paça ganhadora do jogo
    """
    levels = ["facil", "normal", "dificil"]
    if not (type(lvl) == str and lvl in levels and eh_jogador(jog) and type(cfg) == tuple and len(cfg) == 3):
        raise ValueError("jogo_mnk: argumentos invalidos")
    for i in cfg:
        if not (type(i) == int):
            raise ValueError("jogo_mnk: argumentos invalidos")
    
    # atribuir as configurações
    m, n, k = cfg

    # criar um tabuleiro
    linha_da_tabela = (0,) * cfg[1]
    tab = (linha_da_tabela,) * cfg[0]

    
    if not (eh_tabuleiro(tab) and eh_k(k)):
        raise ValueError("jogo_mnk: argumentos invalidos")

    pedras = {-1 : "O", 1 : "X"}
    
    # mensagem
    print("Bem-vindo ao JOGO MNK.")
    # mensagem
    print(f"O jogador joga com '{pedras[jog]}'.")
    # tubuleiro
    print(tabuleiro_para_str(tab))
    
    # caso o jogador comece
    if jog == 1:
        pos = escolhe_posicao_manual(tab)
        tab = marca_posicao(tab, pos, jog)
        print(tabuleiro_para_str(tab))
    
    # definir adversario
    adversario = jog * (-1)

    while True:
        # mensagem
        print(f"Turno do computador ({lvl}):")

        # computador joga
        pos = escolhe_posicao_auto(tab, adversario, k, lvl)
        tab = marca_posicao(tab, pos, adversario)
        print(tabuleiro_para_str(tab))

        # caso seja verificado que o adversario(computador) completou uma linha, DERROTA
        if verifica_k_linhas(tab, pos, adversario, k):
            resultado = "DERROTA"
            vencedor = adversario
            break

        # caso nao haja mais posicoes livres, EMPATE
        if not obtem_posicoes_livres(tab):
            resultado = "EMPATE"
            vencedor = 0
            break
        


        # pessoa joga
        pos = escolhe_posicao_manual(tab)
        tab = marca_posicao(tab, pos, jog)
        print(tabuleiro_para_str(tab))

        # caso seja verificado que o jogador(pessoa) completou uma linha, VITORIA
        if verifica_k_linhas(tab, pos, jog, k):
            resultado = "VITORIA"
            vencedor = jog
            break

        # caso nao haja mais posicoes livres, EMPATE
        if not obtem_posicoes_livres(tab):
            resultado = "EMPATE"
            vencedor = 0
            break
    
    # mensagem
    print(resultado)
    #vencedor
    return vencedor






