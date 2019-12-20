class Solucao():

    def __init__(self, instancia):

        # define a instancia com os valores iniciais
        self.instancia = instancia

        # cria a matriz que ira conter o agrupamento da solucao
        self.solucaoGrupos = [[] for i in range(0, self.instancia.G)]

        # cria o array que contem o somatorio das distancias para cada grupo
        # representa a diversidade em cada grupo
        self.distTotalGrupo = [0 for i in range(0, self.instancia.G)]

        # parametro correspondente a diversidade total
        # somatorio das diversidades de cada grupo
        self.divTotal = 0

        # inclui o tempo que levou para ser gerada
        self.tempoGer = 0

        # inclui o tempo que levou para atingir o otimo
        self.tempoOtimo = 0

        # inclui a melhor solucao gerada no multistart
        self.melhorFO = 0

        # inclui a pior solucao gerada no multistart
        self.piorFO = 999999999

        return
