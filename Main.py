from Instancia import Instancia
from SolInicial import SolInicial
from Solucao import Solucao
from BuscaTabu import BuscaTabu
from SaidaBT import SaidaBT

import time

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# INICIO DO PROGRAMA  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ESCREVER AQUI O NOME DA INSTANCIA UTILIZADA
nomeInst = "Geo_n010_ds_01"
caminho = "F:\Cadu\metaheuristicas\instancias\Geo"

# le instancia com dados de entrada
start_time = time.time()
instancia = Instancia(caminho + "\\" + nomeInst + ".txt")
tempoInst = time.time() - start_time
print("LEU INSTANCIA")

# CADA INSTANCIA DEVE SER RODADA 5 VEZES, POR ISSO:
for i in range(0,5):

    # gera a solucao
    solucao = Solucao(instancia)

    # gera as solucoes iniciais
    start_time = time.time()
    sol_inicial = SolInicial(instancia, solucao)
    tempoSolInicial = time.time() - start_time
    print(str(i+1) + ") GEROU SOLUCOES INICIAIS")

    # O objeto da classe Solucao esta populado com a solucao inicial, por isso ele eh passado por parametro
    start_time = time.time()
    executaBT = BuscaTabu(i, nomeInst, instancia, solucao, sol_inicial)
    tempoExecBT = time.time() - start_time
    print(str(i+1) + ") TERMINOU BT")

    # cria uma instancia da classe SaidaBt e passa todos os parametros para gerar os arquivos txt
    geraSaida = SaidaBT(i, nomeInst, tempoInst, tempoSolInicial, tempoExecBT, instancia, solucao, sol_inicial, executaBT)

    print(str(i+1) + ") ACABOU CERTO")

    del solucao
    del sol_inicial
    del executaBT
    del geraSaida

print("ACABOU TUDO!")