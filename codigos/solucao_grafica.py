import matplotlib.pyplot as mp
import numpy as np
import pandas


def funcao(x1, x2):
   
    return  ((x1 - 3)**2 + (x2 - 2)**2)
    #return (((x1 - 3)**2)/4 + ((x2 - 2)**2)/9) + 13



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
    mp.plot(iteracoes, pontos, 'ro')
    mp.show()



def plot_curvasniveis(a, b):

    #Curvas de Nivel e Convergência
    
    mp.style.use('seaborn-white')

    x = np.linspace(0, 5, 600)
    y = np.linspace(0, 5, 600)

    X, Y = np.meshgrid(x, y)
    Z = funcao(X, Y)

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



def d3():

    fig = mp.figure()
    ax = mp.axes(projection="3d")
        
    ax = mp.axes(projection='3d')
        
    
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)
        
    X, Y = np.meshgrid(x, y)
    Z = funcao(X, Y)
        
    ax.plot_wireframe(X, Y, Z, color='green')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
        
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        cmap='viridis', edgecolor='none')
    ax.set_title('Gráfico de superfícies');
        
    mp.show()
