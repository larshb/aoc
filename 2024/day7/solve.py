data, solution = open("input.txt").read().strip().splitlines(), 3749

OPERATORS = [
    lambda a, b: a + b,
    lambda a, b: a * b,
]

# Part 2
OPERATORS += [lambda a, b: int(str(a) + str(b))]

bridges = []
for line in data:
    target, args = line.split(": ")
    target = int(target)
    args = [int(a) for a in args.split()]
    bridges.append((target, args))

def reduce(imm, arr):
    if len(arr) == 1:
        for op in OPERATORS:
            yield op(imm, arr[0])
        return
    for op in OPERATORS:
        new = op(imm, arr[0])
        for res in reduce(new, arr[1:]):
            yield res

tot = 0
for target, args in bridges:
    for res in reduce(args[0], args[1:]):
        if target == res:
            tot += target
            print(f"{target}: {' '.join(map(str, args))}", "=>", tot)
            break
print(tot)
