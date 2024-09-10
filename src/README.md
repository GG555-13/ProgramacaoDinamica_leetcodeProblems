# 879. Profitable Schemes

Problema: [Profitable Schemes ](https://leetcode.com/problems/profitable-schemes/description/)

**Descrição:** <br>

There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

 

**Example 1:** <br>
**Input:**  n = 5, minProfit = 3, group = [2,2], profit = [2,3]<br>
**Output:** 2 <br>
**Explanation:**  To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.<br>
In total, there are 2 schemes.
<br>

**Example 2:** <br>
**Input:** n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]<br>
**Output:** 7 <br>
**Explanation:** To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).<br>
 

**Constraints:** <br>
1 <= n <= 100 <br>
0 <= minProfit <= 100<br>
1 <= group.length <= 100<br>
1 <= group[i] <= 100<br>
profit.length == group.length<br>
0 <= profit[i] <= 100<br>



## Estrutura do Algoritmo
O algoritmo do `Mochileiro (ou knapsack)` pode ser usado para resolver esse problema. O objetivo nesse caso é sabert como maximar o lucro com um número limitado de pessoas e a o mesmo tempo cumprindo um limite de lucro mínimo.<br>

É possível definir esse problema como uma matriz tridimensional `dp[i][j][k]`, onde:

- i: Número de esquemas (de 0 até i).
- j: Número de pessoas já usadas.
- k: Lucro acumulado (limitado por minProfit).


Para cada esquema i, acontece duas coisas:
- O esquema não é incluido.
- O esquema é incluido se houver pessoas suficientes (j >= group[i]).


O caso base é `dp[0][0][0] = 1`, significando que há uma maneira de ter 0 pessoas e 0 lucro, que é não escolher nada.

O resultado será a soma de todos os `dp[m][j][minProfit]`, onde `m` é o número total de esquemas, dará a resposta, considerando todos os `j <= n`.


### Explicação do Código:

Primeiro como explicado acima a matriz 3D com zeros é inicializada e o número de esquemas disponíveis é armazenado em uma variavel e o caso base é aplicado: <br>
```python
m = len(group)
dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
dp[0][0][0] = 1
```
Após isso a matriz é preenchida para cada caso recursivamente para cada esquema com as duas escolhas discutidas na parte de estrutura do algoritmo:<br>
- Não incluir o esquema i (copiando o valor de `dp[i-1][j][k]`).<br>
- Incluir o esquema i, mas apenas se o número de pessoas j for suficiente. Nesse caso, o valor de `dp[i-1][j - members][max(0, k - earn)]` é aumentado de forma que `k - earn` não fique negativo.<br>
```python
for j in range(n + 1):  
    for k in range(minProfit + 1): 
        dp[i][j][k] = dp[i - 1][j][k]
        if j >= members:
            dp[i][j][k] += dp[i - 1][j - members][max(0, k - earn)]
```

Após isso cada valor é modulado por `10^9 + 7` para evitar estouros de números grandes e após o modulo ser aplicado o código retorna a soma de todas as combinações possíveis de `dp[m][j][minProfit]` para todos os `j` entre `0` e `n`, o que representa todas as maneiras de obter pelo menos `minProfit` usando até `n` pessoas:

```python
mod = 10**9 + 7 
dp[i][j][k] %= mod
result = sum(dp[m][j][minProfit] for j in range(n + 1)) % mod
```



**Submissão:**<br>
![](./assets/Sub21.png)

# 115. Distinct Subsequences

Problema: [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/description/)

**Descrição:** <br>

Given two strings s and t, return the number of distinct subsequences of s which equals t.<br>
The test cases are generated so that the answer fits on a 32-bit signed integer.<br>

**Example 1:**<br>
**Input:** s = "rabbbit", t = "rabbit" <br>
**Output:** 3 <br>
**Explanation:**  As shown below, there are 3 ways you can generate "rabbit" from s. <br>
- rabbbit <br>
- rabbbit <br>
- rabbbit <br>

**Example 2:** <br>
**Input:** s = "babgbag", t = "bag" <br>
**Output:** 5 <br>
**Explanation:** As shown below, there are 5 ways you can generate "bag" from s. <br>
- babgbag <br>
- babgbag <br>
- babgbag <br>
- babgbag <br>
- babgbag <br>
 

**Constraints:**<br>

- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.



## Estrutura do Algoritmo

Esse problema pode ser resolvido usando o algoritmo de `alinhamento de sequências(Sequence Alignment)`, onde a ideia é comparar duas strings, mas nesse caso com o objetivo de encontrar subsequências e não substrings diretas.

Primeiro uma tabela `dp[i][j]` vai ser criada que representa o número de subsequências da string `s[0:i]` que são iguais à string `t[0:j]`.<br>
Após isso a tabela é preenchida para cada caso recursivamente para cada caso que `s[i-1] == t[j-1]` com as seguintes escolhas:<br>
- Contar as subsequências em que `s[i-1]` é parte da correspondência `(dp[i-1][j-1])`.<br>
- Contar as subsequências em que `s[i-1]` é ignorado `(dp[i-1][j])`.
- Se `s[i-1] != t[j-1]`, a única opção é ignorar `s[i-1]`, e a solução será simplesmente `dp[i-1][j]`.<br>

Os casos iniciais para esse problema são:

