"""
This time, you'll need to figure out exactly how often each number from the left
list appears in the right list. Calculate a total similarity score by adding up
each number in the left list after multiplying it by the number of times that
number appears in the right list.
"""

count, L = {}, []
for line in open("input.txt").read().strip().splitlines():
    l, r = map(int, line.split())
    L += [l]
    if r in count:
        count[r] += 1
    else:
        count[r] = 1

total = 0
for l in L:
    if l in count:
        total += l*count[l]

print(total)
