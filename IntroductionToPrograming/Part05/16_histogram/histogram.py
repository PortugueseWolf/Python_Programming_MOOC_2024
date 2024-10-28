def histogram(word: str) -> None:
    counter = {}

    for c in word:
        if c not in counter:
            counter[c] = 0
        
        counter[c] += 1
    
    for key, value in counter.items():
        print(key, "*" * value)

if __name__ == "__main__":
    histogram("test")