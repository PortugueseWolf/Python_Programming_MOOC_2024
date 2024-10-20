def longest(strings: list) -> str:
    longest_string = ""

    for i in strings:
        if len(i) > len(longest_string):
            longest_string = i

    return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))