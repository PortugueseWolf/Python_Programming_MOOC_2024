def first_word(sentence):
    if " " in sentence:
        index = sentence.find(" ")
        return sentence[:index]
    return sentence

def second_word(sentence): 
    if " " in sentence: # primeira
        index = sentence.find(" ")
        sentence = sentence[index + 1:]
        
    if " " in sentence: # segunda
        index = sentence.find(" ")
        sentence = sentence[:index]
    
    return sentence


def last_word(sentence):
    while True:
        if " " in sentence:
            index = sentence.find(" ")
            sentence = sentence[index + 1:]
        else:
            return sentence


if __name__ == "__main__":
    
    sentence = "it was a dark and stormy python"
    print(first_word("First Second"))
    print(second_word("First Second"))
    print(last_word("First Second Third"))