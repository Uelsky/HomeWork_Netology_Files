def extraction_from_recipes(recipes: str):
    with open(recipes, 'r', encoding='utf-8') as file:
        cook_book = dict()
        key = ''
        for i in file.readlines():
            string = i.strip('\n')
            if string.isdigit() == False and ' | ' not in string and string != '':
                cook_book.update({string: []})
                key = string
            elif string.isdigit() or string == '':
                continue
            elif ' | ' in string:
                position = string.split(' | ')
                cook_book[key].append({
                                        'ingredient_name': position[0],
                                        'quantity': int(position[1]),
                                        'measure': position[2]
                                        })
        return cook_book

cook_book = extraction_from_recipes('recipes.txt')

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result_dict = dict()
    for i in dishes:
        if i in cook_book:
            for j in range(len(cook_book[i])):
                name = cook_book[i][j]['ingredient_name']
                qua = cook_book[i][j]['quantity']
                meas = cook_book[i][j]['measure']
                if name not in result_dict:
                    result_dict.update({name: {
                                               'measure': meas,
                                               'quantity': qua * person_count
                                               }
                                        })
                else:
                    result_dict[name]['quantity'] += qua * person_count
    return result_dict