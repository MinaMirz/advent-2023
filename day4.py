def play_games():
    with open("input_files/day4s.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        game_results = {}
        for line in lines:
            card_id, game = line.strip().split(":")
            card_str, our_str = game.split("|")
            card_nums = card_str.strip().split(" ")
            our_nums = our_str.strip().split(" ")
            print(our_nums)
            count = 0
            for number in our_nums:
                if number in card_nums and number != "":
                    if count == 0:
                        count = 1
                    else:
                        count = count * 2
            game_results[card_id] = count
    return game_results


def play_games_2():
    with open("input_files/day4.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        game_results = {}
        for line in lines:
            card_id, game = line.strip().split(":")
            card_id = card_id.split(" ")[-1]
            card_str, our_str = game.split("|")
            card_nums = card_str.strip().split(" ")
            our_nums = our_str.strip().split(" ")
            print(our_nums)
            count = 0
            for number in our_nums:
                if number in card_nums and number != "":
                    count += 1
            game_results[card_id] = count
    return game_results


def count_score(game_results):
    sum = 0
    for res in game_results.values():
        sum += res
    return sum


def read_card_id(id_str):
    return int(id_str.split(" ")[1])


def count_cards(game_results):
    scratch_count = {game_id: 1 for game_id in game_results.keys()}
    print(game_results)
    for i in range(len(scratch_count)):
        game_id = str(i + 1)
        score = game_results[game_id]
        num_card = scratch_count[game_id]
        for n in range(num_card):
            for j in range(score):
                id_num = int(game_id) + 1 + j
                new_id = str(id_num)
                if id_num == 6:
                    print(scratch_count)
                try:
                    scratch_count[new_id] = scratch_count[new_id] + 1
                except KeyError:
                    print(f"{new_id} reached end of deck")
    sums = 0
    for cards in scratch_count.values():
        sums += cards
    return sums


print(count_cards(play_games_2()))
