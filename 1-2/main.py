

DIGITS_N: list = [str(x) for x in range(10)]
DIGITS_W: list = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
DIGITS_WTN: dict = {v:i for i,v in enumerate(DIGITS_W)}
DIGITS: list = DIGITS_W + DIGITS_N



def main():
    with(open("input", mode="r") as f):
        lines = f.readlines()
    sum = 0
    for line in lines:
        dil = get_digits_in_line(line)
        sum += int(dil[0] + dil[-1])

    print(sum)

def get_digits_in_line(line):
    dil = []
    for i, _ in enumerate(line):
        for d in DIGITS:
            try:
                if line[i:i+len(d)] == d:
                    if d in DIGITS_W:
                        dil.append(str(DIGITS_WTN[d]))
                    else:
                        dil.append(d)
                continue
            except:
                continue

    return dil

if __name__ == "__main__":
    main()
