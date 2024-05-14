n1, n2 = map(int, input().split())
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(n1, n2))
print(lcm(n1, n2))