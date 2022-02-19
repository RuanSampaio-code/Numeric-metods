import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return 31 - ((9.8*x)/13)*(1. - np.exp(-6.0*(13.0/x)))

def secante(x0, x1, Erro, itMax):
  it = 0
  Er = 1
  xa1 = x0
  x = x1
  while(Er >= Erro and it < itMax):
    xa2 = xa1
    xa1 = x
    x = xa1 - f(xa1)*(xa2 - xa1)/(f(xa2) - f(xa1))
    Er = np.abs((x - xa1)/x)
    it = it + 1
  return (x, Er, it)

x0 = 54
x1 = 55
Erro = 10**-4
itMax = 6

res = secante(x0, x1, Erro, itMax)

print('O valor da raíz é: ', res[0])
print('O erro relativo foi: ', res[1])
print('O número de iterações realizadas foi: ', res[2])