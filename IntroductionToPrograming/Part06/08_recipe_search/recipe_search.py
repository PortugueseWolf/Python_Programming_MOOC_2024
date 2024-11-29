def recipe_processor(filename: str) -> dict:
    recipes = {}
    i = 0
    name = ""
    time = 0

    with open(filename) as new_file:
        for line in new_file:
            
            content = line.strip()

            if content == "":
                i = 0
                continue

            if i == 0:
                name = content
            if i == 1:
                time = int(content)
                recipes[name] = [time, []]
            if i > 1:
                recipes[name][1].append(content.lower())

            i += 1

    return recipes

def search_by_name(filename: str, word: str) -> list:
    found_recipes = []
    
    for i in recipe_processor(filename):
        if word.lower() in i.lower():
            found_recipes.append(i)

    return found_recipes

def search_by_time(filename: str, prep_time: int) -> list:
    found_recipes = []

    for i in recipe_processor(filename).items():
        if i[1][0] <= prep_time:
            found_recipes.append(f"{i[0]}, preparation time {i[1][0]} min")

    return found_recipes

def search_by_ingredient(filename: str, ingredient: str) -> list:
    found_recipes = []

    for i in recipe_processor(filename).items():
        for ing in i[1][1]:
            if ingredient.lower() in ing:
                found_recipes.append(f"{i[0]}, preparation time {i[1][0]} min")
    
    return found_recipes

if __name__=="__main__":
    print(search_by_name("recipes1.txt", "cake"))
    print(search_by_time("recipes1.txt", 20))
    print(search_by_ingredient("recipes1.txt", "eggs"))