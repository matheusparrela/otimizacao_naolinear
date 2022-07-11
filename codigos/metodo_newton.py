#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DE NEWTON
import sympy as sy
import solucao_grafica as sg

def main(): 
  
    sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

    #Condições Iniciais
    x = 3/4
    y = 1/4
    resultado1 = 0
    resultado2 = 0

    pontos = []
    iteracoes = []
    lista_x = []
    lista_y = []

    symbols = sy.symbols("x1 x2")
    entrada_funcao =  "((x1 - 3)**2 + (x2 - 2)**2)"
    
    expression = sy.parsing.sympy_parser.parse_expr(entrada_funcao)
    
    grad = []
    grad.append(sy.diff(expression, symbols[0]))        #Gradiente da Função
    grad.append(sy.diff(expression, symbols[1]))

    for k in range (0,5):

        a = grad[0].subs(symbols[0], x)               #Valor de X no gradiente
        a2 = a.subs(symbols[1], y)

        b = grad[1].subs(symbols[0], x)               #Valor de Y no gradiente
        b2 = b.subs(symbols[1], y)

        h11 = sy.diff(grad[0], symbols[0])       #Calcula os elementos da hessiana
        h12 = sy.diff(grad[0], symbols[1])
        h21 = sy.diff(grad[1], symbols[0])
        h22 = sy.diff(grad[1], symbols[1])
                                            #Passa as condições iniciais, elementos do hesiano e o gradiente no pontos iniciais para matrizes
        P = sy.Matrix([[x], [y]])            
        H = sy.Matrix([[h11, h12], [h21, h22]])
        G = sy.Matrix([[a2], [b2]])

        H_inv = H.inv()                 #Inverte a matriz hessiana
        
        x0 = P - H_inv*G                #Calcula do ponto x0 

        if (resultado1 != x0[0,0] or resultado2 != x0[1,0]) and k != 0:
            print("Erro - Função não quadrática")
            exit()

        resultado1 = x0[0,0]           #Retira os resultados da matriz
        resultado2 = x0[1,0]
        x = resultado1
        y = resultado2

        print('\nMétodo de Iteração única:')
        print('\nResultado:', resultado1,'\n', resultado2)

        iteracoes.append(k)
        lista_x.append(x)
        lista_y.append(y)
    
    pontos = sg.funcao(expression, symbols, lista_x, lista_y)
        
    sg.plot_convergencia(iteracoes, pontos)
    sg.plot_curvasniveis(expression, symbols, lista_x, lista_y)
    sg.grafico_3d(expression, symbols)
    sg.deslocamento_3d(expression, symbols, lista_x, lista_y)

main()