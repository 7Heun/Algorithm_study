import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
brr = list(map(int, input().split()))

def bin_search(val):
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        if val > arr[mid]:
            low = mid+1
        elif val < arr[mid]:
            high = mid-1
        else:
            return True
    return False

for b in brr:
    print(1 if bin_search(b) else 0)