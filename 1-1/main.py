DIGITS: list = [str(x) for x in range(10)]

def main():
    with(open("input", mode="r") as f):
        lines = f.readlines()
    sum = 0
    for line in lines:
        sum += int(get_first_digit(line) + get_last_digit(line))

    print(sum)

def get_first_digit(line: str) -> str:
    for v in line:
        if v in DIGITS:
            return v
    raise Exception("no digit found")

def get_last_digit(line: str) -> str:
    for v in reversed(line):
        if v in DIGITS:
            return v
    raise Exception("no digit found")

if __name__ == "__main__":
    main()
