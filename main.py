from Shop import * 

def main():
    while True:
        print('Привет вот функционал: \n1 - получить все товары, \n2 - получить определенный товар, \n3 - создать товар: \n4 - удалить товар, \n5 - обновить товар, \n6 - Фильтр товаров, \n0 - Закрыть программу')
        method = input('Введи число: ')
        if method == '1':
            print(get_data())
        elif method == '2':
            id = int(input('Введи id товара: '))
            print(get_one_data(id))
        elif method == '3':
            print(post_data())
        elif method == '4':
            id = int(input('Введите id товара который хотите удалить: '))
            print(delete_data(id))
        elif method == '5':
            id = int(input('Введите id товара который хотите обновить: '))
            print(update_data(id))
        elif method == '6':
            print(get_data(ge_price=int(input('Введите max значение: '),le_price=(int(input('Введите min значение: '))))))
        elif method == '0':
            break
        else:
            print('Нет такого функционала!')

if __name__ == '__main__':
    main()    



# [
#     {
#         "id": 1,
#         "name": "Samsung",
#         "price": 170.0,
#         "created": "dt",
#         "updated": "",
#         "description": "RAM:16gb, Storage:1Tb",
#         "status": "on sale"

#     },
#     {
#         "id": 2,
#         "name": "IPhone",
#         "price": 230.0,
#         "created": "dt",
#         "updated": "",
#         "description": "RAM:8gb, Storage:256gb",
#         "status": "on sale"
#     },
#     {
#         "id": 3,
#         "name": "Xiaomi",
#         "price": 170.0,
#         "created": "dt",
#         "updated": "",
#         "description": "RAM:6gb, Storage:128gb",
#         "status": "on sale"
#     },
#     {
#         "id": 4,
#         "name": "Poco",
#         "price": 150.0,
#         "created": "dt",
#         "updated": "",
#         "description": "RAM:16gb, Storage:512gb",
#         "status": "saled"
#     }
# ]