def create_cook_book(file_recept):
    cooking_book = {}
    for line in file_recept:
        name_dish = line.strip()
        num_lines = int(file_recept.readline().strip())
        ingredients = []
        for line_ in range(num_lines):
            ingredient = {}
            list_ = file_recept.readline().replace("|", "").split()
            ingredient["ingredient_name"] = " ".join(list_[:-2])
            ingredient["quantity"] = int(list_[-2])
            ingredient["measure"] = list_[-1]
            ingredients.append(ingredient)
        cooking_book[name_dish] = ingredients
        file_recept.readline()
    return cooking_book


def get_shop_list_by_dishes(dishes, person_count):
    list_ingr = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                ingr_name = ingr["ingredient_name"]
                if ingr_name not in list_ingr:
                    list_ingr[ingr_name] = {"measure": ingr["measure"], "quantity": ingr["quantity"] * person_count}
                else:
                    list_ingr[ingr_name]["quantity"] += ingr["quantity"] * person_count
        else:
            print(f'Ошибка ввода данных: блюда "{dish}" нет в кулинарной книге!')
    return list_ingr