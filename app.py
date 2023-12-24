from flask import Flask, jsonify, request
import todo_list_operations as tl

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/todo', methods=['GET'])
def todo_list():
    todo_list_element = tl.get_todo_list()
    return jsonify({'data': todo_list_element, 'status': 200})


@app.route('/todo/<int:item_id>', methods=['GET'])
def todo_item(item_id):
    todo_list_item = tl.get_todo_item(item_id)
    if todo_list_item is None:
        return jsonify({'status': 404, 'message': 'Item Not Found'})
    return jsonify({'data': todo_list_item, 'status': 200})


@app.route('/todo/', methods=['POST'])
def add_todo_item():
    data = request.get_json()
    if not bool(data) is False:
        tl.insert_todo_item(data)
        return jsonify({'data': tl.get_todo_list(), 'status': 200})
    else:
        return jsonify({'data': tl.get_todo_list(), 'status': 200})


if __name__ == '__main__':
    app.run()
