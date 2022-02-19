from math import exp
n = int(input("Digite o número de passos: "))
x0 = int(input("1º valor do intervalo: "))
xn = int(input("2º valor do intervalo: "))
h = (xn-x0)/n
y0=2

#metodo de euler
for t in range(1,n+1):
    y1=y0+exp(y0)*x0*h
    y0=y1
    x0=0+t*h
print("Valor metodo de euler:", y1 )
#metodo runge kutta
x0 = int(input("1º valor do intervalo: "))
xn = int(input("2º valor do intervalo: "))
for t in range(1,n+1):
    k1 = x0+y0
    k2 = (x0+h)+(y0+h*k1)
    y1 = y0 + (h/2)*(k1+k2)
    x0 = 0 +t*h
print("Valor metodo de range kutta:", y1 )


#metodo runge kutta 4ªordem:
x0 = int(input("1º valor do intervalo: "))
xn = int(input("2º valor do intervalo: "))
for t in range(1,n+1):
    k1 = x0+y0
    k2 = (x0+h/2)+(y0+h*k1/2)
    k3 = (x0+h/2)+(y0+h*k2/2)
    k4 = (x0+h)+(y0+k3*h)
    y1 = y0 + (h/6)*(k1+2*k2+2*k3+k4)
    x0 = 0 +t*h
print("Valor metodo de range kutta:", y1 )

