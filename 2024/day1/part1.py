from pathlib import Path

input_file = Path(__file__).parent / "input.txt"

data = [[], []]
for line in open(input_file).read().strip().splitlines():
    a, b = map(int, line.split())
    data[0] += [a]
    data[1] += [b]

data = [sorted(data[0]), sorted(data[1])]
total = sum(abs(a-b) for a, b in zip(*data))
print(total)
