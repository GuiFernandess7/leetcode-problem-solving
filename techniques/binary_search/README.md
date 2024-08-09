## Find Smallest Letter Greater Than Target

( https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/ )

- Inicializar ponteiro esquerdo l = 0
- Inicializar ponteiro direito r = len(letters) - 1

- Enquanto l <= r:
    - Calcular o valor do meio: mid = l + (r - l) // 2
    - Se letters[mid] <= TARGET:
        - Atualizar ponteiro l: l = mid + 1
    - Caso contrário:
        - Atualizar ponteiro r: r = mid - 1

- Após o loop:
    - Se l < len(letters):
        - Retornar letters[l]
    - Caso contrário:
        - Retornar letters[0]

#

## Find Minimum in Rotated Sorted Array

( https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/ )

- Inicializar ponteiro esquerdo l = 0
- Inicializar ponteiro direito r = len(nums) - 1
- Inicializar output: res = nums[0]

- Enquanto l <= r:
    - Se nums[l] < nums[r]:
        res = min(res, nums[l])
        break

    - Inicializa m: m = (l + r) // 2
    - Atualiza res: res = min(res, nums[m])
    - Se nums[m] >= nums[l]:
        - l = m + 1
    - Caso contrário:
        - r = m - 1

    - Retorna res

#

## Search in Rotated Sorted Array

( https://leetcode.com/problems/search-in-rotated-sorted-array/description/ )

- Inicializar ponteiro esquerdo l = 0
- Inicializar ponteiro direito r = len(nums) - 1

- Enquanto l <= r:
    - Inicializar m: m = (l + r) // 2

    - Se nums[m] igual a target:
        - Retornar m

    - Se nums[l] <= nums[m]:
        - Se nums[l] <= target < nums[m]:
            - Atualizar r = m - 1
        - Caso contrário:
            - Atualizar l = m + 1

    - Caso contrário:
        - Se nums[m] < target <= nums[r]:
            - Atualizar l = m + 1
        - Caso contrário:
            - Atualizar r = m - 1

- Retornar -1  // Target não encontrado
