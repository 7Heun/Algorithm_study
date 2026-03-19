import sys
input = sys.stdin.readline

def check():
    for i in range(n-1):
        if phone[i+1].startswith(phone[i]):
            return "NO"
    return "YES"

t = int(input())

for _ in range(t):
    n = int(input())
    phone = [input().strip() for _ in range(n)]
    phone.sort()
    print(check())
