from pprint import pprint
from cook_book import create_cook_book, get_shop_list_by_dishes


with open("recept.txt", "r", encoding="utf-8") as file:
    cook_book = create_cook_book(file)
pprint(cook_book)

list_dishes_for_person = get_shop_list_by_dishes(['Омлет', 'Пельмени', 'Запеченный картофель'], 3, cook_book)
pprint(list_dishes_for_person)
