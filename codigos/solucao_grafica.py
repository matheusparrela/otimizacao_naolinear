import sympy as sy
import matplotlib.pyplot as mp
import numpy as np
import pandas

def funtion(x1, x2):
    #return  ((x1 - 3)**2 + (x2 - 2)**2)
    return (((x1 - 3)**2)/4 + ((x2 - 2)**2)/9) + 13

def plot_path(x , y):
      
        df = pandas.DataFrame.from_dict({'x' : x, 'y' : y})
        for i,row in df.iterrows():
            if i==0:
                pass
            else:
                mp.annotate('', xy = (row['x'], row['y']), xytext = (df.iloc[i-1]['x'], df.iloc[i-1]['y']),
            arrowprops = dict(facecolor = 'yellow', width = 0.5, headwidth = 2))
        return

def plot_convergencia(iteracoes, pontos):

    mp.title('Convergência por iteração')
    mp.ylabel('f(x,y)')
    mp.xlabel('Iterações')
    mp.ylim(12,14)
    mp.xlim(0, 10)
    mp.plot(iteracoes, pontos)
    mp.show()

def plot_curvasniveis(a, b):

    #Curvas de Nivel e Convergência
    
    mp.style.use('seaborn-white')

    x = np.linspace(0, 5, 600)
    y = np.linspace(0, 5, 600)

    X, Y = np.meshgrid(x, y)
    Z = funtion(X, Y)

    contours = mp.contour(X, Y, Z, 10, colors='black')
    mp.clabel(contours, inline=True, fontsize=8)

    mp.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
    mp.colorbar();
    mp.title('Curva de níveis e Convergência')
    mp.xlabel('x')
    mp.ylabel('y')

    if len(a) > 2:
        plot_path(a,b)
    else:
        mp.plot(a, b, 'go')

    mp.show()
