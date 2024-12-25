import time

EXAMPLE = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()

# -----------------------------------------------------------------------------

OPEN = "."
BLOCKED = "#"

DIR_KEYS = "^", ">", "v", "<"
DIR_VALS = (-1, 0), (0, 1), (1, 0), (0, -1)


class Guard:

    def __init__(self, pos, idx):
        self.pos = pos
        self.idx = idx

    def next_pos(self):
        r, c = self.pos
        dr, dc = DIR_VALS[self.idx]
        return r + dr, c + dc

    def turn(self):
        self.idx = (self.idx + 1) % 4


class Route:

    def __init__(self, text):
        self.board = text.splitlines()
        self.height = len(self.board)
        self.width = len(self.board[0])
        for r, row in enumerate(self.board):
            for c, tile in enumerate(row):
                if tile in DIR_KEYS:
                    self.board[r] = self.board[r][:c] + OPEN + self.board[r][c + 1 :]
                    self.guard = Guard((r, c), DIR_KEYS.index(tile))
        self.visited = []
        self.log = set()

    def __str__(self):
        string = "\x1b[2J\x1b[H"  # Clear screen and reset cursor
        snapshot = self.board.copy()
        r, c = self.guard.pos
        snapshot[r] = snapshot[r][:c] + DIR_KEYS[self.guard.idx] + snapshot[r][c + 1 :]
        string += "\n".join(' '.join(line) for line in snapshot)
        return string

    __repr__ = __str__

    def in_bounds(self, r, c):
        return (0 <= r < self.height) and (0 <= c < self.width)

    def visit(self, r, c):
        self.visited.append((r, c))
        entry = r, c, self.guard.idx
        if entry in self.log:
            return True
        self.log.add(entry)
        return False

    def play(self, animate=False):
        r, c = self.guard.pos
        while self.in_bounds(r, c):
            if animate:
                self.animate()
            if self.visit(r, c):
                # Loop found
                return True
            for _ in range(3):
                r, c = self.guard.next_pos()
                if not self.in_bounds(r, c):
                    return
                elif self.board[r][c] == BLOCKED:
                    self.guard.turn()
                else:
                    break
            self.guard.pos = r, c
        # Loop not found
        return False

    def animate(self):
        print(self)  # Animate
        time.sleep(0.1)

    def add_obstacle(self, pos):
        r, c = pos
        self.board[r] = self.board[r][:c] + BLOCKED + self.board[r][c + 1 :]


def part1():
    # text, solution = EXAMPLE, 41
    text, solution = open("input.txt").read().strip(), 5153

    r = Route(text)
    r.play()
    count = len(set(r.visited))

    print("Unique positions:", count)
    if solution is not None:
        assert count == solution, f"Expected {solution}, but counted {count}"


def part2():
    #text, solution = EXAMPLE, 6
    text, solution = open("input.txt").read().strip(), 1711

    obstacle_options = []
    tmp = text.splitlines()
    for r, row in enumerate(tmp):
        for c, tile in enumerate(row):
            if tile == OPEN:
                obstacle_options.append((r, c))
                print("\rObstacle options:", len(obstacle_options), end="", flush=True)
    print()
    
    tot = 0
    for i, pos in enumerate(obstacle_options):
        r = Route(text)
        r.add_obstacle(pos)
        if r.play():
            tot += 1
        print(f"\rTested: {i}/{len(obstacle_options)}", end="", flush=True)
    print()

    print("Loop-creating positions:", tot)
    if solution is not None:
        assert tot == solution, f"Expected {solution}, but counted {tot}"

# part1()
part2()
