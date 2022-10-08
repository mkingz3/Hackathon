import json

def get_data(ge_price=None,le_price=None):
    with open(SHOP_FILE) as file:
        data = json.load(file)
        # filtered = filter(lambda x: if )
        new_data = []
        if ge_price:
            new_data.extend([i for i in data if i['price'] >= ge_price])
        if le_price:
            new_data.extend([i for i in data if i['price'] <= le_price])
        # for i in data:
        #     if i['price'] <= ge_price:
        #         new_data.append(i)
        # if new_data:
        #     return new_data
        return data
   

SHOP_FILE = 'shop.json'


def get_one_data(id):
    data = get_data()
    one_data = [i for i in data if i['id'] == id]
    if one_data:
        return one_data[0]
    return 'Нет такого товара!'

def post_data():
    data = get_data()
    max_id = max([i['id']for i in data])
    data.append({
        'id': max_id + 1,
        'name': input('Pass name new item: '),
        'price': float(input('Pass price: ')), 
        'created': input('Pass date created: '),
        'update': input('Pass date updated: '),
        'description': input('Pass descriptions: '),
        'status': input('Pass status: ')
        })
    with open(SHOP_FILE, 'w') as file:
        json.dump(data, file)
    return 'Created!'

def update_data(id):
    data = get_data()
    data_update = [i for i in data if i ['id'] == id]
    if data_update:
        index_ = data.index(data_update[0])
        data[index_]['name'] = input('Pass new name: ')
        data[index_]['price'] = float(input('Pass new price: '))
        data[index_]['created'] = input('Pass date created: '),
        data[index_]['update'] = input('Pass date updated: '),
        data[index_]['description'] = input('Pass descriptions: '),
        data[index_]['status'] = input('Pass status: ')
        # with open(SHOP_FILE, 'w') as file:
        #     json.dupm(data, file)
        json.dump(data, open(SHOP_FILE, 'w'))
        return 'Updated!'
    return 'Нет такого товара!'

def delete_data(id):
    data = get_data()
    data_delete = [i for i in data if i['id'] == id]

    if data_delete:
        data.remove(data_delete[0])
        json.dump(data, open(SHOP_FILE, 'w'))
        return 'Deleted!'
    return 'Нет такого товара!'


