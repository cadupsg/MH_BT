
class SaidaBT:

    def __init__(self, rodada, nomeInst, tempoInst, tempoSolInicial, tempoExecBT, instancia, solucao, sol_inicial, executaBT):

        # recebe como parametro num da rodada e nome
        self.rodada = rodada+1
        self.nomeInst = nomeInst

        # recebe como parametro os tempos de execucao de cada parte
        self.tempoInst = tempoInst
        self.tempoSolInicial = tempoSolInicial
        self.tempoExecBT = tempoExecBT

        # recebe como parametro as instancias de cada classe
        self.instancia = instancia
        self.solucao = solucao
        self.sol_inicial = sol_inicial
        self.executaBT = executaBT

        # chama o metodo para imprimir as saidas
        self.imprimeSaidas()

        return

    def imprimeSaidas(self):

        # define o caminho de onde os arquivos de saida devem ser armazenados
        self.caminho = "F:\Cadu\metaheuristicas\instancias\Escolhidas\Geo\Saidas"

        # cria o arquivo txt
        saidaResul = open(self.caminho + "\\" + "SAIDA_" + self.nomeInst + "_rod_" + str(self.rodada) + ".txt", "w")

        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! INSTANCIA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")

        saidaResul.write("\n")
        saidaResul.write("QTD GRUPO: " + str(self.instancia.G) + "\n")
        saidaResul.write("QTD ELEMENTOS: " + str(self.instancia.M) + "\n")
        saidaResul.write("LIMITES POR GRUPO [MIN, MAX]: " + str(self.instancia.limits) + "\n")
        saidaResul.write("DISTANCIAS ENTRE OS ELEMENTOS: " + str(self.instancia.dist) + "\n")
        saidaResul.write("DISTANCIAS ORDENADAS DECRESC: " + str(self.instancia.distOrd) + "\n")

        saidaResul.write("\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!! SOLUCAO INICIAL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")

        saidaResul.write("\n")
        saidaResul.write("DADOS DE CADA SOLUCAO INICIAL CRIADA:" + "\n")
        for i in range(0, 5):

            saidaResul.write("\n")
            if (i<2):
                saidaResul.write(str(i+1) + ") SAIDA ALEATORIA:" + "\n")
            elif (i<4):
                saidaResul.write(str(i+1) + ") SAIDA SEMI-ALEATORIA:" + "\n")
            else:
                saidaResul.write(str(i+1) + ") SAIDA GULOSA:" + "\n")

            saidaResul.write("\n")
            saidaResul.write("TAMANHO DOS GRUPOS" + "\n")
            for j in range(0, self.instancia.G):
                saidaResul.write(str(len(self.sol_inicial.multiStart[i].solucaoGrupos[j])) + "\n")

            saidaResul.write("\n")
            saidaResul.write("SOLUCAO:" + str(self.sol_inicial.multiStart[i].solucaoGrupos) + "\n")
            saidaResul.write("SOMA DIST INICIAL POR GRUPO:" + str(self.sol_inicial.multiStart[i].distTotalGrupo) + "\n")
            saidaResul.write("DIVERSIDADE TOTAL INICIAL:" + str(self.sol_inicial.multiStart[i].divTotal) + "\n")
            saidaResul.write("TEMPO PRA GERAR SOL:" + str(self.sol_inicial.multiStart[i].tempoGer) + "\n")

        saidaResul.write("\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! BUSCA TABU !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")

        saidaResul.write("\n")
        saidaResul.write("DADOS DA BT APLICADA A CADA SOLUCAO INICIAL CRIADA:" + "\n")

        for i in range(0, 5):

            saidaResul.write("\n")
            saidaResul.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + "\n")
            saidaResul.write("EXECUCAO DA SOLUCAO INICIAL " + str(i) + ": " + "\n")
            saidaResul.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + "\n")

            saidaResul.write("\n")
            saidaResul.write("MELHOR FO:" + str(self.sol_inicial.multiStart[i].melhorFO) + "\n")
            saidaResul.write("TEMPO P/ ATINGIR OTIMO:" + str(self.sol_inicial.multiStart[i].tempoOtimo) + "\n")

        saidaResul.write("\n")
        saidaResul.write("DADOS GERAIS RELATIVOS AO MULTISTART:" + "\n")

        saidaResul.write("\n")
        saidaResul.write("MELHOR FO GERAL:" + str(self.executaBT.melhorFOGeral) + "\n")
        saidaResul.write("PIOR FO GERAL:" + str(self.executaBT.piorFOGeral) + "\n")

        saidaResul.write("\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! TEMPOS !!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
        saidaResul.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + "\n")

        saidaResul.write("\n")
        saidaResul.write("TEMPO LEITURA INSTANCIA:" + str(self.tempoInst) + "\n")
        saidaResul.write("TEMPO TOTAL GERACAO SOLUCOES INCIAIS:" + str(self.tempoSolInicial) + "\n")
        saidaResul.write("TEMPO TOTAL EXECUCAO DA BT COM MULTISTART:" + str(self.tempoExecBT) + "\n")

        # fecha o arquivo
        saidaResul.close()

        return