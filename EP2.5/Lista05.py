'''
Faça um programa que leia uma matriz de um arquivo com os valores de expressão gênica de m genes de n pacientes.
Calcule a matriz de adjacência (em função da correlação de Pearson para redes "signed" e "unsigned") dos m genes e imprima a adjacência para o par de genes solicitado.
Utilize numpy.around(decimals=4) para arredondar os números.

Exemplo de execução:

Nome do arquivo: datExpr.csv
Tipo de rede de adj.: signed
Soft thresholding power (beta): 6
Index do primeiro gene: 0
Index do segundo gene: 5
0.0232

'''
"""Sugestão de parâmetros:
    Calculates (correlation or distance) network adjacency from given expression data or from a similarity
    :param datExpr: data frame containing expression data. Columns correspond to genes and rows to samples.
    :type datExpr: pandas dataframe
    :param adjacencyType: adjacency network type. Allowed values are "unsigned", "signed".
    :type adjacencyType: str
    :param power: soft thresholding power.
    :type power: int
    :param geneA: First gene of the adjacency to be printed.
    :type power: int
    :param geneB: Second gene to print adjacency with first gene.
    :type power: int
    :return: Adjacency
    :rtype: float64
"""
#Escreva seu código aqui
import math
import numpy as np

def cor(colGene1,colGene2,nrows,medias1,medias2):  #função que calcula a correlação entre dois genes
    r = 0.0
    a=0.0
    b=0.0
    for i in range(nrows):
        a += (colGene1[i]-medias1)**2
        b += (colGene2[i]-medias2)**2
    for i in range(nrows):
        r += (colGene1[i]-medias1)*(colGene2[i]-medias2)/math.sqrt(a*b)
    r = np.around(r,4)
    return r


arq = input("Nome do arquivo: ").strip()
tipoRede = input("Tipo de rede de adj.: ")
beta = int(input("Soft thresholding power (beta): "))
gene1 = int(input("Index do primeiro gene: "))
gene2= int(input("Index do segundo gene: "))

with open(arq) as f:
    ncols = len(f.readline().split(','))
genMat = np.genfromtxt(arq, delimiter=',', skip_header=1,  missing_values="NA", filling_values=0, usecols=range(1,ncols)) #matriz com os dados do arquivo

ncols = ncols-1  #número de genes
nrows = len(genMat) #número de pacientes

medias=np.mean(genMat,axis=0)  #médias dos genes


#calcular e retornar o valor da adjacência para os genes especificados
if(tipoRede.lower()=="unsigned"):  
    p = math.fabs(cor(genMat[:,gene1],genMat[:,gene2],nrows,medias[gene1],medias[gene2])) 
            
elif(tipoRede.lower()=="signed"):
    p=math.fabs(0.5+0.5*cor(genMat[:,gene1],genMat[:,gene2],nrows,medias[gene1],medias[gene2]))

else:  
    print("Modo não disponível")

print(np.around(p**beta,4))
