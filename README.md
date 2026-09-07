# IC_Criptografia_RSA

Repositório dedicado ao registro do desenvolvimento de Iniciação Científica na área de Criptografia. O livro utilizado para estudos é **Números Inteiros e Criptografia RSA** de S. C. Coutinho (IMPA, 2ª edição, 2014). O orientador é o professor Eduardo Favaro do IME/UFU.

Os arquivos estão organizados por capítulo do livro. Cada arquivo implementa um exercício ou algoritmo apresentado no texto, conforme descrito abaixo.

---

## Capítulo 1 — Algoritmos Fundamentais

### `mdc.py` — Algoritmo de Euclides

Implementação do algoritmo euclidiano para calcular o Máximo Divisor Comum (MDC) de dois inteiros. O algoritmo realiza divisões sucessivas até que o resto seja zero, retornando o último divisor não nulo como MDC.

### Exercício 8 — `ex8.py` — Algoritmo Euclidiano Estendido

> Usando o método descrito no exercício anterior, escreva um programa para determinar uma solução inteira para a equação ax + by = c, tendo como entrada os coeficientes a, b e c. A saída do programa deve ser, ou uma solução inteira da equação, ou uma mensagem indicando que tais soluções não existem. Portanto o programa consistirá, essencialmente, de uma implementação do algoritmo euclidiano estendido.

O programa implementa o algoritmo euclidiano estendido, que além de calcular o MDC rastreia os coeficientes x e y tais que ax + by = mdc(a, b). A solução da equação existe se, e somente se, mdc(a, b) divide c. Quando existe, o programa exibe uma solução inteira particular; caso contrário, informa que não há soluções.

### Exercício 9 — `ex9.py` — Probabilidade de Coprimalidade

> Escreva um programa que, tendo como entrada dois inteiros a e b, determina o máximo divisor comum de a e b. Adapte o seu programa para gerar aleatoriamente pares de inteiros a e b e calcular o mdc(a, b). O programa deve ter como entrada o número total de pares que você deseja testar, e como saída o quociente [total de pares cujo mdc é 1] / [total de pares testados]. Este quociente dá uma medida da probabilidade de que um par de inteiros escolhido aleatoriamente seja co-primo. [...] o quociente acima deve ficar próximo de 6/π². Faça uma tabela com esses valores, tendo como entrada 10, 100, 1000, 10000 e 100000 pelo menos.

O programa gera aleatoriamente pares de inteiros e calcula a proporção dos que são coprimos (mdc = 1). A experiência é repetida dez vezes para cada tamanho de amostra, e os resultados experimentais convergem para 6/π² ≈ 60,79%, confirmando o resultado teórico da Teoria dos Números.

---

## Capítulo 2 — Fatoração Única

### Exercício 11 — `ex11.py` — Números Altamente Compostos (HCN)

> Seja n um inteiro positivo e d(n) o número de divisores positivos de n. Dizemos que n é altamente composto se d(m) < d(n) para todo m < n. Escreva um programa que, tendo como entrada um número inteiro r, determina todos os números altamente compostos menores que r. Use o programa para fazer uma lista dos números altamente compostos menores que 5000. Observe as fatorações dos números altamente compostos da sua lista: que propriedades destes números você deduz da observação desta lista? Estes números foram estudados pelo matemático indiano autodidata Srinivasa Ramanujan.

O programa percorre todos os inteiros i < r e verifica se nenhum j < i possui mais divisores do que i. Quando essa condição é satisfeita, i é altamente composto e é incluído na lista de saída.

### Exercício 12 — `ex12.py` — Fatoração de Fermat

> Escreva um programa que implemente o algoritmo de Fermat para achar dois fatores de um número inteiro positivo que seja menor que 2³². Este exercício é o primeiro de uma seqüência que termina com o exercício 8 do capítulo 11.

