import time

class Instancia:

    def __init__(self, path):

        self.path = path

        # le o arquivo e armazena os dados no objeto
        self.leituraInstancia()

        return

    def leituraInstancia(self):

        # declara variaveis e abre arquivo
        self.arquivo = open(self.path, "r")
        self.dist = [[]]
        self.limits = [[]]
        self.distOrd = []

        valores = self.arquivo.readline().split(' ')

        # recebe o numero de elementos
        self.M = int(valores[0])

        # declara matriz que recebe as distancias
        self.dist = [[0 for i in range(0, self.M)] for j in range(0, self.M)]

        # recebe o numero de grupos
        self.G = int(valores[1])

        # recebe o tipo de grupo
        self.groupType = valores[2]

        # declara matriz que recebe os limites de cada grupo
        self.limits = [[] for i in range(0, self.G)]

        # recebe os limites de cada grupo
        aux = 3
        for i in range(0, self.G):
            for j in range(aux, aux + 2):
                self.limits[i].append(int(valores[j]))
                aux += 1

        # le as linhas restantes do arquivo
        for linha in self.arquivo.readlines():

            valores = linha.split(' ')

            # armazena as distancias na matriz
            self.dist[int(valores[0])][int(valores[1])] = float(valores[2])
            self.dist[int(valores[1])][int(valores[0])] = float(valores[2])

            # armazena as distancias na lista para construir a solucao gulosa
            self.distOrd.append(valores)

        # fecha o arquivo
        self.arquivo.close()

        # transforma de string pra float e ordena a lista distOrd de maneira decrescente
        # start_time = time.time()
        self.distOrd = [[float(i) for i in self.distOrd[j]] for j in range(0, len(self.distOrd))]
        self.distOrd.sort(reverse = True, key = lambda x: x[2])
        # tempoOrd = time.time() - start_time

        # print("TEMPO DE ORD: " + str(tempoOrd))

        return