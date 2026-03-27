from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to the Flask Calculator! Use /calculate?num1=10&num2=5&op=add"

@app.route('/calculate')
def calculate():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        op = request.args.get('op')

        if op == 'add':
            result = num1 + num2
        elif op == 'sub':
            result = num1 - num2
        elif op == 'mul':
            result = num1 * num2
        elif op == 'div':
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 / num2
        else:
            return "Invalid operation. Use add, sub, mul, or div."

        return f"Result: {result}"

    except (TypeError, ValueError):
        return "Invalid input. Please provide num1, num2, and op."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)