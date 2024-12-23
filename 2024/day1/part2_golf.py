count, L = {}, []
for line in open("input.txt").read().strip().splitlines():
    l, r = map(int, line.split())
    L += [l]
    if r in count:
        count[r] += 1
    else:
        count[r] = 1

total = sum(l*count[l] for l in L if l in count)
assert total == 24869388