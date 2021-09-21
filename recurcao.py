def print_estrelas(n, fim):
    for i in range(n):
        print('*', end='')
    print()
    
    if n < fim: 
        print_estrelas(n+1, fim)
    
    for i in range(n):
        print('*', end='')
    print()


def estrelas(n):
    print_estrelas(0, n)

estrelas(4)