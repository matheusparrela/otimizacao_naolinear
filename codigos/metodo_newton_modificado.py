#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DE NEWTON MODIFICADO   
import sympy as sy

def main(): 
  
    sy.init_printing()

    #Condições Iniciais
    x = 0.5
    y = 0.5
   
    x1 = sy.Symbol('x1')
    x2 = sy.Symbol('x2')
    alfa = sy.Symbol('alfa')

    funcao = 2*x1**2 - 1.05*x1**4 + ((x1**6)/6) +  x1*x2 + x2**2
    
    resultado1 = 0
    resultado2 = 0
    controlex = 1
    controley = 1
    k = 0

    while (abs(controlex) > 0.00001) or (abs(controley) > 0.00001):
        
        k = k + 1
        print('\nITERAÇÃO',k,":")

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
        
        #Passa as condições iniciais, elementos da hessiana e o gradiente no pontos iniciais para matrizes

        hessiana = sy.Matrix([[h11, h12],[h21, h22]]) 
        gradiente = sy.Matrix([[a2], [b2]])

        new_h = hessiana.subs(x1, x)        #Substitui os valores das incognitas pelos pontos iniciais
        hessiana = new_h.subs(x2, y)

        inv_hessiana = hessiana.inv()       #Inverte a matriz hessiana

        prod = -inv_hessiana*gradiente      #Calcula o produto das matrizes

        y1 = (x + alfa*prod[0,0])
        y2 = (y + alfa*prod[1,0])

        funcao1 = funcao.subs(x1, y1)       #Substituição de de y1 e y2 na função 
        funcao2 = funcao1.subs(x2, y2)

        d1 = sy.diff(funcao2, alfa)         #Derivada da função em relação a alfa

        raiz = (sy.solve(d1))               #Raiz da derivada da função
        raiz = raiz[0]

        resultado1 = y1.subs(alfa, raiz)    #Substitui o valor da raiz de alfa na expressão de alfa
        resultado2 = y2.subs(alfa, raiz)
        print('Ponto X1:',float((resultado1)),'\nPonto X2:',float(resultado2))
     
        controlex = resultado1 - x          #Calcula a variação dos valores dos pontos encontrados
        controley = resultado2 - y
                         
        x = resultado1                      #Atualiza os valores de x e y
        y = resultado2
        
main()