def create_cook_book(file_recept):
    """
    Функция принимает переменную после прочтения с файла txt и
    возвращает отформатированные данные ввиде словаря с вложениями
    """
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
