from pprint import pprint


def create_cook_book(file_recept):
    cooking_book = {}
    for line in file_recept:
        name_dish = line.strip()
        num_lines = int(file_recept.readline().strip())
        ingredients = []
        for line_ in range(num_lines):
            ingredient = {}
            list_ = file_recept.readline().replace("|", "").split()
            ingredient["ingredient_name"] = list_[0]
            ingredient["quantity"] = list_[1]
            ingredient["measure"] = list_[2]
            ingredients.append(ingredient)
        cooking_book[name_dish] = ingredients
        file_recept.readline()
    return cooking_book


with open("recept.txt", "r", encoding="utf-8") as file:
    cook_book = create_cook_book(file)
pprint(cook_book)
