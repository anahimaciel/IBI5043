Faça um programa que tenha como entrada o nome de um arquivo texto com:
* Parâmetros α
 e β
 de perturbação
* nome dos genes
* matriz de regulação

E retorne:
* Para cada gene sua CPT
* Probabilidades estacionárias dos estados do caminho biológico

Há um passo intermediário que é a matriz de probabilidades. O código não deverá imprimi-la na avaliação.
A entrada do programa é só o nome do arquivo.
Exemplo de arquivo (arquivo1.txt):

2.3
2.3
A,B,C,D
0,0,0,-1
0,-1,0,1
1,-1,0,0
0,0,1,0

Para o "passeio probabilístico" utilize a biblioteca random do python. (https://docs.python.org/3/library/random.html)
Inicialize com random.seed(0) apenas uma vez no início do código.
Utilize a função choice para sortear o estado inicial para começar o passeio
Utilize a função choices para sortear cada passo (sorteios probabilísticos como um "dado viciado"), leia a documentação.
Faça 20.000 sorteios para os passos do passeio contando quantas vezes aparece cada estado. A probabilidade será a frequência desta contagem (ou seja, divida por 20.000)

Se quiser, utilize a biblioteca pandas para armazenar as tabelas e imprima com duas casas decimais.
pd.options.display.float_format = '{:,.2f}'.format

Para imprimir os dataframes utilize:
print(df.to_string(index=False)) 
ou 
print(df.to_string(dtype=False))

O Exemplo de execução está no template.
