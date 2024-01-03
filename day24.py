import multiprocessing
import itertools
import numpy as np


def map_world():
    world = []
    with open("input_files/day24.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            part_1, part_2 = line.strip().split("@")
            coord = list(map(int, part_1.strip().split(",")))
            velocity = list(map(int, part_2.strip().split(",")))
            # hail = [[coord[i], velocity[i]] for i in range(3)]
            world.append([coord, velocity])
    return world


def simulate_time(hail, t):
    for _ in range(t):
        for coord in hail:
            coord[0] += coord[1]
    return hail


def move_world_through_time(world):
    for hail in world:
        simulate_time(hail, 1)
    return world


BOUND_S = [-100, 100]
BOUNDS = [200000000000000, 400000000000000]


def find_valid_intersection(hail1, hail2):
    X1, Y1, _ = hail1[0]
    X2, Y2, _ = hail2[0]
    vx1, vy1, _ = hail1[1]
    vx2, vy2, _ = hail2[1]
    A = np.array([[-1, (vx1 / vy1)], [-1, (vx2 / vy2)]])
    B = np.array([Y1 * vx1 / vy1 - X1, Y2 * vx2 / vy2 - X2])

    try:
        solve = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        return False, None
    if (
        solve[0] < BOUNDS[0]
        or solve[0] > BOUNDS[1]
        or solve[1] < BOUNDS[0]
        or solve[1] > BOUNDS[1]
    ):
        return False, solve
    elif (solve[1] - Y1) * vy1 < 0 or (solve[1] - Y2) * vy2 < 0:
        return False, solve
    else:
        return True, solve


def find_formula(hails, speed_bounds):
    # BRUTE FORCE
    # x, y, z, t, X0, Y0, Z0
    # len(hails) * 4 + 3

    A = np.zeros((len(hails) * 6, len(hails) * 4 + 3))
    B = np.zeros(len(hails) * 6)

    k = 0
    for hail in hails:
        X, Y, Z = hail[0]
        vx, vy, vz = hail[1]
        B[6 * k + 0] = X
        B[6 * k + 2] = Y
        B[6 * k + 4] = Z

        A[6 * k + 0][4 * k + 0] = 1
        A[6 * k + 0][4 * k + 3] = vx
        A[6 * k + 1][4 * k + 0] = 1
        A[6 * k + 1][-3] = -1

        A[6 * k + 2][4 * k + 1] = 1
        A[6 * k + 2][4 * k + 3] = vy
        A[6 * k + 3][4 * k + 1] = 1
        A[6 * k + 3][-2] = -1

        A[6 * k + 4][4 * k + 2] = 1
        A[6 * k + 4][4 * k + 3] = vz
        A[6 * k + 5][4 * k + 2] = 1
        A[6 * k + 5][-1] = -1

    for vxt in speed_bounds:
        for vyt in speed_bounds:
            for vzt in speed_bounds:
                A[1::6][:-3:4] = vxt
                A[3::6][:-3:4] = vyt
                A[5::6][:-3:4] = vzt
                try:
                    solve = np.linalg.lstsq(A, B)
                    return solve
                except np.linalg.LinAlgError as e:
                    print(e)
    return None


world = map_world()


def solve_a():
    pairs = list(itertools.combinations(world, 2))
    count = 0
    for pair in pairs:
        valid, _ = find_valid_intersection(*pair)
        if valid:
            count += 1
    print(count)


print(find_formula(world, [0, 100]))
