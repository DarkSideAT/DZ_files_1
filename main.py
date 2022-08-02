# Домашнее задание «Открытие и чтение файла, запись в файл»:
from pprint import pprint

cook_book = {}

with open('recipe.txt', encoding='utf-8') as file:
    for recipe in file:
        recipes = recipe.strip()
        ingridients = int(file.readline(2))
        recipe_list = []
        for i in range(ingridients):
            ingredient_name, quantity, measure = file.readline().strip().split(" | ")
            recipe_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        cook_book[recipes] = recipe_list
        file.readline()

pprint(cook_book, sort_dicts=False, width=160)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity']\
                    = str(int(ingredients[ingredient['ingredient_name']]['quantity']) + int(ingredient['quantity'])* person_count)
            else:
                ingredients[ingredient['ingredient_name']] \
                = {'quantity' : str(int(ingredient['quantity']) * person_count), 'measure' : ingredient['measure']}
    return ingredients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

with open("1.txt", encoding='utf-8') as f1, open("2.txt", encoding='utf-8') as f2, open("3.txt", encoding='utf-8') as f3:
    file_1 = f1.readlines()
    file_2 = f2.readlines()
    file_3 = f3.readlines()
    files_unsorted = {"1.txt": file_1, "2.txt": file_2, "3.txt": file_3}
    files_sorted = sorted(files_unsorted, key=lambda key: len(files_unsorted[key]))
    print(files_sorted)

with open('result.txt', 'w', encoding='utf-8') as f:
    for item in files_sorted:
        f.write(f"{item}\n{len(files_unsorted[item])}\n {''.join(files_unsorted[item])}\n")