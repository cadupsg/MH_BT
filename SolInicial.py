import random
import copy
import time

from Solucao import Solucao

class SolInicial:

    def __init__(self, instancia, solucao):

        self.instancia = instancia
        self.solucao = solucao

        # gera a solucao inicial de maneira aleatoria
        # self.geraSolAleatoria()

        # gera a solucao inicial de maneira semi-gulosa
        # self.geraSolSemiAleatoria()

        # gera a solucao inicial de maneira gulosa
        # self.geraSolGulosa()

        # !!!!!!!!!!!!!!! ESTA PARTE DE BAIXO APENAS DESCOMENTAR SE QUISER MULTISTART !!!!!!!!!!!!!!!
        # gera as 5 solucoes que serao utilizadas no multistart
        # 2 aleatorias, 2 semigulosas, 1 gulosa

        # cria o Array 3D que ira conter todas as solucoes a serem utilizadas no multistart
        # comentar essa parte se quiser apenas 1 solucao
        # descomentar essa parte se quiser o multistart
        self.multiStart = []

        for i in range(0, 5):

            self.solucao = Solucao(self.instancia)

            # calcula o tempo que levou para gerar a solucao inicial
            start_time = time.time()

            if (i<2):
                self.geraSolAleatoria()
            elif (i<4):
                self.geraSolSemiAleatoria()
            else:
                self.geraSolGulosa()

            # adiciona o tempo de geracao
            self.solucao.tempoGer = time.time() - start_time

            self.multiStart.append(self.solucao)

        return

    def geraSolAleatoria(self):

        # seleciona randomicamente G elementos
        lista_inicial = random.sample(range(0, self.instancia.M), self.instancia.G)
        self.lista_elementos = list(range(0, self.instancia.M))
        self.lista_elementos = [x for x in self.lista_elementos if x not in lista_inicial]

        # inclui os elementos sorteados randomicamente na solucao
        for i in range(0, self.instancia.G):
            self.solucao.solucaoGrupos[i].append(lista_inicial[i])

        # declara as variaveis auxiliares
        minimoPreenchido = True
        gruposPossiveis = []
        grupoEscolhido = 0

        # inclui os elementos restantes nos grupos
        # enquanto tiver elementos restantes na lista de elementos, adiciona-se elementos nos grupos
        while ((len(self.lista_elementos) != 0)):

            # verifica se todos os grupos ja têm o minimo requerido de elementos para incluir
            for i in range(0, self.instancia.G):
                if (len(self.solucao.solucaoGrupos[i]) < self.instancia.limits[i][0]):
                    minimoPreenchido = False

            # procedimento para caso precise preencher algum minimo
            if (not (minimoPreenchido)):

                for i in range(0, self.instancia.G):
                    if (len(self.solucao.solucaoGrupos[i]) < self.instancia.limits[i][0]):
                        if (len(self.lista_elementos) != 0):
                            # se a lista tiver mais de um elemento, seleciona-se um randomicamente
                            if (len(self.lista_elementos) > 1):
                                rand = random.randint(0, len(self.lista_elementos) - 1)
                            else:
                                rand = 0

                            # soma a diversidade total em cada grupo
                            for elemento in self.solucao.solucaoGrupos[i]:
                                self.solucao.distTotalGrupo[i] += self.instancia.dist[self.lista_elementos[rand]][
                                    int(elemento)]

                            # adiciona o elemento sorteado no grupo correspondente
                            self.solucao.solucaoGrupos[i].append(self.lista_elementos[rand])

                            # retira o elemento em questao da lista de elementos faltantes
                            del self.lista_elementos[rand]
                        else:
                            print("Nao tem elementos o suficiente para preencher o minimo das listas")

                # muda-se o flag para testar novamente
                minimoPreenchido = True

            # depois que todos os grupos ja tiverem o seu minimo, aloca-se os elementos restantes
            # a alocacao deve ser feita em grupos que nao tenham ultrapassado o seu maximo
            else:

                # a cada loop verifica quais grupos ainda podem receber elementos
                # ou seja, quais grupos nao tiveram seu maximo atingido
                for i in range(0, self.instancia.G):
                    if (len(self.solucao.solucaoGrupos[i]) < self.instancia.limits[i][1]):
                        gruposPossiveis.append(i)

                if (len(gruposPossiveis) != 0):

                    # adiciona-se o elemento em um grupo aleatorio
                    grupoEscolhido = random.randint(0, len(gruposPossiveis) - 1)

                    # se a lista tiver mais de um elemento, seleciona-se um randomicamente
                    if (len(self.lista_elementos) > 1):
                        rand = random.randint(0, len(self.lista_elementos) - 1)
                    else:
                        rand = 0

                    # soma a diversidade total em cada grupo
                    for elemento in self.solucao.solucaoGrupos[gruposPossiveis[grupoEscolhido]]:
                        self.solucao.distTotalGrupo[gruposPossiveis[grupoEscolhido]] += self.instancia.dist[self.lista_elementos[rand]][
                                    int(elemento)]

                    # adiciona o elemento sorteado no grupo correspondente
                    self.solucao.solucaoGrupos[gruposPossiveis[grupoEscolhido]].append(self.lista_elementos[rand])

                    # retira o elemento em questao da lista de elementos faltantes
                    del self.lista_elementos[rand]

                    # zera a lista de grupos possiveis para ser recriada caso tenha algum elemento faltante
                    gruposPossiveis.clear()

                else:
                    print("nao existe mais grupo em que seja possivel incluir mais um elemento")

        # atualiza a diversidade total
        for i in range(0, self.instancia.G):
            self.solucao.divTotal += self.solucao.distTotalGrupo[i]

        """print("TAMANHO DOS GRUPOS")
        for i in range(0, self.instancia.G):
            print(len(self.solucao.solucaoGrupos[i]))

        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("SOLUCAO ALEATORIA:" + str(self.solucao.solucaoGrupos))
        print("SOMA DIST POR GRUPO:" + str(self.solucao.distTotalGrupo))
        print("DIVERSIDADE TOTAL:" + str(self.solucao.divTotal))"""

        return

    def geraSolSemiAleatoria(self):

        # seleciona randomicamente G elementos
        lista_inicial = random.sample(range(0, self.instancia.M), self.instancia.G)
        self.lista_elementos = list(range(0, self.instancia.M))
        self.lista_elementos = [x for x in self.lista_elementos if x not in lista_inicial]

        # inclui os elementos sorteados randomicamente na solucao
        for i in range(0, self.instancia.G):
            self.solucao.solucaoGrupos[i].append(lista_inicial[i])

        # declara as variaveis auxiliares
        minimoPreenchido = True
        gruposPossiveis = []
        grupoEscolhido = 0

        # inclui os elementos restantes nos grupos
        # enquanto tiver elementos restantes na lista de elementos, adiciona-se elementos nos grupos
        while ((len(self.lista_elementos) != 0)):

            # verifica se todos os grupos ja têm o minimo requerido de elementos para incluir
            for i in range(0, self.instancia.G):
                if (len (self.solucao.solucaoGrupos[i]) < self.instancia.limits[i][0]):
                    minimoPreenchido = False

            # procedimento para caso precise preencher algum minimo
            if (not(minimoPreenchido)):

                for i in range(0, self.instancia.G):
                    if (len(self.solucao.solucaoGrupos[i]) < self.instancia.limits[i][0]):
                        if (len(self.lista_elementos) != 0):
                            # se a lista tiver mais de um elemento, seleciona-se um randomicamente
                            if (len(self.lista_elementos) > 1):
                                rand = random.randint(0, len(self.lista_elementos)-1)
                            else:
                                rand = 0

                            # soma a diversidade total em cada grupo
                            for elemento in self.solucao.solucaoGrupos[i]:
                                self.solucao.distTotalGrupo[i] += self.instancia.dist[self.lista_elementos[rand]][int(elemento)]

                            # adiciona o elemento sorteado no grupo correspondente
                            self.solucao.solucaoGrupos[i].append(self.lista_elementos[rand])

                            # retira o elemento em questao da lista de elementos faltantes
                            del self.lista_elementos[rand]
                        else:
                            print("Nao tem elementos o suficiente para preencher o minimo das listas")

                # muda-se o flag para testar novamente
                minimoPreenchido = True

            # depois que todos os grupos ja tiverem o seu minimo, aloca-se os elementos restantes
            # a alocacao deve ser feita em grupos que nao tenham ultrapassado o seu maximo
            else:

                # a cada loop verifica quais grupos ainda podem receber elementos
                # ou seja, quais grupos nao tiveram seu maximo atingido
                for i in range(0, self.instancia.G):
                    if (len(self.solucao.solucaoGrupos[i]) < self.instancia.limits[i][1]):
                        gruposPossiveis.append(i)

                if (len(gruposPossiveis) != 0):

                    # estrategia: adiciona-se o elemento no grupo com a maior quantidade de elementos
                    grupoEscolhido = gruposPossiveis[0]
                    for i in range(0, len(gruposPossiveis)): # gruposPossiveis:
                        if(len(self.solucao.solucaoGrupos[i]) > len(self.solucao.solucaoGrupos[grupoEscolhido])):
                            grupoEscolhido = gruposPossiveis[i]

                    # soma a diversidade total em cada grupo
                    for elemento in self.solucao.solucaoGrupos[grupoEscolhido]:
                        self.solucao.distTotalGrupo[grupoEscolhido] += self.instancia.dist[self.lista_elementos[0]][int(elemento)]

                    # adiciona o elemento sorteado no grupo correspondente
                    self.solucao.solucaoGrupos[grupoEscolhido].append(self.lista_elementos[0])

                    # retira o elemento em questao da lista de elementos faltantes
                    del self.lista_elementos[0]

                    # zera a lista de grupos possiveis para ser recriada caso tenha algum elemento faltante
                    gruposPossiveis.clear()

                else:
                    print("nao existe mais grupo em que seja possivel incluir mais um elemento")

        # atualiza a diversidade total
        for i in range(0, self.instancia.G):
            self.solucao.divTotal += self.solucao.distTotalGrupo[i]

        """print("TAMANHO DOS GRUPOS")
        for i in range(0, self.instancia.G):
            print(len(self.solucao.solucaoGrupos[i]))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        print("SOLUCAO SEMI-ALEATORIA:" + str(self.solucao.solucaoGrupos))
        print("SOMA DIST POR GRUPO:" + str(self.solucao.distTotalGrupo))
        print("DIVERSIDADE TOTAL:" + str(self.solucao.divTotal))"""

        return

    def geraSolGulosa(self):

        # cria a lista com todos os elementos que devem ser alocados em grupos
        self.lista_elementos = copy.deepcopy(self.instancia.distOrd)

        # declara as variaveis auxiliares
        minimoPreenchido = True
        gruposReceber = []
        gruposRetirar = []
        grupoEscolhido = 0
        elementoInicio = 0
        proximoElemento = 0
        start_time = time.time()

        while ((len(self.lista_elementos) != 0)):

            for i in range(0, len(self.lista_elementos[0])-1):

                elementoAlocado = False
                for j in range(0, self.instancia.G):

                    # verifica se o elemento em questao ja esta em algum grupo
                    if (self.lista_elementos[0][i] in self.solucao.solucaoGrupos[j]):
                        elementoAlocado = True

                    # verifica quais grupos podem receber elementos
                    if (len(self.solucao.solucaoGrupos[j]) < self.instancia.limits[j][1]):
                        gruposReceber.append(j)

                if (not(elementoAlocado)):

                    # adiciona ao grupo caso nao tenha ultrapassado o seu maximo
                    self.solucao.solucaoGrupos[gruposReceber[0]].append(int(self.lista_elementos[0][i]))

                # zera a lista de grupos possiveis para ser recriada caso tenha algum elemento faltante
                gruposReceber.clear()

            # retira-se a linha referente aos elementos ja adicionados
            del self.lista_elementos[0]

        """print("SOLUCAO ANTES")
        print("SOLUCAO GULOSA: " + str(self.solucao.solucaoGrupos))
        print("TAMANHO DA LISTA:")
        for i in range(0, self.instancia.G):
            print(len(self.solucao.solucaoGrupos[i]))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")"""

        # Faz as modificacoes necessarias para que todos tenham seus minimos preenchidos
        for i in range(0, self.instancia.G):

            # verifica quais grupos precisam ser preenchidos com o minimo
            if (len(self.solucao.solucaoGrupos[i]) < self.instancia.limits[i][0]):

                # muda o flag representando que tem grupo sem o minimo preenchido
                minimoPreenchido = False

                # a partir de agora os grupos possiveis serao aqueles que ainda necessitam incluir elementos
                # para completar o minimo de cada grupo
                gruposReceber.append(i)

            # verifica quais grupos podem ter elementos retirados
            if (len(self.solucao.solucaoGrupos[i]) > self.instancia.limits[i][0]):
                gruposRetirar.append(i)

        while (not(minimoPreenchido)):

            # retira um elemento do grupo que pode perder e coloca no grupo que precisa ganhar
            # o grupo que ira perder eh o ultimo grupo da lista de grupos que pode perder
            grupoEscolhido = gruposRetirar[len(gruposRetirar)-1]
            self.solucao.solucaoGrupos[gruposReceber[0]].append(self.solucao.solucaoGrupos[grupoEscolhido][len(self.solucao.solucaoGrupos[grupoEscolhido])-1])
            del self.solucao.solucaoGrupos[grupoEscolhido][len(self.solucao.solucaoGrupos[grupoEscolhido])-1]

            # muda o flag novamente para True
            minimoPreenchido = True

            # zera as listas
            gruposReceber.clear()
            gruposRetirar.clear()

            # verifica novamente quais grupos precisam receber e quais podem perder
            for i in range(0, self.instancia.G):

                # verifica quais grupos precisam ser preenchidos com o minimo
                if (len(self.solucao.solucaoGrupos[i]) < self.instancia.limits[i][0]):
                    # muda o flag representando que tem grupo sem o minimo preenchido
                    minimoPreenchido = False

                    # a partir de agora os grupos possiveis serao aqueles que ainda necessitam incluir elementos
                    # para completar o minimo de cada grupo
                    gruposReceber.append(i)

                # verifica quais grupos podem ter elementos retirados
                if (len(self.solucao.solucaoGrupos[i]) > self.instancia.limits[i][0]):
                    gruposRetirar.append(i)

        # Soma as diversidades internas em cada grupo e a diversidade total
        for i in range(0, self.instancia.G):
            for j in range(0, len(self.solucao.solucaoGrupos[i]) - 1):

                # variavel auxiliar para facilitar a compreensao do somatorio da diversidade em cada grupo
                elementoInicio = self.solucao.solucaoGrupos[i][j]

                # iterador responsavel por fazer a soma de cada vertice j para os outros vertices no mesmo grupo
                for k in range(j+1, len(self.solucao.solucaoGrupos[i])):

                    # variavel auxiliar para facilitar a compreensao do somatorio da diversidade em cada grupo
                    proximoElemento = self.solucao.solucaoGrupos[i][k]

                    # somatorio da distancia da aresta no contador
                    self.solucao.distTotalGrupo[i] += self.instancia.dist[elementoInicio][proximoElemento]

            self.solucao.divTotal += self.solucao.distTotalGrupo[i]

        tempoGuloso = time.time() - start_time

        """print("SOLUCAO DEPOIS:")
        print("SOLUCAO GULOSA: " + str(self.solucao.solucaoGrupos))
        print("TAMANHO DOS GRUPOS:")
        for i in range(0, self.instancia.G):
            print(len(self.solucao.solucaoGrupos[i]))

        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("SOMA DIST POR GRUPO:" + str(self.solucao.distTotalGrupo))
        print("DIVERSIDADE TOTAL: " + str(self.solucao.divTotal))
        print("TEMPO CONSTR GULOSO: " + str(tempoGuloso))"""

        return