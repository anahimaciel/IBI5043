import math
import numpy as np
import random
import pandas as pd
import itertools as it

def randomWalk(initialNet,initialState,steps,probChangeArray,probNetworksArray):   
   #Dicionários
   STdicts={
            'R1': {'000': '000', '001': '000', '010': '101', '011': '001', '100': '010', '101': '010', '110': '111', '111': '011'},
            'R2': {'000': '000', '001': '110', '010': '000', '011': '010', '100': '001', '101': '111', '110': '001', '111': '011'},
            'R3': {'000': '001', '001': '011', '010': '001', '011': '111', '100': '000', '101': '010', '110': '000', '111': '110'},
            'R4': {'000': '010', '001': '010', '010': '011', '011': '111', '100': '000', '101': '000', '110': '001', '111': '101'},
            'R5': {'000': '001', '001': '001', '010': '000', '011': '100', '100': '011', '101': '011', '110': '010', '111': '110'}
            }
   IDdicts={
           '000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7
           }

   freqs=np.zeros(len(IDdicts))
   probs=np.zeros(len(IDdicts))
   presentState=initialState
   presentNet=initialNet
   freqs[IDdicts[presentState]]+=1

   for i in range(steps):
      contextChanges=random.choices([True,False],weights=np.flip(probChangeArray)) #sorteia se muda ou não
      if(contextChanges[0]):
         presentNet=random.choices(['R1','R2','R3','R4','R5'],weights=probNetworksArray/100)[0] #se muda, sorteia pra qual muda
         presentState=STdicts[presentNet][presentState]
         freqs[IDdicts[presentState]]+=1
      else:
         presentState=STdicts[presentNet][presentState]
         freqs[IDdicts[presentState]]+=1

   probs=freqs/steps
   return np.around(probs,3)

#inputs
initialNet=input("ini_net: ").strip()
initialState=input("ini_state: ")
steps=int(input("steps: ")) #trnasformar em inteiro
probChange=input("p_change: ")
probNetworks=input("Prob: ")

#arrays
probChangeArray = np.fromstring( probChange, dtype=float, sep=',' )
probNetworksArray = np.fromstring( probNetworks, dtype=float, sep=',' )

#estados
S=[0,1]
states= np.array([list(pair) for pair in it.product(S, repeat=3)]) #estados possíveis para ngenes genes

#passeio aleatório
random.seed(0) #inicializar o gerador aleatório
probs=randomWalk(initialNet,initialState,steps,probChangeArray,probNetworksArray)

print("Long-Run Relative Frequencies:")

for i in range(len(states)):
    print(''.join(map(str,states[i].tolist())) + '\t ' + str(probs[i]))


