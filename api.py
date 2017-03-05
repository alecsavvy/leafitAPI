#!leafitAPI/bin/
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python Tutorial',
        'done': False
    }
]


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


# @app.route('/', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': map(make_public_task, tasks)})


@app.route('/', methods=['POST'])
def create_task():
    if not request.json not in 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] +1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task:task'}), 201


@app.route('/<int:task_id>', methods=["GET"])
def get_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)

