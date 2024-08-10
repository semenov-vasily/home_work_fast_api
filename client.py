import requests

# -----Запросы для записи, получения, изменения и удаления объявления в бд-----

# -----Запись нового объявления-------------------------------------------------
# response = requests.post('http://127.0.0.1:8000/v1/advertisement/',
#                         json={
#                             'name': "advertisement_1",
#                             'description': 'text of description 1',
#                             'price': 100,
#                             'author': 'Petya Pypkin'
#                         })
# print(response.json())
# print(response.status_code)


# -----Изменение объявления  по его id-----------------------------------------------
# response = requests.patch('http://127.0.0.1:8000/v1/advertisement/2/',
#                           json={
#                               'name': "advertisement_123",
#                               'description': 'text of description aaaaaaccccasdafa',
#                               'price': 200,
#                               'author': 'Petya Pypkin'
#                           })
# print(response.json())
# print(response.status_code)


# -----Удаление объявления по его id---------------------
# response = requests.delete('http://127.0.0.1:8000/v1/advertisement/2/',)
# print(response.json())
# print(response.status_code)


# -----Получение объявления по его id----------
response = requests.get('http://127.0.0.1:8000/v1/advertisement/1/', )
print(response.json())
print(response.status_code)


# -----Получение объявления по полю id----------
response = requests.get('http://127.0.0.1:8000/v1/advertisement_id?advertisement_id=1', )
print(response.json())
print(response.status_code)


# -----Получение объявления по полю author----------
response = requests.get('http://127.0.0.1:8000/v1/advertisement_author?author=Petya Pypkin', )
print(response.json())
print(response.status_code)


# -----Получение объявления по полю author через id----------
response = requests.get('http://127.0.0.1:8000/v1/advertisement_author_id?author=Petya Pypkin', )
print(response.json())
print(response.status_code)