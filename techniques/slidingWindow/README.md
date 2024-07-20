# Saída esperada: [3, 3, 5, 5, 6, 7] - SumMaxSubset

Dica: Use uma deque para manter os índices dos elementos candidatos para o máximo.
Exercício 2: Soma Máxima de Subarray com Tamanho Fixo

Descrição: Dada uma lista de inteiros arr e um número inteiro k, encontre a soma máxima de qualquer subarray contíguo de tamanho k.

Exemplo:

arr = [2, 1, 5, 1, 3, 2]
k = 3

# Saída esperada: 9 (subarray [5, 1, 3]) - SubstringPalindrome

Dica: Mantenha uma soma acumulada e atualize-a enquanto a janela deslizante se move.
Exercício 3: Contagem de Palíndromos em Substrings de Tamanho Fixo

Descrição: Dada uma string s e um número inteiro k, conte quantas substrings contíguas de tamanho k são palíndromos.

Exemplo:

s = "abbaacc"
k = 4

# Saída esperada: 2 (substrings "abba" e "bbaa" são palíndromos)

Dica: Verifique se cada substring de tamanho k é um palíndromo.
Exercício 4: Subarrays com Soma Máxima

Descrição: Dada uma lista de inteiros arr e um número inteiro k, encontre a soma máxima de qualquer subarray contíguo que tenha uma soma menor ou igual a k.

Exemplo:

arr = [1, 2, 3, 4, 5]
k = 11

# Saída esperada: 10 (subarray [2, 3, 4, 1])

Dica: Use a técnica de janela deslizante para manter a soma atual e ajustar a janela para manter a soma dentro do limite.
Exercício 5: Substring com Caracteres Únicos

Descrição: Dada uma string s e um número inteiro k, encontre a substring mais longa com exatamente k caracteres únicos.

Exemplo:

s = "araaci"
k = 2

# Saída esperada: 4 (substring "araa")

Dica: Use um dicionário para contar a frequência de caracteres dentro da janela deslizante e ajuste a janela para manter exatamente k caracteres únicos.
Exercício 6: Distância Máxima entre Repetições

Descrição: Dada uma string s e um número inteiro k, encontre a distância máxima entre as repetições de uma substring de tamanho k.

Exemplo:

s = "abcababc"
k = 3

# Saída esperada: 6 (substring "abc" aparece em posições 0 e 6)

Dica: Mantenha um dicionário para armazenar as posições de ocorrência de cada substring de tamanho k.
Exercício 7: Subarray com Mínima Diferença

Descrição: Dada uma lista de inteiros arr e um número inteiro k, encontre o subarray contíguo de tamanho k cuja soma é a mais próxima de um valor alvo target.

Exemplo:

arr = [1, 2, 3, 4, 5]
k = 3
target = 10

# Saída esperada: 9 (subarray [2, 3, 4] tem soma mais próxima de 10)

Dica: Mantenha a soma do subarray e atualize a diferença em relação ao alvo enquanto move a janela.
Exercício 8: Número de Subarrays com Soma Exatamente K

Descrição: Dada uma lista de inteiros arr e um número inteiro k, encontre o número de subarrays contíguos cuja soma é exatamente k.

Exemplo:

arr = [1, 1, 1, 1, 1]
k = 2

# Saída esperada: 4 (subarrays [1, 1], [1, 1], [1, 1], [1, 1])

Dica: Use uma soma acumulada e um dicionário para armazenar a frequência das somas acumuladas.
Exercício 9: Máximo Elemento Distante

Descrição: Dada uma lista de inteiros arr e um número inteiro k, para cada posição na lista, encontre o máximo elemento em qualquer janela de tamanho k que inclui essa posição.

Exemplo:

arr = [1, 3, 1, 2, 5, 4]
k = 3

# Saída esperada: [3, 3, 5, 5, 5] (para cada posição na janela)

Dica: Utilize a abordagem de deque para manter os índices do máximo dentro da janela.
Exercício 10: Mínimo Elemento Distante

Descrição: Dada uma lista de inteiros arr e um número inteiro k, para cada posição na lista, encontre o mínimo elemento em qualquer janela de tamanho k que inclui essa posição.

Exemplo:

arr = [1, 3, 1, 2, 5, 4]
k = 3

# Saída esperada: [1, 1, 1, 2, 4] (para cada posição na janela)

Dica: Utilize a abordagem de deque para manter os índices do mínimo dentro da janela.
