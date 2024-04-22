'''
Faça um programa que leia uma matriz do teclado linha por linha (opção: 1) ou 
de um arquivo (opção: 2) com os valores de expressão gênica de  m  genes 
de  n  pacientes, calcule a correlação de Pearson dos genes par a par e 
imprima a matriz de correlação. 
Utilize numpy.around() para arredondar os números.

Exemplo de execução 1:

digite opção: 1
quantos genes (m): 3
gene 1: 47.0, 52.0, 23.0, 76.0, 95.0, 68.0, 34.0, 32.0, 37.0, 69.0
gene 2: 203.0, 207.0, 220.0, 179.0, 154.0, 190.0, 199.0, 235.0, 220.0, 184.0
gene 3: 504.0, 507.0, 480.0, 513.0, 508.0, 508.0, 486.0, 502.0, 491.0, 511.0
[[ 1. -0.918 0.795]
[-0.918 1. -0.551]
[ 0.795 -0.551 1. ]]

Exemplo de execução 2:

digite opção: 2
nome do arquivo: arquivo1.csv
[[ 1. -0.918 0.795]
[-0.918 1. -0.551]
[ 0.795 -0.551 1. ]]


'''
# escreva seu código aqui 

import math
import numpy

def cor(gene1,gene2, geneLen, medias1, medias2):
    r = 0.0
    a=0.0
    b=0.0
    for i in range(geneLen):
        a += (gene1[i]-medias1)**2
    for i in range(geneLen):
        b += (gene2[i]-medias2)**2
    for i in range(geneLen):
        r += (gene1[i]-medias1)*(gene2[i]-medias2)/math.sqrt(a*b)
    r = numpy.around(r,3)
    return r

opcao = input ("digite opção: ")

if (int(opcao) == 1):
    strNum = input("quantos genes (m): ")
    intNum = int(strNum)
    genes = [None] * intNum
    medias = [None] * intNum
    
    for x in range(intNum):
        genes[x] = input("gene " + str(x+1) + ":").split(", ") #é uma lista
        for y in range(len(genes[x])):
            genes[x][y] = float(genes[x][y])
        medias[x] = sum(genes[x])/len(genes[x])
    
    matriz = [ [ None for y in range(intNum) ] for x in range(intNum) ]
    
    for x in range(intNum):
        for y in range(intNum):
            matriz[x][y]= cor(genes[x],genes[y],len(genes[x]), medias[x],medias[y])
     
    matriz = numpy.array(matriz)
    print(matriz)
    
elif(int(opcao) == 2):
    nome = input("nome do arquivo: ")
    arq = open(nome)
    lista = arq.readlines()
    genes = [None] * (len(lista)-1)
    medias = [None] * (len(lista)-1)
    novoGenes = [0.0] * (len(lista)-1)
    
    for i in range(len(lista)-1):
        genes[i]=lista[i+1].split(",")
        for j in range(len(genes[i])-1):
            genes[i][j]=float(genes[i][j+1])
        genes[i][len(genes[i])-1]=0.0
        medias[i]=sum(genes[i])/(len(genes[i])-1)
        
    
    matriz = [ [ None for y in range(len(lista)-1) ] for x in range(len(lista)-1) ]  
    
    for x in range(len(lista)-1):
        for y in range(len(lista)-1):
            matriz[x][y]= cor(genes[x],genes[y],len(genes[x])-1, medias[x],medias[y])
    
    matriz = numpy.array(matriz)
    print(matriz)
    
else:
    print("Opção não disponível")