from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a = input()
    a = "<h1>{}<h1>".format(a)
    return a

if __name__ == '__main__':
    app.run(debug=True)