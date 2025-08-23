from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/GREET/<name>')
def greet(name):
    print("Greet request for %s\n", name)
    result = {
         "name": name,
        "greeting": f"Hello, {name}",
        "alternative_greeting": f"Hi, {name}",
        "contact": "abcxyz",
        "email": "ritik@6448gmail.com",
        "phone number": "1234567890",
        "address": "abc street, bangalore -560037",
        "type": "1",
        "street": "xyz street",
        "city": "bangalore",
        "country": "india",
        "landmark": "near xyz mall",
        "state": "Karnataka",
        "pincode": "560037",
        "type" : "2",
        "street": "abc street",
        "city" : "mumbai",
        "country" : "india",
        "landmark" : "near mall of asia",
        "state" : "maharastra",
        "pincode" : "400001",
        "server IP": "122.234.456.789"
    }
    return jsonify(result)

@app.route('/ARMSTRONG/<int:num>')
def armstrong(num):
    print("Checking if %d is an Armstrong number\n", num)
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