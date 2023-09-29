def calculate(first, operation, second):
    a = first
    b = second
    r = operation
    if r == "+":
        return a + b
    elif r == "-":
        return a - b
    elif r == "*":
        return a * b
    elif r == "/":
        return a / b
    elif r == "%":
        return a % b
    else:
        return "Error: Invalid operation"





#app.py
from flask import Flask, render_template, request,json 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
 
def calculate_route():
    try:
        first = int(request.form['first'])
        operation = request.form['operation']
        second = int(request.form['second'])

        result = calculate(first, operation, second)

        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', error=str(e))
         
        

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)



