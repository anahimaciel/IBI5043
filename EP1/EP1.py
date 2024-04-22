'''
Faça um programa que leia a matriz do arquivo adjSigned.csv com os valores de adjacência de m genes.
Calcule a Topological Overlap Matrix (TOM) (a partir da matriz de adjacência para redes "signed" ou "unsigned" e para variantes que considerem a mínima conetividade ou a média das conetividades) dos m genes e imprima o valor para o par de genes solicitado. Utilize numpy.around(decimals=4) para arredondar os números.

Exemplo de execução:

Nome do arquivo: adjSigned.csv
Tipo de rede TOM: signed
Variante TOM (min ou mean): min
Index do primeiro gene: 0
Index do segundo gene: 5

0.0325

Parâmetros sugeridos
        Calculation of the topological overlap matrix from a given adjacency matrix
        :param adjMat: adjacency matrix, that is a square, symmetric matrix with entries between 0 and 1 (negative values are allowed if TOMType=="signed").
        :type adjMat: numpy array
        :param TOMType: one of "unsigned", "signed"
        :type TOMType: str
        :param TOMDenom: a character string specifying the TOM variant to be used. Recognized values are "min" giving the standard TOM described in Zhang and Horvath (2005),
                         and "mean" in which the min function in the denominator is replaced by mean. 
        :type TOMDenom: str
        :return: A matrix holding the topological overlap.
        :rtype: numpyt array
'''

import math 
import numpy as np

def tom(gene1, gene2,colunas):

  # Computar TOM: O cálculo da TOM precisa do correto cálculo no denominador e no numerador. Analise a fórmula da TOM comentada na aula.
  # No numerador calculamos a multiplicação das adjacências para todo gene "i" e "j" com um gene vizinho "u". Se calcularmos para a matriz de adjacência completa, o cálculo fica representado por um "dot product".
  L = 0 # complete o código para a variável da somatória de multiplicação de adjências.
  for u in range(colunas):
    L += adjMat[gene1,u]*adjMat[u,gene2] #cálculo da somatória
  num=L+adjMat[gene1,gene2] #cálculo do numerador

  # No denominador temos a conetividade para cada gene do par "i" e "j". A conetividade é a soma da adjacência do gene com todos os outros da matriz. Dado que a matriz é simétrica, vamos consider um gene das filas e o outro das colunas.
  ki = np.sum(adjMat,axis=0)[gene1] #complete o código para calcular a conetividade dos genes das colunas
  kj = np.sum(adjMat,axis=1)[gene2] #complete o código para calcular a conetividade dos genes das filas  

  if TOMDenom == "min":  # cálculo do primeiro termo do denominador quando a variante da TOM seleciona a mínima conetividade. 
    k=min(ki,kj)
  else:   #cálculo do primeiro termo do denominador quando a variante da TOM usa a média da conetividade.
    kSum=ki+kj
    k=kSum/2
  
  if TOMType == "unsigned":  # unsigned TOM, como descrito na fórmula
      den=k+1-adjMat[gene1,gene2] #cálculo do denominador
      value = num/den  #cálculo do valor final
  else:  # signed TOM, onde o numerador e a matriz de adjacência do denominador são transformados em valores positivos.
      den=k+1-math.fabs(adjMat[gene1,gene2]) #cálculo do denominador
      value = math.fabs(num)/den #cálculo do valor final
  return np.round(value,4)

arq = input("Nome do arquivo: ").strip()
TOMType = input("Tipo de rede TOM: ")
TOMDenom = input("Variante TOM (min ou mean): ")
a = int(input("Index do primeiro gene: "))
b = int(input("Index do segundo gene: "))

# Prepare a matriz de adjacência: vamos calcular os valores para a matriz completa.
with open(arq) as f:
    ncols = len(f.readline().split(','))
adjMat = np.loadtxt(arq, delimiter=',', skiprows=1, usecols=range(1,ncols))

# Dado que a adjacência de gene "i" com o gene "i" não é considerado na fórmula, vamos zerar (função do numpy) esses valores na matriz de adjacência para facilitar o cálculo da conetividade e a multiplicação de matrices.
#escreva o código aqui
np.fill_diagonal(adjMat, 0)

#A TOM final recupera os valores para os pares gene "i" com gene "j"
#escreva o código aqui
col=ncols-1
tomMatrix=np.zeros((col,col))
for i in range(col):
  for j in range(i+1):
    if(i==j):
      tomMatrix[i][j]=1
    else:
      tomMatrix[i][j]=tom(i,j,col)
      tomMatrix[j][i]=tomMatrix[i][j]

# Retorne o valor para o par de genes solicitados
#escreva o código aqui
print(tomMatrix[a][b])
