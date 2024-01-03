VALID_COUNT = {"red": 12, "green": 13, "blue": 14}


def solve_a():
    with open("input_files/day2a.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        valid_game = {}
        for line in lines:
            game_id, game_plays = line.strip().split(":")
            game_id = int(game_id.strip().split(" ")[1])
            game_plays = game_plays.strip().split(";")
            validator = {"red": 0, "green": 0, "blue": 0}
            valid_game[game_id] = True
            for game in game_plays:
                dice_results = game.strip().split(",")
                for dice_result in dice_results:
                    number, dice = dice_result.strip().split(" ")
                    validator[dice] = int(number)

                for key, val in VALID_COUNT.items():
                    if val < validator[key]:
                        valid_game[game_id] = False
                        break

        sum = 0
        for key, val in valid_game.items():
            # print(key)
            if val:
                sum += key

        print(sum)


def solve_b():
    with open("input_files/day2a.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        game_size = {}
        for line in lines:
            game_id, game_plays = line.strip().split(":")
            game_id = int(game_id.strip().split(" ")[1])
            game_plays = game_plays.strip().split(";")

            game_size[game_id] = {"red": 0, "green": 0, "blue": 0}
            for game in game_plays:
                dice_results = game.strip().split(",")
                for dice_result in dice_results:
                    number, dice = dice_result.strip().split(" ")
                    if game_size[game_id][dice] < int(number):
                        game_size[game_id][dice] = int(number)

    game_power = {}
    for key, num_balls in game_size.items():
        game_power[key] = 1
        for _, num_ball in num_balls.items():
            game_power[key] = game_power[key] * num_ball
    print(game_power)
    sum = 0
    for _, val in game_power.items():
        if val:
            sum += val
    print(sum)


solve_b()
