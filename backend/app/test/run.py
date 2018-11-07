from flask import Flask, render_template, jsonify, make_response
from functools import wraps

from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources=r'/*')

# def allow_cross_domain(fun):
#     @wraps(fun)
#     def wrapper_fun(*args, **kwargs):
#         rst = make_response(fun(*args, **kwargs))
#         rst.headers['Access-Control-Allow-Origin'] = '*'
#         rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
#         allow_headers = "Referer,Accept,Origin,User-Agent"
#         rst.headers['Access-Control-Allow-Headers'] = allow_headers
#         return rst
#     return wrapper_fun

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
 
 
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/test')
# @allow_cross_domain
def api_test():
    return jsonify({'tasks': tasks})

@app.route('/api/test/<params>')
# @allow_cross_domain
def params_test(params):
    return jsonify({'params': params})
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050, threaded=True)
