from flask import Flask, request
from fibonacci import fibonacci_of
import time

app = Flask(__name__)

@app.route("/echo")
def echo():
    return request.args.get('text', '')

@app.route("/cpu_bound")
def cpu_bound():
    n = int(request.args.get('n', 0))
    
    t_start = time.time()
    ###
    f = fibonacci_of(30)
    ###
    t_end = time.time()

    t_diff = t_end - t_start
    print(t_diff)

    return str(f)
    

if __name__ == '__main__':
    app.run()