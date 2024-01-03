def check_number_end(j, row):
    if j == len(row) - 1:
        return True
    elif not row[j + 1].isdigit():
        return True
    else:
        return False


def check_number_start(j, row):
    if j == 0:
        return True
    elif not row[j - 1].isdigit():
        return True
    else:
        return False


def parse_number(j, row):
    num_parse = ""
    counter = j
    while not check_number_end(counter, row):
        counter += 1
    while not check_number_start(counter, row):
        num_parse = row[counter] + num_parse
        counter += -1
    num_parse = row[counter] + num_parse
    counter = j
    return int(num_parse)


def search_adjacent_symbol(i, j, matrix):
    frwd = j

    while frwd < len(matrix[i]) and matrix[i][frwd].isdigit():
        frwd += 1
        try:
            if not matrix[i][frwd].isdigit() and matrix[i][frwd] != ".":
                return True
        except ValueError as err:
            print(err)

    back = j
    while back >= 0 and matrix[i][back].isdigit():
        back += -1
        try:
            if not matrix[i][back].isdigit() and matrix[i][back] != ".":
                return True
        except ValueError as err:
            print(err)
    try:
        upper_row = back
        while upper_row <= frwd:
            if (
                not matrix[i - 1][upper_row].isdigit()
                and matrix[i - 1][upper_row] != "."
            ):
                return True
            upper_row += 1
    except ValueError as err:
        print(err)
    try:
        lower_row = back
        while lower_row <= frwd:
            if (
                not matrix[i + 1][lower_row].isdigit()
                and matrix[i + 1][lower_row] != "."
            ):
                return True
            lower_row += 1
    except ValueError as err:
        print(err)
    return False


def search_adjacent_number(matrix, i, j):
    nums = []
    if i == 5:
        print(matrix[i][j])
    try:
        if matrix[i - 1][j].isdigit():
            nums.append(parse_number(j, matrix[i - 1]))
        else:
            try:
                if matrix[i - 1][j + 1].isdigit():
                    nums.append(parse_number(j + 1, matrix[i - 1]))
            except ValueError as err:
                print(err)
            try:
                if matrix[i - 1][j - 1].isdigit():
                    nums.append(parse_number(j - 1, matrix[i - 1]))
            except ValueError as err:
                print(err)
    except ValueError as err:
        print(err)
    try:
        if matrix[i + 1][j].isdigit():
            nums.append(parse_number(j, matrix[i + 1]))
        else:
            try:
                if matrix[i + 1][j + 1].isdigit():
                    nums.append(parse_number(j + 1, matrix[i + 1]))
            except ValueError as err:
                print(err)
            try:
                if matrix[i + 1][j - 1].isdigit():
                    nums.append(parse_number(j - 1, matrix[i + 1]))
            except ValueError as err:
                print(err)
    except ValueError as err:
        print(err)
    try:
        if matrix[i][j + 1].isdigit():
            nums.append(parse_number(j + 1, matrix[i]))
    except ValueError as err:
        print(err)
    try:
        if matrix[i][j - 11].isdigit:
            nums.append(parse_number(j - 1, matrix[i]))
    except ValueError as err:
        print(err)
    return nums


def solve_a():
    with open("input_files/day3.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        matrix = []
        sums = 0
        for line in lines:
            line = line.strip()
            matrix.append([*line])
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell.isdigit() and check_number_end(j, row):
                    num = parse_number(j, row)
                    i_search = i
                    j_search = j
                    if search_adjacent_symbol(i_search, j_search, matrix):
                        sums += num
    return sums


def solve_b():
    with open("input_files/day3.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        matrix = []
        sums = 0
        for line in lines:
            line = line.strip()
            matrix.append([*line])
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == "*" and not cell.isdigit():
                    nums = search_adjacent_number(matrix, i, j)
                    if len(nums) == 2:
                        sums += nums[0] * nums[1]

    return sums


ans = solve_b()
print(ans)
