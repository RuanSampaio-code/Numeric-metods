#importamos bibliotecas numpy e matplot lib
import numpy as np
import matplotlib.pyplot as plt
def interpLagrange(xp,x,y,grau): 
  # Valor inicial de g(xp).
  yp = 0
  # Interpolação de Lagrange
  for k in range(0,n+1):  
    p = 1
    for j in range(0,n+1):
      if k != j:
        p = p*(xp - x[j])/(x[k] - x[j])
    
    yp = yp + p * y[k]  
  return yp  
# dados da interolaçao : eixo x e y.
x=[78,79]
y = [2.9785,3.06173]
# Ponto da interpolação
xp = float(input('Entre com xp: '))
# Grau da interpolação. 
n = 1
# Interpolação de Lagrange.
yp = interpLagrange(xp,x,y,n)
# Valor interpolado encontrado
print('g(%.3f) = %.3f' % (xp, yp))
t  = np.arange(-1.0, 2.0, 0.1)
yt = []
for i in t:
  yt.append(interpLagrange(i,x,y,n))
plt.title('Grafico da Interpolação')
plt.plot(t,yt,'b-')
plt.plot(x,y,'ro')
plt.plot(xp,yp,'p')

plt.show()