def is_safe(arr, has_dampener=False):

    def check(diff, direction):
        return (abs(diff) > 3 or diff == 0) or (diff > 0 and direction == -1) or (diff < 0 and direction == +1)

    diff0 = arr[1] - arr[0]
    direction = +1 if diff0 > 0 else -1
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if check(diff, direction):
            if has_dampener:
                has_dampener = False
                if i == 1:
                    direction = +1 if arr[2]-arr[1] > 0 else -1
            else:
                return False
    return True

def part1():
    tot = 0
    for line in open("input.txt").read().strip().splitlines():
        arr = list(map(int, line.split()))
        if is_safe(arr):
            tot += 1
    print(tot)

def part2():
    tot = 0
    for line in open("input.txt").read().strip().splitlines():
        arr = list(map(int, line.split()))
        try:
            if is_safe(arr, has_dampener=True):
                tot += 1
        except:
            pass
    print(tot)
