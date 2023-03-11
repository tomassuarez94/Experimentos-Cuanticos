import Matrices as lc
import matplotlib.pyplot as plot

def canicas(m,x,c):
    aux = []
    for i in range(c):
        x = lc.accion(m,x)
    for i in range(len(x)):
        aux.append(x[i])
    return aux
def dos_rendijas(m,x,c):
    x = canicas(m,x,c)
    j = 0
    z = []
    prob = []
    for i in range(len(x)):
        j = x[i]**2
        prob.append(j)
    for i in range(len(x)):
        z.append(x[i])
    return prob
def multiples(matriz, estado):
    matriz_transpuesta = lc.tra_matr(matriz)
    for i in range(len(matriz_transpuesta)):
        if sum(matriz_transpuesta[i]) != 1:
            estocastica = False
            break
        else:
            estocastica = True
    if estocastica == True:
        res = list(map(float, canicas(matriz, estado, 1)))
        return res
    else:
        return False
def diagrama(vector,prob):
    fig = plot.figure()
    ax = fig.add_subplot(111)
    datos = prob
    xx = range(len(datos))
    ax.bar(xx,datos)
    ax.set_xticks(xx)
    ax.set_xticklabels(vector)
    ax.set_xlabel("Estado")
    ax.set_ylabel("Probabilidad")
    plot.show()
