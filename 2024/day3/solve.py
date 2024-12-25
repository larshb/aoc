import re

# Part 1
print(sum(int(a)*int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", open("input.txt").read())))

# Part 2
is_enabled = True
code = open("input.txt").read()
total = 0
for i in range(len(code)):
    if code[i:].startswith("do()"):
        is_enabled = True
    elif code[i:].startswith("don't()"):
        is_enabled = False
    if is_enabled and (capt := re.match(r"^mul\((\d{1,3}),(\d{1,3})\)", code[i:])):
        a, b = capt.groups()
        total += int(a) * int(b)
print(total)
