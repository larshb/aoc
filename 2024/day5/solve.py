DATASETS = {
    "example": {
        "path": "example.txt",
        "part1": 143,
        "part2": 123,
    },
    "input": {
        "path": "input.txt",
        "part1": 7024,
        "part2": 4151,
    },
}


def parse_input(path):

    with open(path, "r") as file:
        lines = file.read().strip().splitlines()

    order, updates = [], []
    for line in lines:
        if "|" in line:
            try:
                a, b = map(int, line.split("|"))
                order.append((a, b))
            except ValueError:
                pass
        elif "," in line:
            try:
                updates.append(list(map(int, line.split(","))))
            except ValueError:
                pass

    return order, updates


def is_valid(update, order):
    for a, b in order:
        if b in update:
            b_index = update.index(b)
            if a in update[b_index + 1 :]:
                return False
    return True


def part1(dataset):

    order, updates = parse_input(dataset["path"])

    total = sum(
        update[(len(update) - 1) // 2] for update in updates if is_valid(update, order)
    )

    if dataset["part1"] is not None:
        assert (
            total == dataset["part1"]
        ), f"Wrong answer. Expected {dataset['part1']}, got {total}"

    print(f"Part 1: {total}")


def part2(dataset):

    order, updates = parse_input(dataset["path"])

    def correct(update):
        def step(update):
            changed = False
            for a, b in order:
                for i in range(len(update)):
                    while update[i] == b and a in update[i + 1 :]:
                        update[i], update[i + 1] = update[i + 1], update[i]
                        changed = True
                        i += 1
            return changed

        while step(update):
            pass

        return update

    corrected_updates = []
    for update in updates:
        if not is_valid(update, order):
            corrected_updates += [correct(update)]

    total = sum(update[(len(update) - 1) // 2] for update in corrected_updates)

    if dataset["part2"] is not None:
        assert (
            total == dataset["part2"]
        ), f"Wrong answer. Expected {dataset['part2']}, got {total}"

    print(f"Part 2: {total}")


if __name__ == "__main__":
    part1(DATASETS["input"])
    part2(DATASETS["input"])
