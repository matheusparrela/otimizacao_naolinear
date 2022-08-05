#OTIMIZAÇÃO NÃO LINEAR - MÉTODO DO GRADIENTE
#RESTRIÇÃO DA BARREIRA
import sympy as sy
import solucao_grafica as sg
import search_result as sr

sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

def gradiente(function, restriction, mi, x, y, precision_decimals=4):
    alfa = sy.symbols("alfa")
    symbols = sy.symbols("x1 x2")
    #Nova Função
    a = function+'+'+str(mi)+'/('+restriction+')'

    try:
        expression = sy.parsing.sympy_parser.parse_expr(a)
    except:
        print("Erro na função")
        return 1
    precision = 10**(-precision_decimals)
    k = 0
    iterations = [0]
    loop = True
    converged = True
    points = [[x,y]]
    grad1 = sy.diff(expression, symbols[0]) #Gradiente da Função
    grad2 = sy.diff(expression, symbols[1])
    while loop == True:

        a = grad1.subs(symbols[0], x) #Valor de x1 no gradiente
        a2 = a.subs(symbols[1], y)
        b = grad2.subs(symbols[0], x) #Valor de x2 no gradiente
        b2 = b.subs(symbols[1], y)
        y1 = (x - alfa*a2) #Expressão do alfa
        y2 = (y - alfa*b2)
        funcao1 = expression.subs(symbols[0], y1) #Substituição de de y1 e y2 na função
        funcao2 = funcao1.subs(symbols[1], y2)
        df_dalfa = sy.diff(funcao2, alfa) #Derivada da função em relação a alfa
        raiz = (sy.solve(df_dalfa)) #Raiz da derivada da função
        try:
            raiz = raiz[0]
        except: #Critério de Parada 1
            grad1 = grad1.subs(symbols[0], x)
            grad1 = grad1.subs(symbols[1], y)
            grad2 = grad2.subs(symbols[1], y)
            grad2 = grad2.subs(symbols[0], x)
            if grad1 == 0 and grad2 == 0:
                k=k+1
                print("Gradiente: Zero")
                points.append([x,y])
                image_z = sg.function(expression, symbols, points)
                iterations.append(k)
                break
        #Substitui o valor da raiz de alfa na expressão de alfa
        x = round(y1.subs(alfa, raiz), precision_decimals) #Atualiza os valores de x e y
        y = round(y2.subs(alfa, raiz), precision_decimals)
        points.append([x,y])
        k = k + 1
        iterations.append(k)
        image_z = sg.function(expression, symbols, points)
        if k >= 5: #Critério de Parada 2
            fmax = max(image_z[k-5:])
            fmin = min(image_z[k-5:])
            if abs(fmax - fmin) < precision:
                loop = False
        if k>= 100: #Critério de Parada 3
            print("Não Convergiu")
            converged = False
            loop = False
        print("Iteração: ", k)
        print('X:',x,'\nY',y)
    sg.graphic_solution(expression, symbols, points, image_z, iterations)
    return sr.SearchResult(function, points, converged, precision_decimals)

funcao = '(x1 + 2*x2 -7)**2 + (2* x1 + x2 - 5)**2'
retricao = 'x2 - (x1 -2)**3 - x1**2 -10'
mi = 1

result = gradiente(funcao,retricao, mi,1, 1, 4)
print(result)
