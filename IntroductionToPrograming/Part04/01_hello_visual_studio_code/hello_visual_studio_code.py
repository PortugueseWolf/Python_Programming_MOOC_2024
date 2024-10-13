while True:
    editor = input("Editor: ")
    lower = editor.lower()
    if lower == "word" or lower == "notepad":
        print("awful")
    elif lower == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")
