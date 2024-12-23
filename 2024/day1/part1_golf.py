print(sum(abs(a-b)for a,b in zip(*map(sorted,zip(*[[int(x)for x in l.split()]for l in open("input.txt")])))))
