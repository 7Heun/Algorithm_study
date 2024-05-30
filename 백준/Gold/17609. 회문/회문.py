import sys
input = sys.stdin.readline
print = sys.stdout.write

def is_pseudo_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            temp1 = s[:left] + s[left+1:]
            if temp1 == temp1[::-1]:
                return True
            temp2 = s[:right] + s[right+1:]
            if temp2 == temp2[::-1]:
                return True
            return False
        left += 1
        right -= 1
    return True

T = int(input())
for _ in range(T):
    s = input().strip()
    if s == s[::-1]:
        print('0\n')
    elif is_pseudo_palindrome(s):
        print('1\n')
    else:
        print('2\n')