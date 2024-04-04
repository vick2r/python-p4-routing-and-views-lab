#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html = '<h1>Python Operations with Flask Routing and Views</h1>'
    return html

@app.route('/print/<string:msg>')
def print_string(msg):
    print(msg)
    return msg

@app.route('/count/<int:num>')
def count(num):
    return (f'{x}\n' for x in range(num))

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        res = (int(num1) + int(num2))
        return str(res)
    elif operation == '-':
        res = (int(num1) - int(num2))
        return str(res)
    elif operation == '*':
        res = (int(num1) * int(num2))
        return str(res)
    elif operation == 'div':
        res = (int(num1) / int(num2))
        return str(res)
    elif operation == '%':
        res = (int(num1) % int(num2))
        return str(res)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
