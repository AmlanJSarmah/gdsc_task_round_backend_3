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


def update_todo_item(item_id, new_data):
    file = open('todo_list.json', 'r')
    data = json.load(file)
    file.close()
    for i in range(len(data)):
        if int(data[i]['item_id']) == int(item_id):
            data[i] = new_data
            data[i]['item_id'] = str(item_id)
            file = open('todo_list.json', 'w')
            json.dump(data, file)
            file.close()
            return 0
    return 1


def delete_todo_item(item_id):
    file = open('todo_list.json', 'r')
    data = json.load(file)
    file.close()
    for i in range(len(data)):
        if int(data[i]['item_id']) == int(item_id):
            data.pop(i)
            file = open('todo_list.json', 'w')
            json.dump(data, file)
            file.close()
            return 0
    return 1
