from core import create_shop_list

with open('recipes.txt', encoding='utf8') as recipes:
    cook_book = dict()

    for line in recipes:
        recipe_name = line.strip()
        cook_book[recipe_name] = list()

        ingridients_count = int(recipes.readline().strip())

        for i in range(ingridients_count):
            ingridient = recipes.readline().strip().split(' | ')

            ingridient_name = ingridient[0]
            ingridient_quantity = int(ingridient[1])
            ingridient_measure = ingridient[2]

            ingridient = {
                'ingridient_name': ingridient_name,
                'quantity': ingridient_quantity,
                'measure': ingridient_measure
            }

            cook_book[recipe_name].append(ingridient)

        recipes.readline()

    create_shop_list(cook_book)
