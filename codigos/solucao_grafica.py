import matplotlib.pyplot as mp
import numpy as np
import pandas
import operator

def function(expression, symbols, points):

    len = operator.length_hint(points)
    f = []

    for i in range (0, len):        
        e = expression.subs(symbols[0], points[i][0])
        f.append(e.subs(symbols[1], points[i][0]))
    
    return f


def function_aux(expression, symbols, x, y):

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


def list_separator(points):

    x = []
    y = []
    len = operator.length_hint(points)
 
    for i in range (0, len):
        x.append(points[i][0])
        y.append(points[i][1])
    return  x, y


def graphic_solution(expression, symbols, points, image_z, iterations, filename: str = ""):

    #Gráfico 3D
    fig = mp.figure(figsize = (12, 8), dpi=130)
    ax = mp.subplot2grid((7,7),(4, 0), rowspan=3, colspan=3, projection='3d')
    mp.style.use('Solarize_Light2')

    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)        
    X, Y = np.meshgrid(x, y)
    Z = function_aux(expression, symbols, X, Y)
        
    ax.plot_wireframe(X, Y, Z, color='green')
    
    ax.set_xlabel('x', fontsize = 10, color='gray')
    ax.set_ylabel('y', fontsize = 10, color='gray')
    ax.set_zlabel('z', fontsize = 10, color='gray')

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('FUNÇÃO', fontsize = 8)

    #Gráfico de convergência
    mp.subplot2grid((7,7),(0,4), rowspan=7, colspan=3)
    mp.style.use('seaborn-ticks')

    mp.title('CONVERGÊNCIA', fontsize = 10)
    mp.ylabel('f(x,y)', fontsize = 10)
    mp.xlabel('Iterações', fontsize = 10)

    lim_a = int(min(image_z)-1)
    lim_b = int(max(image_z)+1)
    lim_c = int(min(iterations))
    lim_d = int(max(iterations)+1)

    mp.ylim(lim_a,lim_b)
    mp.xlim(lim_c,lim_d)
    mp.plot(iterations, image_z, 'k-h')
    mp.plot(iterations, image_z,'rh')

    #Curvas de Nível
    mp.subplot2grid((7,7),(0,0), rowspan=3, colspan=3)    
    mp.style.use('_classic_test_patch')
    
    a, b = list_separator(points)

    lim_a = int(min(a)-1)
    lim_b = int(max(a)+1)
    lim_c = int(min(b)-1)
    lim_d = int(max(b)+1)

    x = np.linspace(lim_a, lim_b, 60)
    y = np.linspace(lim_c, lim_d, 60)

    X, Y = np.meshgrid(x, y)
  
    Z = function_aux(expression, symbols, X, Y)

    contours = mp.contour(X, Y, Z, 30, colors='black')
    mp.clabel(contours, inline=True, fontsize=8)

    mp.imshow(Z, extent=[lim_a, lim_b, lim_c, lim_d], origin='lower', cmap='RdGy')
    mp.colorbar()
    mp.title('CURVAS DE NÍVEL', fontsize = 8)
    mp.xlabel('x', fontsize = 10, color='gray')
    mp.ylabel('y', fontsize = 10, color='gray')

    if len(points) > 2:
        plot_path(a, b)
        mp.plot(a, b, 'g.')
 
    else:
        mp.plot(a, b, 'g.')

    if (filename is None) or (filename == ""):
        mp.show()
    else:
        mp.savefig(filename, facecolor='#f8f8f8', edgecolor='none')