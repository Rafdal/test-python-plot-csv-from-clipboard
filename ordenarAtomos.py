


















""" from scanf import scanf

buf = ''
c= 0
x = []
p = []
g = []

ordenado = []

while 1:
    buf = input('Ingrese un elemento con periodo y grupo X(P,G): ')
    if buf == '0':
        print(x)
        print(p)
        print(g)
    result = scanf("%c(%d,%d)", buf)
    x.append(result[0])
    p.append(result[1])
    g.append(result[2])

    print(result)
    pass

def ordenar(X, P, G):

     """
    