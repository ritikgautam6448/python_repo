from flask import request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

    @app.route('ARMSTRONG/<int:num>')
    def armstrong(num):
        sum = 0
        order = len(str(num))
        copy_num = num
        while copy_num > 0:
            digit = copy_num % 10
            sum += digit ** order
            num //= 10


            if sum == copy_num:
                print(f"{num} is an armstrong number")
                result = {
                    "number": copy_num 
                    "Armstrong": True,
                    "message":"this is an Armstrong number"
                    "server IP": "122.234.456.789"

                }
                else:
                    print(f"{copy_num} is an Armstrong number")
                    result = {
                        number: copy_num, 
                        "Armstrong": False,  
                        "message": "this is not an Armstrong number",
                        "server IP": "122.234.456.789"
                    }
                return jsonify(jsonify(result  ))



    if __name__ == "__main__":
        app.run(debug=True)