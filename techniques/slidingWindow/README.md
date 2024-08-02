## Padrões | Pseudocódigos [PT-BR] 🇧🇷

* **Max Average Substring**

**Parâmetros**: nums, k (tamanho da janela)

- Variával para armazenar média (Inicial = -inf)
- Váriável para soma atual (Inicial = 0)
- LOOP:
    - Acumular soma
    - Caso i seja maior que k - 1 (tamanho de janela válido):
        - Pega a média (divide a soma por k)
        - Compara a média capturada com a média existente
        - Diminuir a soma acumulada pelo primeiro valor a esquerda (Fecha a janela a esquerda)
    - retornar a janela

- Fórmulas: | i >= k - 1 | & | nums[i - k + 1] |

#

* **Minimum Size Subarray Sum**

**Parâmetros**: nums, target

- Variável para armazenar soma (Inicialmente vale 'inf')
- Variável para armazenar length minimun (Inicialmente vale 0)
- Variável para gravar valor inicial - inicio da janela (start = 0)

- Loop:
    - Acumular soma
    - Enquanto soma atual ser maior ou igual ao target:
        - Comparar o valor de lenght com o tamanho da janela | nums[i - start + 1] |
        - Diminui a soma acumulada pelo primeiro valor da janela | nums[start] |
        - Fechar a janela na esquerda (start += 1)
    - Retornar o lenght minimum

#

* **Fruit Into Baskets**

**Parâmetros**: fruits: List

- Hash para armazenar frequências: {}
- Variável para gravar o valor inicial - inicio da janela (start = 0)
- Variável para armazenar tamanho da janela / quantidade de frutas

- Loop:
    - Se fruits[i] está no hash:
        - Valor de fruits[i] soma 1
    - Caso contrário:
        - Valor de fruits[i] se torna 1

    - Enquanto o tamanho do hash (tamanho da cesta) for maior de que 2:
        - Diminui 1 do valor da cesta associado a fruta nums[start]
        - Se o valor do hash for 0 (quantidade de frutas chegou a zero):
            - fruta é deletada do hash
        - Fechar a janela na esquerda (start += 1)

    - Comparar a variavel de tamanho da janela com o tamanho atual |i - start + 1|
    - Retornar tamanho da janela

#

* **Permutation in String**

**Parâmetros** : s1: str, s2: str

- Variável para tamanho de s1
- Variável para frequencias de s1 (Counter from collections)

- Loop por s2:
    - Caso i seja maior que len(s1) - 1 (tamanho de janela válido):
        - Captura as frequencias do tamanho da janela (Counter(s2[i - len(s1) + 1: i + 1]))
        - Caso as frequencias dos chars da janela sejam iguais a frequencia de s1:
            - return True

    return False

#

* **Longest Repeating Character Replacement**

**Parâmetros**: s: str, k: int

- Variável para armazenar longest_substr
- Variável para gravar o inicio da janela (start = 0)
- Hash para armazenar frequências
- Variável para armazenar máxima frequência de um char em uma janela

- Loop:
    - Adiciona o char no hash com o value sendo a frequencia | freq[s[end]] = 1 + freq.get(s[end], 0) |
    - Compara a frequência maxima entre a max_freq atual com o armazenado no hash | max_freq = max(max_freq, freq[s[end]]) |

    - Enquanto o tamanho da janela - frequencia maxima for maior que k:
        - Frequencia do char inicial (start) diminui 1
        - janela fecha 1 (start += 1)

    - Compara o longest_substr com o tamanho da janela |longest_substr = max(longest_substr, end - start + 1)|
    - Retorna o tamanho da janela

#

* **Longest Substring Without Repeating Characters**

**Parâmetros**: s: str

- Variável para armazenar longest_substr
- Variável para gravar o inicio da janela (start = 0)
- Set para gravar repetições

- Loop:
    - Enquanto o char está no set:
        - Remove o char do set
        - janela fecha 1 (start += 1)

    - Adiciona o char atual no set
    - Compara o longest_substr com o tamanho da janela
    - Retorna o tamanho da janela

--------------------

## Patterns | Pseudocodes [EN] 🇺🇸

* **Max Average Substring**

**Parameters**: nums, k (window size)

- Variable to store average (Initial = -inf)
- Variable to store current sum (Initial = 0)
- LOOP:
    - Accumulate sum
    - If i is greater than k - 1 (valid window size):
        - Compute the average (divide the sum by k)
        - Compare the captured average with the existing average
        - Decrease the accumulated sum by the first value on the left (Close the window on the left)
    - Return the window

- Formulas: | i >= k - 1 | & | nums[i - k + 1] |

* **Minimum Size Subarray Sum**

**Parameters**: nums, target

- Variable to store sum (Initially 'inf')
- Variable to store minimum length (Initially 0)
- Variable to track initial value - start of the window (start = 0)

- Loop:
    - Accumulate sum
    - While current sum is greater than or equal to the target:
        - Compare the length with the window size | nums[i - start + 1] |
        - Decrease the accumulated sum by the first value of the window | nums[start] |
        - Close the window on the left (start += 1)
    - Return the minimum length

* **Fruit Into Baskets**

**Parameters**: fruits: List

- Hash to store frequencies: {}
- Variable to track initial value - start of the window (start = 0)
- Variable to store window size / quantity of fruits

- Loop:
    - If fruits[i] is in the hash:
        - Value of fruits[i] increment by 1
    - Else:
        - Value of fruits[i] becomes 1

    - While the size of the hash (number of baskets) is greater than 2:
        - Decrease 1 from the value in the basket associated with fruit nums[start]
        - If the hash value is 0 (quantity of fruits reaches zero):
            - Fruit is deleted from the hash
        - Close the window on the left (start += 1)

    - Compare the window size variable with the current size | i - start + 1 |
    - Return window size

* **Permutation in String**

**Parameters**: s1: str, s2: str

- Variable for size of s1
- Variable for frequencies of s1 (Counter from collections)

- Loop through s2:
    - If i is greater than len(s1) - 1 (valid window size):
        - Capture the frequencies of the window size (Counter(s2[i - len(s1) + 1: i + 1]))
        - If the frequencies of the chars in the window match the frequencies of s1:
            - return True

    return False

* **Longest Repeating Character Replacement**

**Parameters**: s: str, k: int

- Variable to store longest_substr
- Variable to track the start of the window (start = 0)
- Hash to store frequencies
- Variable to store maximum frequency of a char in a window

- Loop:
    - Add the char to the hash with the value being the frequency | freq[s[end]] = 1 + freq.get(s[end], 0) |
    - Compare the maximum frequency between the current max_freq and the stored frequency in the hash | max_freq = max(max_freq, freq[s[end]]) |

    - While the window size - maximum frequency is greater than k:
        - Frequency of the initial char (start) decreases by 1
        - Window closes 1 (start += 1)

    - Compare longest_substr with the window size | longest_substr = max(longest_substr, end - start + 1) |
    - Return the window size


* **Longest Substring Without Repeating Characters**

**Parameters**: s: str

- Variable to store longest_substr
- Variable to track the start of the window (start = 0)
- Set to track repetitions

- Loop:
    - While the char is in the set:
        - Remove the char from the set
        - Close the window by moving the start index (start += 1)

    - Add the current char to the set

    - Compare longest_substr with the size of the window
    - Return the size of the window