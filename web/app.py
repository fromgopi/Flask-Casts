from flask import request, Flask
import json 
from web.trees.trees import tree_mould

app = Flask(__name__)

 
@app.route('/')
def index():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route('/plus_one')  
def one_plus():
    x = int(request.args.get('x', 1))
    return json.dumps({
        'x': x + 1
    })
 
 
@app.route('/plus_two')
def plus_two():
    x = int(request.args.get('x', 1))
    return json.dumps({
        'x': x + 2
    })


@app.route('/square')
def square():
    x = int(request.args.get('x', 1))
    return json.dumps({
        'x': x * x
    })


app.register_blueprint(tree_mould, url_prefix='/oak')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
