

def fiboRec(n):
    if n <= 1:
        return 1
    return fiboRec(n-1) + fiboRec(n-2)



def fibo(n):

    a,b = -1,1

    while n:
        c = a + b
        a,b = b,c
        n -= 1

    return c


def factRec(n):
    if n <= 1:
        return 1
    return n*factRec(n-1)



def fact(n):

    res = 1

    while n>1:
        
        res *= n
        n -= 1

    return res