cheap = 0
def cheap_drink(d,e):
    if d>=e:
        cheap = e
    else:
        cheap = d
    return cheap

def cheap_burger(a,b,c,cheap):
    if a<=b and a<=c:
        print(a+cheap-50)
    elif a>=b and b<=c:
        print(b+cheap-50)
    else:
        print(c+cheap-50)
    return
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
cheap = cheap_drink(d, e)
cheap_burger(a, b, c, cheap)