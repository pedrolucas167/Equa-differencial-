import numpy as np

# função de EDO
def f(y, t):
    return t*np.exp(-t) - y

# valor inicial
y0 = 1

# intervalo de tempo
a = 0
b = 1

# número de passos
n = 10

# passo de tempo
h = (b-a)/n

# array de temop
t = np.arange(a, b+h, h)

# array de solução
y = np.zeros(n+1)
y[0] = y0

# loop para calcular a solução
for i in range(1, n+1):
    y[i] = y[i-1] + h*f(y[i-1], t[i-1])

# imprime a solução
print(y)


