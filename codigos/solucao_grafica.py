from matplotlib import projections
import matplotlib.pyplot as mp
import numpy as np
import pandas
import operator

import youtube_dl


def funcao(expression, symbols, x, y):

    l = operator.length_hint(x)
    f = []

    for i in range (0, l):
        
        e = expression.subs(symbols[0], x[i])
        f.append(e.subs(symbols[1], y[i]))
    
    return f


def funcao1(expression, symbols, x, y):

    l = operator.length_hint(x)
    f = np.zeros((l,l) ,dtype=np.float64)

    for i in range (0, l):

        for j in range(0,l):
            e = expression.subs(symbols[0], x[i][j])
            f[i][j] = (e.subs(symbols[1], y[i][j]))
        
    return f
 

#Setas das Curvas de nível
def plot_path(x , y):
      
        df = pandas.DataFrame.from_dict({'x' : x, 'y' : y})
        for i,row in df.iterrows():
            if i==0:
                pass
            else:
                mp.annotate('', xy = (row['x'], row['y']), xytext = (df.iloc[i-1]['x'], df.iloc[i-1]['y']),
            arrowprops = dict(facecolor = 'yellow', width = 0.5, headwidth = 1.5))
        return



#Gráfico f(x,y) pelas iterações
def plot_convergencia(iteracoes, pontos):

    mp.title('Convergência por iteração')
    mp.ylabel('f(x,y)')
    mp.xlabel('Iterações')

    lim_a = int(pontos[0]-1)
    lim_b = int(pontos[len(pontos)-1]+1)
    lim_c = 0
    lim_d = int(len(iteracoes)+1)

    mp.ylim(lim_a,lim_b)
    mp.xlim(lim_c,lim_d)
    mp.plot(iteracoes, pontos, 'k-h')
    mp.plot(iteracoes, pontos,'rh')
    mp.show()


#Curvas de Nivel e Convergência
def plot_curvasniveis(expression ,symbols, a, b):
    
    mp.style.use('seaborn-white')

    x = np.linspace(0, 5, 60)
    y = np.linspace(0, 5, 60)

    X, Y = np.meshgrid(x, y)
  
    Z = funcao1(expression, symbols, X, Y)

    contours = mp.contour(X, Y, Z, 10, colors='black')
    mp.clabel(contours, inline=True, fontsize=8)

    mp.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
    mp.colorbar();
    mp.title('Curva de níveis e Convergência')
    mp.xlabel('x')
    mp.ylabel('y')

    if len(a) > 2:
        plot_path(a,b)
        mp.plot(a, b, 'g.')
    else:
        mp.plot(a, b, 'g.')

    mp.show()


#Gráfico da Função
def grafico_3d(expression ,symbols):

    fig = mp.figure()
    ax = mp.axes(projection="3d")
        
    
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)
        
    X, Y = np.meshgrid(x, y)
    Z = funcao1(expression ,symbols, X, Y)
        
    ax.plot_wireframe(X, Y, Z, color='green')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
        
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        cmap='viridis', edgecolor='none')
    ax.set_title('Gráfico de superfícies');
        
    mp.show()


#Delocamento da convergência em #D
def deslocamento_3d(expression, symbols, a, b):
  
    fig = mp.figure()
    grafico = fig.gca(projection='3d')

    z = funcao(expression, symbols, a, b)

    grafico.plot(a, b, z,'k-s')
    grafico.plot(a, b, z,'rs')

    mp.show()