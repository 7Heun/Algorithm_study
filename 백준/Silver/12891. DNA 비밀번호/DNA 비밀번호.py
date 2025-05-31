import sys
input = sys.stdin.readline

S, P = map(int, input().split())
dna = list(input().strip())
A, C, G, T = map(int, input().split())
min_cnt = {'A': A, 'C': C, 'G': G, 'T': T}

ans = 0
left = 0
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

def is_acceptable():
    for char in min_cnt:
        if min_cnt[char] > count[char]:
            return False
    return True

for i in range(P-1):
    count[dna[i]] += 1

for right in range(P-1, S):
    count[dna[right]] += 1
    if is_acceptable():
        ans += 1
    count[dna[left]] -= 1
    left += 1

print(ans)