O algoritmo de Fermat explora a decomposição n = (x + y)(x − y) a partir de x = ⌈√n⌉, verificando se x² − n é um quadrado perfeito. O programa retorna os dois fatores encontrados ou indica que nenhuma fatoração foi possível no intervalo testado.

---

## Capítulo 3 — Números Primos

### `crivo.py` — Crivo de Eratóstenes

Implementação do Crivo de Eratóstenes seguindo o algoritmo em 4 etapas descrito na Seção 6 do capítulo. Um vetor booleano de tamanho n é inicializado e, a cada primo descoberto, todos os seus múltiplos são marcados como compostos. O algoritmo retorna todos os números primos até n. Esta implementação serve de base para os exercícios do capítulo que requerem a lista de primos.

### `crivo_melhorado.py` — Crivo de Eratóstenes Otimizado

Versão otimizada do Crivo de Eratóstenes usando `bytearray` e fatiamento Python para marcar múltiplos diretamente. Essa abordagem reduz o consumo de memória e acelera a execução, tornando viável encontrar primos em intervalos maiores.

---

## Capítulo 4 — Aritmética Modular

### Exercício 11 — `ex_binaria.py` e `potenciacao_mod.py` — Exponenciação Binária Modular

> Escreva um programa que implemente o algoritmo para calcular potências módulo n que é descrito na seção 2 do apêndice. O algoritmo deverá ter como entrada a, k e n, onde a é um inteiro qualquer e k e n são inteiros positivos. A saída deverá ser a forma reduzida de aᵏ módulo n. Este algoritmo é uma parte fundamental de quase todos os algoritmos que estudaremos a partir do capítulo 6.

Dois arquivos implementam o mesmo algoritmo de exponenciação binária (método quadrado-e-multiplica):

- **`ex_binaria.py`**: versão modularizada com funções auxiliares separadas para os casos em que o expoente é par ou ímpar, tornando o fluxo do algoritmo mais explícito.
- **`potenciacao_mod.py`**: versão compacta com função `simplifica` para redução modular a cada passo, mais próxima de uma implementação de produção.

---

## Capítulo 5 — Indução e Fermat

### `ex14.py` — (em desenvolvimento)

Arquivo reservado para exercício futuro. O arquivo se encontra vazio.

---

## Capítulo 6 — Pseudoprimos

### Exercício 8 — `ex8.py` — Pseudoprimos para as Bases 2 e 3

> Escreva um programa que, tendo como entrada um inteiro positivo r, determina todos os números entre 1 e r que são pseudoprimos para as bases 2 e 3. Lembre-se que um tal pseudoprimo n é um número ímpar e composto que satisfaz as equações 2ⁿ⁻¹ ≡ 1 (mod n) e 3ⁿ⁻¹ ≡ 1 (mod n). Aplique o programa com r = 10⁵. Quantos e quais foram os pseudoprimos obtidos? Quantos destes são números de Carmichael?

O programa usa o Crivo de Eratóstenes para identificar compostos ímpares no intervalo e então testa, via exponenciação modular, se cada composto satisfaz simultaneamente as congruências de Fermat para as bases 2 e 3.

### `miller.py` — Teste de Miller

Implementação do Teste de Miller: dado n e base b, o teste verifica se b^(n−1) ≡ 1 (mod n) e, em caso afirmativo, examina condições adicionais decompondo n−1 = 2ˢ·d (com d ímpar) para detectar pseudoprimos fortes. O programa determina se n é composto, primo ou inconclusivo para a base b.

### Exercício 9 — `ex9.py` — Números de Carmichael com d Fatores Primos

> O objetivo deste exercício é a elaboração de um programa para determinar todos os números de Carmichael que são produtos de d primos, todos menores que 10³. [...] Aplique o seu programa para d = 1, ..., 8. Quais os números de Carmichael obtidos em cada caso?

O programa usa `itertools.combinations` para gerar combinações de d primos distintos (todos < 1000) e verifica a condição de Korselt: o produto n = p₁·p₂·…·pₐ é de Carmichael se, para cada fator primo pᵢ, (pᵢ − 1) divide (n − 1).

