from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/ARMSTRONG/<int:num>')
def armstrong(num):
    sum = 0
    order = len(str(num))
    copy_num = num
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if sum == copy_num:
        print(f"{copy_num} is an armstrong number")
        result = {
            "number": copy_num,
            "Armstrong": True,
            "message": "this is an Armstrong number",
            "server IP": "122.234.456.789"
        }
    else:
        print(f"{copy_num} is not an armstrong number")
        result = {
            "number": copy_num,
            "Armstrong": False,
            "message": "this is not an Armstrong number",
            "server IP": "122.234.456.789"
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)