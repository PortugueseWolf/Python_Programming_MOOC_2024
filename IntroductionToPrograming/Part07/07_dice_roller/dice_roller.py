from random import choice

def roll(dye: str) -> int:
    a = [3, 3, 3, 3, 3, 6]
    b = [2,5]
    c = [1, 4, 4, 4, 4, 4]

    if dye == "A":
        return choice(a)
    
    if dye == "B":
        return choice(b)
    
    return choice(c)

def play(die1: str, die2: str, times: int) -> tuple:
    win1 = 0
    win2 = 0
    tie = 0

    for i in range(times):
        first = roll(die1)
        second = roll(die2)

        if first > second:
            win1 += 1
        elif first < second:
            win2 += 1
        else:
            tie += 1
    
    return (win1, win2, tie)

if __name__ == "__main__":
    for i in range(100):
        print(roll("A"))
