Faça um programa que leia uma matriz do teclado linha por linha (opção: 1) ou de um arquivo (opção: 2) com os valores de expressão gênica de m genes de n pacientes, calcule a correlação de Pearson dos genes par a par e imprima a matriz de correlação. Utilize numpy.around() para arredondar os números.

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
