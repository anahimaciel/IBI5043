'''
Faça um programa que tenha como entrada o nome de um arquivo texto
e retorne:

Para cada gene sua CPT
Probabilidades estacionárias dos estados do caminho biológico

Exemplo do arquivo texto - arquivo1.txt

0.5
0.5
A,B,C
-1,0,1
-1,-1,0
1,1,0

Exemplo de execução:

arquivo: arquivo1.txt
Conditional Probability Tables
 A(t)  C(t)  ProbA(t+1)=0  ProbA(t+1)=1
    0     0          0.62          0.38
    0     1          0.27          0.73
    1     0          0.73          0.27
    1     1          0.38          0.62
 A(t)  B(t)  ProbB(t+1)=0  ProbB(t+1)=1
    0     0          0.62          0.38
    0     1          0.73          0.27
    1     0          0.73          0.27
    1     1          0.88          0.12
 A(t)  B(t)  C(t)  ProbC(t+1)=0  ProbC(t+1)=1
    0     0     0          0.62          0.38
    0     0     1          0.38          0.62
    0     1     0          0.27          0.73
    0     1     1          0.27          0.73
    1     0     0          0.27          0.73
    1     0     1          0.27          0.73
    1     1     0          0.12          0.88
    1     1     1          0.12          0.88

Steady State Probability
000   0.10
001   0.22
010   0.04
011   0.08
100   0.12
101   0.29
110   0.05
111   0.11
'''

#seu código aqui

import numpy as np 
import pandas as pd
import itertools as it #módulo do python de iteradores
import math
import random

def CPT(regMat,regsArray,ngene,estado,alpha,beta): #função que calcula as probabilidades e as retorna
   h = 0   #input signal
   j= 0
   prob=[0,0]
   for i in range(len(regMat)):
      if(str(i) in regsArray):
         h += regMat[ngene][i]*estado[j] #calculando input signal
         j=j+1
   if(h==0):                              #calculando as probabilidades conforme a fórmula dada em aula
      if(estado[regsArray.index(str(ngene))]==0):
         prob[0]=float(1/(1+math.exp(-1*alpha)))
         prob[1]=1-prob[0]
      else:
         prob[1]=float(1/(1+math.exp(-1*alpha)))
         prob[0]=1-prob[1]
   else:
      prob[1]= float(math.exp(beta*h)/(math.exp(beta*h)+math.exp(-1*beta*h)))
      prob[0]=1-prob[1]
   return np.around(prob,2)

def dataGen(regMat,regs,ngene,alpha,beta): #função que retorna os dados de cada coluna do dataframe
   S=[0,1]
   regsArray = regs.split()
   estados = np.array([list(pair) for pair in it.product(S, repeat=len(regsArray))])
   probMat = np.zeros((len(estados),2))
   data = np.zeros((len(estados),len(regsArray)+2))
 
   for j in range(len(estados)): #tem que fazer o cpt para cada estado j
      probMat[j]=CPT(regMat,regsArray,ngene,estados[j],alpha,beta)
      data[j]=np.append(estados[j],probMat[j])
   return data

def whichState(regs, estado): #função que retorna a qual estado dos reguladores de cada gene corresponde um certo estado
   regsArray=regs.split()
   estadoGene=np.zeros(len(regsArray),dtype=int)
   j=0
   for i in regsArray:
      estadoGene[j]=estado[int(i)]
      j=j+1
   return estadoGene

def randomWalk(length,estados,probMat): #função que faz o passeio aleatório e retorna uma lista com as probabilidades calculadas
   presentState = random.choice(estados) #faz o sorteio do estado inicial
   freqs=np.zeros(len(estados))
   probs=np.zeros(len(estados))
   index=estados.index(presentState)
   for i in range(length):
      presentState=random.choices(estados, weights=probMat[index]) #faz o sorteio do próximo estado
      index=estados.index(presentState[0])
      freqs[index]+=1 #aumenta a frequência do estado em 1
   probs=freqs/length
   return probs

arq = input("Nome do arquivo: ").strip()

with open (arq) as f:
   lines = f.readlines()
   alpha=float(lines[0].strip())
   beta=float(lines[1].strip())
   genes=lines[2].split(",")

ngenes = len(genes) #número de genes
regMat = np.loadtxt(arq, delimiter=',', skiprows=3) #matriz de regulação (tipo: float)
columns = ["" for x in range(ngenes)]
regs = ["" for x in range(ngenes)] #lista dos genes reguladores de cada gene

#para as probabilidades de estado estacionário
random.seed(0) #inicializar o gerador aleatório
S=[0,1]
estados= np.array([list(pair) for pair in it.product(S, repeat=ngenes)]) #estados possíveis para ngenes genes
probMat=np.zeros((len(estados),len(estados))) #matriz de probabilidades, para cada estado temos de achar a probabilidade dele ir para cada estado
probs = np.zeros((ngenes)) #probabilidade de cada gene mudar de forma a produzir um certo estado final

#para fazer os títulos das colunas do dataframe das probabilidades condicionais
for i in range(ngenes):
   for j in range(len(regMat[i])):
      if(i==j):   
         columns[i]=columns[i] +genes[j].strip()+"(t) "
         regs[i]=regs[i] +str(j) + " "
      else:
         if (regMat[i][j] != 0):
            columns[i]=columns[i] +genes[j].strip()+"(t) "
            regs[i]=regs[i] + str(j) +" "
   columns[i]=columns[i] + "Prob" + genes[i].strip() + "(t+1)=0"+ " " +"Prob" + genes[i].strip() + "(t+1)=1"

#para calcular a matriz de probabilidades
for i in range(len(estados)):
   for j in range(len(estados)):
      for k in range(ngenes):
         estadoGene=whichState(regs[k], estados[i])
         if (str(estados[j]).replace(" ", "")[1:-1][k] == str(1)):
            probs[k]=CPT(regMat,regs[k].split(),k,estadoGene,alpha,beta)[1]
         else:
            probs[k]=CPT(regMat,regs[k].split(),k,estadoGene,alpha,beta)[0]
      probMat[i][j]=np.prod(probs)

SteadyState=randomWalk(20000,estados.tolist(),probMat) #lista com as probabilidades do estado estacionário

print("Conditional Probability Tables")

for i in range(ngenes):
   data= dataGen(regMat,regs[i],i,alpha,beta)
   df=pd.DataFrame(data = data, columns = columns[i].split()) 
   print(df.to_string(index=False))

print("\nSteady State Probability")

for i in range(len(estados)):
    print(''.join(map(str,estados[i].tolist())) + '\t ' + str(np.around(SteadyState[i],2)))
