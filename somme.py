def somme(m, n):
    total = 0
    a = max( m, n )
    b = min( m, n )
    for i in range( b, a + 1 ):
        total += i
    return total

print(somme(1,10))