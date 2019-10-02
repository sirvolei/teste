#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Verifica se há necessidade de pivotamento, caso positivo faz o pivotamento
# (inteiro, vetor, matriz) -> none
from numpy import *
def pivo(col, b, M): 
    n = len(M)
    jmax = col
    for k in range(col+1,n):
        if abs(M[k][col]) > abs(M[jmax][col]): jmax = k
    M[col],M[jmax] = M[jmax], M[col]
    b[col], b[jmax] = b[jmax], b[col]

#Torna a matriz nxn em uma matriz triangular superior
# (Matriz, vetor) -> (Matriz, vetor)
def trian(M,b):
    n = len(M)
    for k in range(0,n-1):
        pivo(k, b, M)
        for t in range(k+1,n):
            divisor = M[t][k]/M[k][k]
            for col in range(k,n):
                M[t][col] = M[t][col] - M[k][col]*divisor 
            b[t] = b[t] - b[k]*divisor
    return M, b

#Faz a retrosubstituição e devolve uma lista com as soluções
# (Matriz, vetor) -> vetor
def sub(M, b):
    n = len(b)
    sol = [0]*n
    sol[n-1] = b[n-1]/M[n-1][n-1]
    for k in range(n-2,-1,-1):
        print(M)
        soma = b[k]
        for j in range(k+1,n):
            soma -= M[k][j]*sol[j]
        sol[k] = soma/M[k][k]
    return sol

#Função principal que define a solução do sistema linear
def gauss(M, b):
    mat, vet = trian(M, b)
    solucao = sub(mat, vet)
    return solucao

# Função que resolve o problema dado
def main():
    matriz = [ [ 0 , 5 , -1 ] , [11 , 0 , 1] , [ 1 , -1 , -1]]
    vetor = [5,14,0]
    sol = gauss(matriz, vetor)
    print('\n')
    for k in range(len(sol)):
        print('i_{} = {}'.format(k, sol[k]))
if __name__ == "__main__":
    main()

