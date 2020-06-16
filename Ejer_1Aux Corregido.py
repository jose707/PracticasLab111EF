def cociente(num):
    c=0
    while num >= 2:
        num=num-2
        c += 1
    return (c)

def resto(num2):
    while num2 >= 2:
        num2=num2-2
    return (num2)


numero = int(input("Intro Numero"))

m=1
n=0
x=numero

while x >= 2:

    dig=resto(x)
    x = cociente(x)

    n=n+(dig*m)
    m=m*10

n=n+(x*m)

print (f"{numero} en base 2 es: {n}")


