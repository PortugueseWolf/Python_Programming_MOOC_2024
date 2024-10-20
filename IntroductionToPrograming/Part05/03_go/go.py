def who_won(game_board: list) -> int:
    player_one = 0
    player_two = 0

    for i in game_board:
        player_one += i.count(1)
        player_two += i.count(2)
    
    if player_one > player_two:
        return 1
    if player_one < player_two:
        return 2
    return 0
