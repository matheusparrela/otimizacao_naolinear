#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DE NEWTON
import sympy as sy

def main(): 
  
    sy.init_printing()

    #Condições Iniciais
    x = 3/4
    y = 1/4

    x1 = sy.Symbol('x1')
    x2 = sy.Symbol('x2')

    funcao = ((x1 - 3)**2 + (x2 - 2)**2)
        
    resultado1 = 0
    resultado2 = 0
    controlex = 1
    controley = 1
    k = 0

    while (abs(controlex) > 0.000001) or (abs(controley) > 0.000001):
        
        k = k + 1
        print('\nINTERAÇÃO',k,":")
        
        grad1 = sy.diff(funcao, x1)         #Gradiente da Função
        grad2 = sy.diff(funcao, x2)
        
        a = grad1.subs(x1, x)               #Valor de X no gradiente
        a2 = a.subs(x2, y)

        b = grad2.subs(x1, x)               #Valor de Y no gradiente
        b2 = b.subs(x2, y)

        h11 = sy.diff(grad1, x1)       #Calcula os elementos do hesiano
        h12 = sy.diff(grad1, x2)
        h21 = sy.diff(grad2, x1)
        h22 = sy.diff(grad2, x2)
                                        #Passa as condições iniciais, elementos do hesiano e o gradiente no pontos iniciais para matrizes
        P = sy.Matrix([[x], [y]])            
        H = sy.Matrix([[h11, h12], [h21, h22]])
        G = sy.Matrix([[a2], [b2]])

        H_inv = H.inv()                 #Inverte a matriz do hesiano
       
        x0 = P - H_inv*G                #Calcula do ponto x0 

        resultado1 = x0[0,0]           #Retira os resultados da matriz
        resultado2 = x0[1,0]

        print('\nResultado:', resultado1,'\n          ', resultado2)

        controlex = resultado1 - x          #Calcula a variação dos valores dos pontos encontrados
        controley = resultado2 - y                          

        x = resultado1                      #Atualiza os valores de x e y
        y = resultado2

main()