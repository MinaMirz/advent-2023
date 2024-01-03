"""PART 1"""
with open("input_files/day1a.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    numbers = []
    for line in lines:
        for ch in line:
            try:
                num = int(ch)
                numbers.append(num)
                break
            except ValueError:
                pass
        for i in range(len(line)):
            try:
                ch = line[-i - 1]
                num = int(ch)
                numbers[-1] = int(str(numbers[-1]) + ch)
                break
            except ValueError:
                pass
    print(sum(numbers))

"""PART 2"""

NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
REVERESE_NUMBER_MAP = {key[::-1]: value for key, value in NUMBER_MAP.items()}

with open("input_files/day1b.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    numbers = []
    for line in lines:
        i = 0
        str_end = False
        while not str_end:
            for key, val in NUMBER_MAP.items():
                if line[i] == key[0]:
                    if line[i : i + len(key)] == key:
                        line = line[:i] + str(val) + line[i:]
                        i += 1
            i += 1

            if i == len(line):
                str_end = True

        for ch in line:
            try:
                num = int(ch)
                numbers.append(num)
                break
            except ValueError:
                pass
        for i in range(len(line)):
            try:
                ch = line[-i - 1]
                num = int(ch)
                numbers[-1] = int(str(numbers[-1]) + ch)
                break
            except ValueError:
                pass

    print(sum(numbers))