### Exercício 10 — `ex10.py` — Menor Pseudoprimo Forte para uma Base

> Escreva um programa para determinar o menor pseudoprimo forte para uma dada base. Vai ser necessário implementar o teste de Miller, de modo que a entrada seja um inteiro positivo b > 1. O programa deve aplicar o teste de Miller na base b aos ímpares compostos, até achar o primeiro número para o qual o teste é inconclusivo. Aplique o teste para as bases 2, 3, 5 e 7. Quais os resultados obtidos?

O programa percorre os compostos ímpares em ordem crescente e aplica o Teste de Miller (implementado em `miller.py`) para encontrar o menor pseudoprimo forte para a base b fornecida pelo usuário.

---

## Capítulo 7 — Sistemas de Congruências

### `alg_chines_resto.py` — Algoritmo Chinês do Resto

Implementação do Teorema Chinês do Resto (TCR) para sistemas de congruências lineares simultâneas do tipo x ≡ aᵢ (mod nᵢ). Quando os módulos são dois a dois coprimos, o algoritmo constrói a solução única módulo N = n₁·n₂·…·nₖ usando inversos modulares calculados via MDC.

### `ex10.py` — (em desenvolvimento)

Arquivo reservado para exercício futuro. O arquivo se encontra vazio.

---

## Capítulo 8 — Grupos

### `phi.py` — Função Totiente de Euler

Implementação da função φ(n) de Euler, que conta os inteiros positivos menores que n e coprimos com n. O algoritmo fatora n manualmente e aplica a fórmula φ(n) = n · ∏ₚ(1 − 1/p) para cada fator primo p de n.

### `phi2.py` — Função Totiente de Euler (versão aprimorada)

Versão melhorada que usa `Counter` para rastrear a multiplicidade de cada fator primo, calculando φ(n) pela fórmula φ(pᵉ) = pᵉ⁻¹(p − 1) aplicada a cada componente da fatoração.

---

## Capítulo 9 — Mersenne e Fermat

### Exercício 9 — `ex9.py` e `ex9_2.py` — Menor Fator Primo de M(p)

> Programe o método de Fermat para achar fatores de um número de Mersenne. O programa deve ter como entrada um primo p > 0 e como saída o menor fator primo de M(p) = 2ᵖ − 1 ou uma mensagem indicando que M(p) é primo. O programa vai consistir, basicamente, de uma implementação do algoritmo apresentado na seção 2 do apêndice para calcular 2ⁿ módulo q, onde q é da forma q = r · 2p + 1 com 0 ≤ r ≤ [(2^(p/2) − 1)/(2p)].

Os candidatos a fator de M(p) são da forma q = 2kp + 1 (resultado clássico: todo fator primo de um número de Mersenne tem essa forma). O limite superior é derivado de q ≤ √M(p). Dois arquivos implementam o mesmo algoritmo com pequenas variações:

