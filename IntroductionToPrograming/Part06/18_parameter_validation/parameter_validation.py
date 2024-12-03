def new_person(name: str, age: int) -> tuple:
    splitter = name.split(" ")
    if name == "" or len(splitter) <= 1 or len(name) > 40:
        raise ValueError("Name cannot be empty, cannot be less than two words or be more than 40 characters")
        
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150, included")
        
    return (name,age)
