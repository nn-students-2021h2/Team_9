from flask import Flask, request
from fibonacci import fibonacci_of

app = Flask(__name__)

@app.route("/echo")
def echo():
    return request.args.get('text', '')

@app.route("/cpu_bound")
def cpu_bound():
    n = int(request.args.get('n', 0))
    return str(fibonacci_of(n))
    

if __name__ == '__main__':
    app.run()