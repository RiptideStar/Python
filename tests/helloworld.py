# import Flask objects
from flask import Flask, render_template, request

app = Flask(__name__)

# http://127.0.0.1:5000/kyle/?name=zhang&num=1234
@app.route('/kyle/')
def hello_kyle():
    params = request.args
    return f'Hello, kyle! Your parameters are : {params}'

# http://127.0.0.1:5000/kai/?name=zhang&num=1234
@app.route('/kai/')
def hello_kai():
    params = request.args
    return f'Hello, kai! Your last name is : {params.get("name")}'

if __name__ == '__main__':
    app.run(debug=True)