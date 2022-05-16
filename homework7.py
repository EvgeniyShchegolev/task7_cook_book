from pprint import pprint
from cook_book import create_cook_book


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


# ДЗ 7-1
with open("recept.txt", "r", encoding="utf-8") as file:
    cook_book = create_cook_book(file)
pprint(cook_book)

# ДЗ 7-2
list_dishes_for_person = get_shop_list_by_dishes(['Омлет', 'Пельмени', 'Запеченный картофель'], 3)
pprint(list_dishes_for_person)