- `dp[0][0] = 1`: Há exatamente uma forma de corresponder uma string vazia com outra string vazia.
- Se `t` for uma string vazia, então `dp[i][0] = 1`, pois sempre há uma subsequência vazia em qualquer string `s`.
- Se `s` for uma string vazia e t não for, então `dp[0][j] = 0`, pois uma string vazia não pode conter nenhuma subsequência que corresponda a `t`.

Após a tabela ser preenchida o resultado final é `dp[len(s)][len(t)]`.

### Explicação do Código:

Primeiro como explicado acima a tabela `dp[i][j]` é criada representando o número de subsequências de `s[0:i]` que correspondem à string `t[0:j]`, o número de esquemas disponíveis é armazenado em uma variavel e o caso base é aplicado que é se `t` é vazio, há apenas uma subsequência vazia: <br>

```python
def numDistinct(self, s: str, t: str) -> int:
    m, n = len(s), len(t)        
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
```
Após isso a matriz é preenchida para cada caso recursivamente para os casos em que os caracteres correspondem, aplicamos os dois casos:<br>
- Se `s[i-1] == t[j-1]`: Podemos incluir o caractere `s[i-1]` na correspondência, ou ignorá-lo. Assim, a solução para `dp[i][j]` é a soma de `dp[i-1][j-1]` (incluindo ele) e `dp[i-1][j]` (ignorando ele).<br>
- Se `s[i-1] != t[j-1]`: Só podemos ignorar `s[i-1]`, então copiamos o valor de `dp[i-1][j]`.<br> 


```python
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j]
```

Após isso  o código retorna `dp[m][n]`, que representa o número de subsequências de `s` que correspondem à string `t`:

```python
return dp[m][n]
```



**Submissão:**<br>
![](./assets/Sub22.png)

# 72. Edit Distance

Problema: [Edit Distance](https://leetcode.com/problems/edit-distance/description/)

**Descrição:**

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.<br> 

You have the following three operations permitted on a word:<br> 

- Insert a character
- Delete a character
- Replace a character
 

**Example 1:**<br> 

**Input:** word1 = "horse", word2 = "ros"<br> 
**Output:** 3<br> 
**Explanation:** 
- horse -> rorse (replace 'h' with 'r')<br> 
- rorse -> rose (remove 'r')<br> 
- rose -> ros (remove 'e')<br> 

**Example 2:**<br> 

**Input:** word1 = "intention", word2 = "execution"<br> 
**Output:** 5<br> 
**Explanation:** 
- intention -> inention (remove 't')<br> 
- inention -> enention (replace 'i' with 'e')<br> 
- enention -> exention (replace 'n' with 'x')<br> 
- exention -> exection (replace 'n' with 'c')<br> 
- exection -> execution (insert 'u')<br> 
 

**Constraints:**

- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

## Estrutura do Algoritmo

Esse problema pode ser resolvido usando o algoritmo de `alinhamento de sequências(Sequence Alignment)`, sendo nesse caso a resposta a `Levenshtein Distance (Distância de Levenshtein)` que é o mínimo de operações necessárias para transformar uma string em outra.
Definir a tabela de DP:

Primeiro uma tabela `dp[i][j]` vai ser criada que representa o número mínimo de operações necessárias para transformar `word1[0:i]` em `word2[0:j]`.<br>
Após isso a tabela é preenchida para cada caso recursivamente para cada caractere com as seguintes escolhas:<br>
- Se  `word1[i-1] == word2[j-1] `, então  `dp[i][j] = dp[i-1][j-1] ` (não faz nada).<br>

Caso contrário, três operações são possíveis:<br>

- Inserção:  `dp[i][j-1] + 1 ` (inserir  `word2[j-1] ` em  `word1 `).
- Deleção:  `dp[i-1][j] + 1 ` (deletar  `word1[i-1] `).
- Substituição:  `dp[i-1][j-1] + 1` (substituir  `word1[i-1]` por  `word2[j-1]`).

Os casos base para esse problema é que se uma das strings for vazia:

- `dp[i][0] = i`: Para transformar qualquer prefixo de word1 em uma string vazia, será necessário de `i` operações de deleção.
- `dp[0][j] = j`: Para transformar uma string vazia em qualquer prefixo de word2, será necessário de `j` operações de inserção.

Após tudo isso feito o código retorna `dp[len(word1)][len(word2)]` que é o número mínimo de operações necessárias para transformar `word1` em `word2`.

### Explicação do Código:

Primeiro como o tamanho das palavras são armazenados em varíaveis diferentes, depois a tabela é iniciada: <br>

```python
m, n = len(word1), len(word2)
dp = [[0] * (n + 1) for _ in range(m + 1)]
```
Após isso o caso base discutido acima é aplicado fazendo que todos os caracteres de word1 sejam deletados para torná-la vazia e insere todos os caracteres de word2 em uma string vazia  .<br> 

```python
for i in range(m + 1):
    dp[i][0] = i  
for j in range(n + 1):
    dp[0][j] = j 
```

Após isso a tabela é preenchida com cada caractere sendo verificado recursivamente como foi discutido acima, se o caractere for igual não faz nada e caso contrário considera ás três operações necessárias e depois de rodar por toda a tabela ele retorna `dp[m][n]` com a resposta:

```python
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(
                dp[i - 1][j] + 1, #deletar
                dp[i][j - 1] + 1, #inserir
                dp[i - 1][j - 1] + 1 #substituir
                )
        return dp[m][n]
```


**Submissão:**


![](./assets/Sub11.png)
