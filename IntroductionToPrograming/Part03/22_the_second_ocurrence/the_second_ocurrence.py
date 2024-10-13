user_input = input("Please type in a string: ")
sub_string = input("Please type in a substring: ")

# abababa
# 0123456
# 1   2

if sub_string in user_input:
    index = user_input.find(sub_string) # 0
    if sub_string in user_input[index + len(sub_string):]: # 0 + 3 = 3 (baba)
        second_index = user_input[index + len(sub_string):].find(sub_string) # = 1
        print(f"The second occurrence of the substring is at index {index + second_index + len(sub_string)}.")
    else:
        print("The substring does not occur twice in the string.")

else: 
    print("The substring does not occur twice in the string.")
