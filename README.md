# :key: Criptografia Assimétrica com RSA
Trabalho da disciplina de Criptografia, focado na implementação de um algoritmo de criptografia RSA. Esse é um algoritmo de criptografia de chave assimétrica amplamente utilizado para comunicação segura na internet. Ele é baseado na dificuldade de fatorar o produto de dois números primos grandes, tornando a quebra do sistema impraticável quando as chaves são suficientemente longas.
## Funcionalidades Implementadas

### 1. Exponenciação Modular

A função ***`exponenciacao(a, x, p)`*** realiza a exponenciação modular, uma operação fundamental no RSA, onde *a<sup>x</sup> mod p* é calculado eficientemente.

### 2. Algoritmo Euclidiano Estendido

A função ***`euclidiano_estendido(a, b)`*** implementa o algoritmo euclidiano estendido para encontrar o máximo divisor comum (MDC) e os coeficientes de Bézout entre dois números.

### 3. Geração de Expoentes

A função ***`gerar_expoentes(phi)`*** gera expoentes adequados para a implementação do RSA, garantindo que o expoente público seja relativamente primo em relação ao totiente de Euler.
### 4. Utilização
 1. Instale as dependências
`pip install pycryptodome` 
2. Execute o código:
`python3 main.py`
