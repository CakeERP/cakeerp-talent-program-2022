
a = int(input('Primeiro numero: '))
b  = int(input('Segundo numero : '))
c = int(input('Terceiro numero: '))

if(c > b):
    aux = c
    c = b
    b = aux
if(b > a):
    aux = b
    b = a
    a = aux

if(c > b):
    aux = c
    c = b
    b = aux

print(a,b,c)
