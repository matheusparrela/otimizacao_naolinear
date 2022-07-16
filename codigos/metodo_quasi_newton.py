#OTIMIZAÇÃO NÃO LINEAR - MÉTODO DE QUASI NEWTON  
#Nâo funciona 
from numpy import gradient
import sympy as sy

def main(): 
  
    sy.init_printing()

    #Condições Iniciais
    x = 0.5
    y = 0.5
   
    inicio = sy.Matrix([[x],[y]])

    x1 = sy.Symbol('x1')
    x2 = sy.Symbol('x2')
    alfa = sy.Symbol('alfa')

    funcao = 2*x1**2 - 1.05*x1**4 + ((x1**6)/6) +  x1*x2 + x2**2
    
    hessiana = sy.Matrix([[1, 0],[0, 1]]) 

    grad = sy.Matrix([[funcao.diff(x1)],[funcao.diff(x2)]]) 
   
    gradiente = grad.subs(x1, x)
    gradiente = gradiente.subs(x2, y)
    
    k = 0

    while k < 1:

        k +=1

        dk = -hessiana*gradiente

        fun = inicio + alfa*dk
        
        funcao1 = funcao.subs(x1, fun[0,0])
        funcao1 = funcao1.subs(x2, fun[1,0])
        
        d1 = sy.diff(funcao1, alfa)         #Derivada da função em relação a alfa
       
        raiz = (sy.solve(d1))               #Raiz da derivada da função

        try:               
            raiz = raiz[0]

        except:
            print("Erro")
            exit()

        resultado1 = fun[0,0].subs(alfa, raiz)    #Substitui o valor da raiz de alfa na expressão de alfa
        resultado2 = fun[1,0].subs(alfa, raiz)

        resultado = sy.Matrix([[resultado1], [resultado2]])

        print('\nITERAÇÃO',k,":")
        print(resultado1,'\n',resultado2)

        gradiente1 = grad.subs(x1, resultado1)
        gradiente1 = gradiente1.subs(x2, resultado2)

        vk = inicio - resultado

        rk = gradiente - gradiente1

      
        print(rk.T)

        print(rk)

        ck  = (vk * rk.inv()) - hessiana

        ck2 = (1 + hessiana*rk*vk.inv()) - hessiana + (hessiana*rk*vk*sy.inv(rk.T*vk.T))
        print(ck)  

main()