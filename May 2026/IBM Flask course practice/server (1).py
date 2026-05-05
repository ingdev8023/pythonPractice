from flask import Flask, render_template, request
# Import the Maths package here
from Maths.mathematics import summation, subtraction,multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    sum = summation(num1, num2)
    if sum.is_integer():
        sum = int(sum)
    return str(sum)
@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    sub = subtraction(num1, num2)
    if sub.is_integer():
        sub = int(sub)
    return str(sub)
@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here  
    mul = multiplication(num1, num2)
    if mul.is_integer():
        mul = int(mul)
    return str(mul)
@app.route("/")
def render_index_page():
    # Write your code here
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
