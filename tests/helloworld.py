from flask import Flask
app = Flask(__name__)

@app.route('/kai/')
def hello_world():
    return 'Hello, World!'

@app.route('/kyle/')
def hello_world2():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)