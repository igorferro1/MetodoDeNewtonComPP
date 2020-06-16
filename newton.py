import numpy as np
from scipy.misc import derivative

def function(x):
    """ Função que será iterada pelo Método de Newton, buscando sua raíz.
    Parâmetros:
    - x: Variável de entrada da função.
    Retornos:
    - function(x): Função aplicada à variável de entrada.
    """
    return 0

delta = 0
x0 = 0

# Mexer apenas nos parâmetros acima para adaptar o programa ao problema desejado.
# Não é necessário mexer em nada abaixo, a não ser que se deseje mudar o que será printado ou número de iterações (50 é o máximo, o tamanho dos vetores).

aproxRaiz = np.zeros(50)
aproxRaizComDelta = np.zeros(50)
aproxRaiz[0] = x0

for i in range (3):
  aproxRaiz[i+1] = aproxRaiz[i] - (function(aproxRaiz[i]))/derivative(function, aproxRaiz[i], dx=1e-6)

if (aproxRaiz[0] < aproxRaiz[1] and aproxRaiz[1] < aproxRaiz[2]): # Monotona Crescente
  aproxRaiz = np.zeros(50)
  aproxRaizComDelta = np.zeros(50)
  aproxRaiz[0] = x0
  
  for i in range(aproxRaiz.shape[0]-1): #while ()
    aproxRaizComDelta[i] = aproxRaiz[i]+2*delta
    aproxRaiz[i+1] = aproxRaizComDelta[i] - (function(aproxRaizComDelta[i]))/derivative(function, aproxRaizComDelta[i], dx=1e-6)
    
    if(aproxRaiz[i+1] < aproxRaizComDelta[i]):
      print("Iteracao de parada: "+ str(i))
      iteracaoCorreta = i
      break
  solucao = aproxRaiz[iteracaoCorreta] + delta

# Tabela
  print("Sequencia monotona crescente")
  for i in range(iteracaoCorreta+1):
    print("n: " + str(i) + " xn: " + str(aproxRaiz[i]) + " xn+2delta: " + str(aproxRaizComDelta[i]) + " f(xn+2delta): " + str(function(aproxRaizComDelta[i])) + " phi(xn+2delta): " + str(aproxRaiz[i+1]))
  print("A solucao é dada por xn da ultima iteracao completa + delta: x = " + str(solucao))

if (aproxRaiz[0] > aproxRaiz[1] and aproxRaiz[1] > aproxRaiz[2]): # Monotona Decrescente
  aproxRaiz = np.zeros(50)
  aproxRaizComDelta = np.zeros(50)
  aproxRaiz[0] = x0
  
  for i in range(aproxRaiz.shape[0]-1): #while ()
    aproxRaizComDelta[i] = aproxRaiz[i]-2*delta
    aproxRaiz[i+1] = aproxRaizComDelta[i] - (function(aproxRaizComDelta[i]))/derivative(function, aproxRaizComDelta[i], dx=1e-6)
    
    if(aproxRaiz[i+1] > aproxRaizComDelta[i]):
      print("Iteracao de parada: "+ str(i))
      iteracaoCorreta = i
      break
  solucao = aproxRaiz[iteracaoCorreta] - delta

# Tabela
  print("Sequencia monotona decrescente")
  for i in range(iteracaoCorreta+1):
    print("n: " + str(i) + " xn: " + str(aproxRaiz[i]) + " xn-2delta: " + str(aproxRaizComDelta[i]) + " f(xn-2delta): " + str(function(aproxRaizComDelta[i])) + " phi(xn-2delta): " + str(aproxRaiz[i+1]))
  print("A solucao é dada por xn da ultima iteracao completa - delta: x = " + str(solucao))

if((aproxRaiz[0] < aproxRaiz[1] and aproxRaiz[1] > aproxRaiz[2]) or (aproxRaiz[0] > aproxRaiz[1] and aproxRaiz[1] < aproxRaiz[2])): # Oscilante

  aproxRaiz = np.zeros(50)
  aproxRaiz[0] = x0
  
  for i in range(aproxRaiz.shape[0]-1): #while ()
    aproxRaiz[i+1] = aproxRaiz[i] - (function(aproxRaiz[i]))/derivative(function, aproxRaiz[i], dx=1e-6)
    
    if(abs(aproxRaiz[i+1]-aproxRaiz[i])/2 <= delta):
      print("Iteracao de parada: "+ str(i))
      iteracaoCorreta = i
      break
  solucao = (aproxRaiz[iteracaoCorreta+1] + aproxRaiz[iteracaoCorreta])/2

# Tabela
  print("Sequencia oscilante")
  for i in range(iteracaoCorreta+1):
    print("n: " + str(i) + " xn: " + str(aproxRaiz[i]) + " phi(xn): " + str(aproxRaiz[i+1]))
  print("A solucao é dada por um ponto médio entre xn e xn+1: x = " + str(solucao))

print("O valor para a função no ponto encontrado será: " + str(function(solucao)))
