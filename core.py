from datetime import datetime

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += \
                    new_shop_list_item['quantity']
    return shop_list


def formated_list_item(item):
    return '{} {} {}'.format(item['ingridient_name'], item['quantity'], item['measure'])


def go_over_list(items_dict, callback):
    for list_item in items_dict.values():
        callback(list_item)


def print_shop_list(item):
    print(formated_list_item(item))


def write_products_order_list(item):
    with open('products_order_list.txt', encoding='utf8', mode='a') as order_list:
        order_list.write('{}\n'.format(formated_list_item(item)))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

    go_over_list(shop_list, print_shop_list)

    with open('products_order_list.txt', encoding='utf8', mode='w') as order_list:
        order_list.write('{}\n'.format(datetime.now()))

    go_over_list(shop_list, write_products_order_list)
