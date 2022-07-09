#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DE NEWTON MODIFICADO   

import sympy as sy
import solucao_grafica as sg

def main(): 
  
    sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

    #Condições Iniciais
    x = 2
    y = 2 

    x1 = sy.Symbol('x1')
    x2 = sy.Symbol('x2')
    alfa = sy.Symbol('alfa')

    symbols = sy.symbols("x1 x2 alfa")
    funcao = "2*x1**2 - 1.05*x1**4 + ((x1**6)/6) +  x1*x2 + x2**2"
    expression = sy.parsing.sympy_parser.parse_expr(funcao)
    
    
    resultado1 = 0
    resultado2 = 0
    k = 0
    pontos = []
    iteracoes = []
    lista_x = []
    lista_y = []


    grad1 = sy.diff(expression, symbols[0])         #Gradiente da Função
    grad2 = sy.diff(expression, symbols[1])

    h11 = sy.diff(grad1, symbols[0])            #Calcula os elementos da hessiana
    h12 = sy.diff(grad1, symbols[1])
    h21 = sy.diff(grad2, symbols[0])
    h22 = sy.diff(grad2, symbols[1])

    #Passa as condições iniciais, elementos da hessiana e o gradiente no pontos iniciais para matrizes

    hessiana = sy.Matrix([[h11, h12],[h21, h22]]) 

    gradiente = sy.Matrix([[grad1], [grad2]])

    inv_hessiana = -hessiana.inv()       #Inverte a matriz hessiana

    prod = inv_hessiana*gradiente      #Calcula o produto das matrizes

    #while (abs(controlex) > 0.00001) or (abs(controley) > 0.00001):
    while k < 10:
        
        k = k + 1

        prod1 = prod.subs(symbols[0], x)
        prod2 = prod1.subs(symbols[1], y)

        y1 = (x + symbols[2]*prod2[0,0])
        y2 = (y + symbols[2]*prod2[1,0])

        funcao1 = expression.subs(symbols[0], y1)       #Substituição de de y1 e y2 na função 
        funcao2 = funcao1.subs(symbols[1], y2)
       
        d1 = sy.diff(funcao2, symbols[2])         #Derivada da função em relação a alfa
  
        raiz = (sy.solve(d1))
       
        try:               
            raiz = raiz[0]

        except:
            exit()

        resultado1 = y1.subs(symbols[2], raiz)    #Substitui o valor da raiz de alfa na expressão de alfa
        resultado2 = y2.subs(symbols[2], raiz)
        
        print('\nITERAÇÃO',k,":")
        print('Ponto X1:',resultado1,'\nPonto X2:',resultado2)
     
        controlex = resultado1 - x          #Calcula a variação dos valores dos pontos encontrados
        controley = resultado2 - y
                         
        x = round(resultado1,4)                      #Atualiza os valores de x e y
        y = round(resultado2,4)  


        iteracoes.append(k)
        pontos.append(sg.funcao(expression, symbols, x, y))
        lista_x.append(x)
        lista_y.append(y)
    
    pontos = sg.funcao(expression, symbols, lista_x, lista_y)
        
      
    sg.plot_convergencia(iteracoes, pontos)
    sg.plot_curvasniveis(expression, symbols, lista_x, lista_y)
    sg.grafico_3d(expression, symbols)
    sg.deslocamento_3d(expression, symbols, lista_x, lista_y)

    

main()