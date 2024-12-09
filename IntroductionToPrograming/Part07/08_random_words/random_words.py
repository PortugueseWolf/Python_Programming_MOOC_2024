from random import sample

def words(n: int, beginning: str) -> list:
    correct_words = []

    try:
        with open("words.txt", "r") as new_file:
            for line in new_file:
                line = line.strip()
                if line.startswith(beginning):
                    correct_words.append(line)
    except:
        print("Couldn't open the file!")

    if len(correct_words) < n:
        raise ValueError

    return sample(correct_words, n)