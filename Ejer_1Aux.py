num = int(input("Intro Numero"))

m=1
n=0

x=num

while x >= 2:
    dig= x % 2
    x = x // 2
    n=n+(dig*m)
    m=m*10

n=n+(x*m)

print (f"{num} en base 2 es: {n}")


