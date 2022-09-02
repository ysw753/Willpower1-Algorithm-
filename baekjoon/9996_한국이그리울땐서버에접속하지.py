import sys
sys.stdin=open("input.txt", "r")

n=int(input())
pattern = input()

star = pattern.index('*')
before, after = pattern[:star], pattern[star+1]
for _ in range(n):
    name = input()

    if before in name and after in name:
        idx_b = name.index(before)
        idx_a = name.index(after)

        if idx_b == 0 and idx_b+len(before) <= idx_a and name[::-1].index(after[::-1]) == 0:
            print('DA')
            continue

    print('NE')
  