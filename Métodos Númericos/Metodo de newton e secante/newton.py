 import numpy as np

def f(x):
  return np.exp(-x) + x**2 - 2

def df(x):
  return (-1+2*x*np.exp(x))/np.exp(x)

def newton(x0, Erro, itMax):
  it = 0
  Er = 0.01
  x = x0
  while(Er >= Erro and it < itMax):
    xold = x
    x = x - f(x)/df(x)
    Er = np.abs((x - xold)/x)
    it = it + 1
  return (x, Er, it)

x0 = 1
Erro = 0.01
itMax = 6

res = newton(x0, Erro, itMax)

print('O valor da raíz é: ', res[0])

print('O número de iterações realizadas foi: ', res[2])