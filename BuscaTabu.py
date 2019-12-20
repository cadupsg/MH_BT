
import random
import copy
import time
#import numpy as np
#import math

class BuscaTabu:

    def __init__(self, rodada, nomeInst, instancia, solucao, sol_inicial):

        # recebe como parametro num da rodada e nome
        self.rodada = rodada + 1
        self.nomeInst = nomeInst

        self.instancia = instancia
        self.sol_inicial = sol_inicial

        # variavel com o caminho do arquivo que armazena os tempos de mudança da solucao global
        self.caminhoTempo = "F:\Cadu\metaheuristicas\instancias\Escolhidas\Geo\Saidas"

        # descomentar essa parte se quiser apenas 1 solucao
        # comentar se quiser usar o multistart
        # self.solucao = solucao
        # self.executaBuscaTabu()

        # descomentar essa parte se quiser utilizar o multistart
        # comentar se quiser apenas 1 solucao

        self.melhorFOGeral = 0
        self.piorFOGeral = 999999999

        for i in range(0, 5):

            self.solucao = self.sol_inicial.multiStart[i]

            # calcula o tempo que levou para convergir pra solucao
            start_time = time.time()

            self.executaBuscaTabu(i)

            # adiciona o tempo de solucao
            self.solucao.tempoOtimo = time.time() - start_time

            if (self.solucao.divTotal > self.melhorFOGeral):
                self.melhorFOGeral = self.solucao.divTotal
            elif (self.solucao.divTotal < self.piorFOGeral):
                self.piorFOGeral = self.solucao.divTotal

        return

    def executaBuscaTabu(self, iter):

        # cria o arquivo txt

        if (iter < 2):
            saidaTempo = open(self.caminhoTempo + "\\" + "SAIDA_" + self.nomeInst + "_rod_" + str(self.rodada) + "_tempo" + "_AL_" + str(iter+1) + ".txt", "w")
        elif (iter < 4):
            saidaTempo = open(self.caminhoTempo + "\\" + "SAIDA_" + self.nomeInst + "_rod_" + str(self.rodada) + "_tempo" + "_SAL_" + str(iter+1) + ".txt", "w")
        else:
            saidaTempo = open(self.caminhoTempo + "\\" + "SAIDA_" + self.nomeInst + "_rod_" + str(self.rodada) + "_tempo" + "_G_" + str(iter+1) + ".txt", "w")

        saidaTempo.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaTempo.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! INSTANCIA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaTempo.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")

        saidaTempo.write("\n")
        saidaTempo.write("NOME: " + self.nomeInst + "\n")
        saidaTempo.write("RODADA: " + str(self.rodada) + "\n")

        saidaTempo.write("\n")
        if (iter < 2):
            saidaTempo.write("TIPO SOL INICIAL: " + "ALEATORIA" + "\n")
        elif (iter < 4):
            saidaTempo.write("TIPO SOL INICIAL: " + "SEMI-ALEATORIA" + "\n")
        else:
            saidaTempo.write("TIPO SOL INICIAL: " + "GULOSA" + "\n")


        #a0 = self.instancia.limits[0][0]
        #a1 = self.instancia.limits[0][1]
        #a0 = self.instancia.limits[0][0]
        #a1 = self.instancia.limits[0][1]
        
        # define os parametros
        #temp = 250
        lista_tabu_tamanho = 20
        adicao_elementos = 1000
        sem_alteracao = 50
        #nsol = 20
        iter = 50000

        sol_corrente = []
        sol_corrente = copy.deepcopy(self.solucao.solucaoGrupos)
        sol_global = copy.deepcopy(self.solucao.solucaoGrupos)
        sol_best = self.verifica_FO(self.instancia.dist, sol_corrente)
        sol_historico = []

        lista_tabu = []
        #lista_tabu_aux = []
        
        sol_anterior = sol_best
        sem_alteracao_aux = 0

        # calcula o tempo que levou para convergir pra solucao
        start_time2 = time.time()

        # COMECA O LOOP
        for k in range(iter):
            # Constroi vetor que identifica o grupo em que cada vertice esta
            lista_grupos = []
            for i in range(self.instancia.M):
                for j in sol_corrente:
                    if (i in j):
                        lista_grupos.append(sol_corrente.index(j))

            # Guarda nsol solucoes vizinhas a solucao corrente

            #aux = 0
            #sol_aux = []
            sol_corrente_aux = []
            #rand_aux = []

            # variaveis que armazenam a posicao da melhor solucao encontrada
            # maior_solucao = 0
            # maior_indice = []

            #while (aux < nsol):
            sol_corrente_aux = copy.deepcopy(sol_corrente)
            sol_auxiliar = []
            while (True):
                # Sorteia entre quais grupos trocar os vertices
                rand1 = random.randint(0, self.instancia.M - 1)
                rand2 = random.randint(0, self.instancia.M - 1)
                if (lista_grupos[rand1] != lista_grupos[rand2]):
                    # troca_aux = sol_corrente_aux[lista_grupos[rand1]][lista_grupos[rand1].index(rand1)]
                    # troca_aux1 = rand1
                    # troca_aux2 = rand2

                    if (rand1 in sol_corrente[lista_grupos[rand1]]):
                        sol_corrente_aux[lista_grupos[rand1]][
                            sol_corrente[lista_grupos[rand1]].index(rand1)] = rand2
                        sol_corrente_aux[lista_grupos[rand2]][
                            sol_corrente[lista_grupos[rand2]].index(rand2)] = rand1
                    else:
                        sol_corrente_aux[lista_grupos[rand2]][
                            sol_corrente[lista_grupos[rand1]].index(rand1)] = rand2
                        sol_corrente_aux[lista_grupos[rand1]][
                            sol_corrente[lista_grupos[rand2]].index(rand2)] = rand1

                    sol_auxiliar.append(min(rand1, rand2))
                    sol_auxiliar.append(max(rand1, rand2))
                    sol_auxiliar.append(min(lista_grupos[rand1], lista_grupos[rand2]))
                    sol_auxiliar.append(max(lista_grupos[rand1], lista_grupos[rand2]))
                    sol_auxiliar.append(self.verifica_FO(self.instancia.dist, sol_corrente_aux))
                    #sol_aux.append(sol_auxiliar)
                    # sol_aux.append([rand1, rand2, lista_grupos[rand1], lista_grupos[rand2], verifica_FO(entrada, sol_corrente_aux)])
                    # if (sol_aux[aux][4] > maior_solucao):
                    #    maior_solucao = sol_aux[aux][4]
                    #    maior_indice = aux

                    # print(f'rand1 = {rand1}, rand2 = {rand2}')
                    #rand_aux.append(sorted([rand1, rand2]))

                    break

                #aux += 1
            # print(rand_aux)
            #sol_aux = np.array(sol_aux)[np.array(sol_aux)[:, 4].argsort()[::-1]].tolist()
            # print(sol_aux)

            # Constroi a lista tabu
            # lista_tabu = []
            # lista_tabu_aux = []

            #tabu_cheia = True
            #for i in sol_auxiliar:
            i = [int(sol_auxiliar[0])]
            i.append(int(sol_auxiliar[1]))
            i.append(int(sol_auxiliar[2]))
            i.append(int(sol_auxiliar[3]))
            i.append(sol_auxiliar[4])
                
            if (i[4] > sol_best):  # <- criterio de aspiracao

                saidaTempo.write("\n")
                tempoNovaFO = time.time() - start_time2
                saidaTempo.write("NOVA FO: " + str(i[4]) + "TEMPO:" + str(tempoNovaFO) + "\n")

                if (i in lista_tabu):  # <- verifica se o movimento estah na LT
                    #lista_tabu_aux[lista_tabu.index(i)] = 999
                    #lista_tabu_aux.remove(999)
                    lista_tabu.remove(i)
                    sol_historico[lista_tabu.index(i)] = 999
                    sol_historico.remove(999)
                sol_best = i[4]
                if (i[0] in sol_corrente[i[2]]):
                    # aux_troca = i[2]
                    sol_corrente[i[2]][sol_corrente[i[2]].index(i[0])] = i[1]
                    sol_corrente[i[3]][sol_corrente[i[3]].index(i[1])] = i[0]
                else:
                    sol_corrente[i[2]][sol_corrente[i[2]].index(i[1])] = i[0]
                    sol_corrente[i[3]][sol_corrente[i[3]].index(i[0])] = i[1]
                # aux_troca = sol_corrente[i[0]] [i[2]]
                # sol_corrente[i[0]][i[2]] = sol_corrente[i[1]][i[3]]
                # sol_corrente[i[1]][i[3]] = aux_troca
                sol_global = copy.deepcopy(sol_corrente)
                sol_historico.append(sol_corrente)
                lista_tabu.append(i)
                sem_alteracao_aux = 0
                sol_anterior = i[4]
                #lista_tabu_aux.append(temp + 1)
                #tabu_cheia = False
                #break
            elif (i[4] >= sol_anterior):
                if (i not in lista_tabu):  # <- movimento nao estah na LT
                    lista_tabu.append(i)
                    #lista_tabu_aux.append(temp + 1)
                    sol_historico.append(sol_corrente)
                    # print(f'i = {i}')
                    # print(f'sol_corrente = {sol_corrente}')
                    if (i[0] in sol_corrente[i[2]]):
                        # aux_troca = i[2]
                        sol_corrente[i[2]][sol_corrente[i[2]].index(i[0])] = i[1]
                        sol_corrente[i[3]][sol_corrente[i[3]].index(i[1])] = i[0]
                    else:
                        sol_corrente[i[2]][sol_corrente[i[2]].index(i[1])] = i[0]
                        sol_corrente[i[3]][sol_corrente[i[3]].index(i[0])] = i[1]
                    sem_alteracao_aux = 0
                    sol_anterior = i[4]
                else:
                    sem_alteracao_aux += 1
            elif (i[4] < sol_anterior):
                sem_alteracao_aux += 1

                # aux_troca = sol_corrente[i[0]] [i[2]]
                # sol_corrente[i[0]][i[2]] = sol_corrente[i[1]][i[3]]
                # sol_corrente[i[1]][i[3]] = aux_troca
                #tabu_cheia = False
                #break
            #voltar_solucao = math.inf
            #if (k % adicao_elementos == 0):  # <- faz o movimento mais antigo da LT
            #    if (k > 0):
            if (sem_alteracao_aux == sem_alteracao):
                #for i in sol_auxiliar:
                #    if (lista_tabu.index(i) < voltar_solucao):
                #        voltar_solucao = lista_tabu.index(i)
                #        if (voltar_solucao == 0):
                #            break

                sol_corrente = sol_historico[0]
                sol_historico.remove(sol_historico[0])
                sol_historico.append(sol_corrente)
                # aux_troca = lista_tabu[voltar_solucao][2]
                # sol_corrente[sol_aux[len(sol_aux)] [0]] [2] = sol_corrente[sol_aux[len(sol_aux)] [1]] [3]
                # sol_corrente[sol_aux[len(sol_aux)] [1]] [3] = aux_troca
                lista_tabu.append(lista_tabu[0])
                sol_anterior = lista_tabu[0][4]
                lista_tabu.remove(lista_tabu[0])
                sem_alteracao_aux = 0
                
                #lista_tabu_aux.remove(lista_tabu_aux[voltar_solucao])

                #lista_tabu_aux.append(temp + 1)

                # lista_tabu.remove(sol_aux[len(sol_aux)])
                # lista_tabu_aux[len(lista_tabu_aux)] = 999
                # lista_tabu_aux.remove(999)
                # lista_tabu.append(sol_aux[len(sol_aux)])
                # lista_tabu_aux.append(t+1)

            #lista_tabu_aux = list(np.array(lista_tabu_aux) - 1)
           # while (True):
           #     if (0 in lista_tabu_aux):
           #         sol_historico.remove(sol_historico[lista_tabu_aux.index(0)])
           #         lista_tabu.remove(lista_tabu[lista_tabu_aux.index(0)])
           #         lista_tabu_aux.remove(0)
           #     else:
           #         break
            
            # Remove solucao mais antiga da LT caso a mesma esteja acima do limite
            if (len(lista_tabu) > lista_tabu_tamanho):
                lista_tabu.remove(lista_tabu[0])
            
            # Faz insercao e remocao
            if (k % adicao_elementos == 0):
                if (k > 0):
                    while(True):
                        remocao = random.randint(0, len(sol_corrente)-1)
                        #print(f'remocao = {remocao}, a0 = {self.instancia.limits[remocao][0]}, {len(sol_corrente[remocao])}')
                        if (len(sol_corrente[remocao]) > self.instancia.limits[remocao][0]):
                            while(True):
                                insercao = random.randint(0, len(sol_corrente)-1)
                                #print(f'insercao = {insercao}, a1 = {self.instancia.limits[insercao][1]}, {len(sol_corrente[insercao])}')
                                if (insercao != remocao and len(sol_corrente[insercao]) < self.instancia.limits[insercao][1]):
                                    sol_corrente[insercao].append(random.choice(sol_corrente[remocao]))
                                    sol_corrente[remocao].remove(sol_corrente[insercao] [ len(sol_corrente[insercao])-1 ] )
                                    break
                            break
                #for i in sol_corrente:
                #    print(f'-> {len(i)}')
                #print('===')
                    

            # print(f'sol_global = {sol_global}')
            #print(f'sol_best = {sol_best}')
            # print(lista_tabu)

        # adiciona o valor de sol_best como diversidade total do objeto de Solucao
        self.solucao.divTotal = sol_best
        self.solucao.melhorFO = sol_best
        #print(sol_global)

        # fecha o arquivo
        saidaTempo.close()

        return

    def verifica_FO(self, entrada, sol):
        FO = 0
        for i in sol:
            for j in i:
                for k in i:
                    if (j < k):
                        # print(f'j = {j}, k = {k}')
                        FO += entrada[j][k]
        # print(f'FO = {FO}')
        # if FO >= 3864:
        #    print(f'FO = {FO}')
        return FO