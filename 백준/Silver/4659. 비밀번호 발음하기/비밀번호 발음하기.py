import sys
input = sys.stdin.readline

def is_acceptable(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    have_vowel = False
    for v in vowels:
        if v in s:
            have_vowel = True
            break
    if not have_vowel:
        return False
    for i in range(len(s)-1):
        if s[i] == s[i+1] and not (s[i] == 'e' or s[i] == 'o'):
            return False
        if i > len(s)-3: continue
        if s[i] in vowels:
            if s[i+1] in vowels and s[i+2] in vowels:
                return False
        else:
            if s[i+1] not in vowels and s[i+2] not in vowels:
                return False
    return True         

while True:
    pw = input().strip()
    if pw == "end":
        break
    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")