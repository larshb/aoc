text = open("input.txt").read().strip().splitlines()
ROWS = len(text)
COLS = len(text[0])


def part1():
    XMAS = "XMAS"

    def check(r, c, dr, dc):
        if not (0 <= r < ROWS and 0 <= c < COLS):
            return False
        return all(
            0 <= r + i * dr < ROWS
            and 0 <= c + i * dc < COLS
            and text[r + i * dr][c + i * dc] == XMAS[i]
            for i in range(4)
        )

    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    tot = sum(
        check(r, c, dr, dc)
        for r in range(ROWS)
        for c in range(COLS)
        for dr, dc in directions
    )

    print(tot)


def part2():
    def create_matrix(string):
        return [line.strip() for line in string.strip().splitlines()]

    # Variations (. means don't care)
    XMAS_PATTERNS = [
        ["M.M", ".A.", "S.S"],
        ["S.M", ".A.", "S.M"],
        ["S.S", ".A.", "M.M"],
        ["M.S", ".A.", "M.S"],
    ]

    def check_pattern(square):
        def match_pattern(xmas, square):
            return all(
                square[r][c] == xmas[r][c]
                for r in range(3)
                for c in range(3)
                if xmas[r][c] != "."
            )

        return any(match_pattern(xmas, square) for xmas in XMAS_PATTERNS)

    # Brute force check
    total = sum(
        check_pattern([row[c : c + 3] for row in text[r : r + 3]])
        for r in range(ROWS - 2)
        for c in range(COLS - 2)
    )

    print(total)


part1()
part2()
