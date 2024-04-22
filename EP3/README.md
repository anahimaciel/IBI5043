Faça um programa que tenha como entrada os parâmetros :
* Rede inicial do sistema
* Estado inicial da rede selecionada
* Número de passos
* Probabilidade de mudança de contexto (separadas por vírgula)
* Probabilidade de seleção para cada rede do sistema (separadas por vírgula).

E retorne:
* As frequências relativas para cada possível estado no final dos passos

As interações dos elementos estão representados na imagem dos grafos de cada rede.

Há um passo intermediário que é calcular a transição de estados para cada rede do sistema. Se quiser, faça a transição na mão e coloque no código. O código não deverá imprimi-la na avaliação.

Para o "passeio probabilístico" utilize a biblioteca random do python. (https://docs.python.org/3/library/random.html)
Inicialize com random.seed(0) apenas uma vez no início do código.
Utilize a função choice para sortear se haverá ou não troca de contexto.
Utilize a função choices para sortear cada passo usando a probabilidade de cada rede. Diferencie os casos quando há ou não troca de contexto.
Após terminar todos os passos indicados no input, calcule probabilidade (frequência de contagem) para cada possível estado.

Imprima até 3 casas decimais.

O Exemplo de execução está no template.
