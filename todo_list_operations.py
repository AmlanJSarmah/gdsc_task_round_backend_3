import json
from utils import get_random_id


def get_todo_list():
    file = open('todo_list.json', 'r')
    data = json.load(file)
    file.close()
    return data


def get_todo_item(item_id):
    file = open('todo_list.json', 'r')
    data = json.load(file)
    file.close()
    for item in data:
        if int(item['item_id']) == int(item_id):
            return item
    return None


def insert_todo_item(item):
    item['item_id'] = get_random_id()
    file = open('todo_list.json', 'r')
    data = json.load(file)
    data.append(item)
    file.close()
    file = open('todo_list.json', 'w')
    json.dump(data, file)
    file.close()
