
def estrelas(fim, n=1):
    print('*'*n)
    
    if n < fim: 
        estrelas(fim, n+1)
        print('*'*n)


estrelas(5)