- **`ex9.py`**: usa o limite r = (2^(p//2) − 1) // (2p) e itera sobre r.
- **`ex9_2.py`**: versão alternativa que compara q ≤ 2^(p//2) diretamente.

### Exercício 10 — `ex10.py` — Teste de Pepín para Números de Fermat

> Programe o algoritmo apresentado na seção 3. O algoritmo deve ter como entrada o primo p e deve procurar o valor de m (se existir) para o qual p divide F(m). Observe que, escrevendo p na forma p = k · 2ⁿ + 1, temos que m < n, o que nos dá um limite além do qual não adianta continuar a busca.

O arquivo implementa o Teste de Pepín: F(k) = 2^(2^k) + 1 é primo se, e somente se, 5^((F(k)−1)/2) ≡ −1 (mod F(k)). O teste é eficiente porque envolve apenas calcular potências de 5 módulo F(k) por exponenciação binária.

---

## Capítulo 10 — Raízes Primitivas

### `teste_lucas.py` — Teste de Lucas

Implementação do Teste de Lucas para primalidade. Dado n e base b, o teste verifica se b^(n−1) ≡ 1 (mod n) e se b^((n−1)/q) ≢ 1 (mod n) para todo fator primo q de n−1. Quando ambas as condições são satisfeitas para alguma base b, n é definitivamente primo.

### `ordem_elemento.py` — Ordem de Elemento em U(p)

Implementação do algoritmo das potências para calcular a ordem de um elemento a no grupo multiplicativo U(p) = (ℤ/pℤ)×. O algoritmo fatora p−1 e, para cada fator primo pᵢ com multiplicidade eᵢ, determina o maior k tal que a^((p−1)/pᵢᵏ) ≡ 1 (mod p), compondo a ordem por multiplicação.

### `raiz_primitiva.py` — Raiz Primitiva de U(p) pelo Método de Gauss

Implementação do método de Gauss para encontrar uma raiz primitiva de U(p). O algoritmo combina dois elementos a e b de U(p) cujas ordens são "complementares" (cada um contribui com potências de primos distintos da fatoração de p−1), construindo iterativamente um elemento de ordem máxima p−1.

### Exercício 10 — `ex10.py` — Teste de Wilson

> Escreva um programa que implemente o teste de primalidade descrito no exercício 6. O programa vai consistir, essencialmente, de um algoritmo para calcular a forma reduzida de (n−1)! módulo n. [...] Aplique o programa ao maior primo, menor que 10ᵏ, quando k = 1, ..., 6.

O programa implementa o Teste de Wilson: n é primo se, e somente se, (n−1)! ≡ −1 ≡ n−1 (mod n). Para evitar o cálculo explícito do fatorial inteiro, as reduções módulo n são aplicadas a cada multiplicação.

### `ex11.py` e `mmc.py` — Mínimo Múltiplo Comum

Implementação do Mínimo Múltiplo Comum (MMC) usando a relação mmc(a, b) = (a · b) / mdc(a, b):

- **`mmc.py`**: versão básica que calcula o MMC de dois inteiros.
- **`ex11.py`**: versão que encapsula o cálculo do MMC via MDC, possivelmente usada em conjunto com exercícios sobre identidades envolvendo MMC e MDC.

---

## Capítulo 11 — Criptografia RSA

### `menor_grupo_p.py` — Menor Primo p tal que a é a Menor Raiz Primitiva de U(p) (versão inicial)

Dado um inteiro a que não seja quadrado perfeito nem ≤ 1, o programa busca o menor primo p > a tal que a é a menor raiz primitiva de U(p). O algoritmo: (1) verifica se a é raiz primitiva de U(p) pela condição de Korselt para p−1; (2) somente se a passa, verifica se algum g < a também é raiz primitiva; (3) se nenhum g menor for raiz, retorna p. A fatoração de p−1 usa `Counter` para multiplicidades.

### `menor_p2.py` — Menor p tal que a é a Menor Raiz Primitiva (versão otimizada)

Versão aprimorada do mesmo algoritmo. As melhorias incluem o uso de `fatores_primos_unicos` (lista sem repetição de primos distintos, suficiente para o teste de raiz primitiva) e a interrupção imediata da verificação assim que um g < a com raiz primitiva é encontrado, eliminando iterações desnecessárias.

### `valores_p.py` — Tabela de Desempenho

Extensão do algoritmo anterior que executa `menor_p` para dez valores de entrada no intervalo [10, 60]: [10, 15, 20, 26, 30, 35, 42, 47, 50, 60]. Os quadrados perfeitos (16, 25, 36, 49) foram omitidos propositalmente, pois não admitem raiz primitiva em nenhum grupo U(p) segundo a definição do problema. O programa exibe uma tabela com o menor p encontrado e o tempo de execução para cada entrada.
