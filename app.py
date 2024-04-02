from flask import Flask, request, jsonify
app = Flask(__name__)  # create Flask app!!


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello App!'


@app.route('/post_example', methods=['POST'])
def post_example():
    """ Is person passed oldest person in DB? """
    data = request.json  # Assuming JSON data is sent in the request body

    # Mock DB
    db = {"Peter": 25,
          "Paul": 26,
          "Mary": 27
          }

    # Get data from POST
    name = data.get('name')
    age = int(data.get('age'))

    # Check if POST age is max (oldest)
    m = max(db.values())
    if age > m:
        response = {'message': 'New user is oldest', 'name': name, 'age': age}
    else:
        response = {'message': 'New user is NOT oldest', 'name': name, 'age': age}

    return jsonify(response)


if __name__ == '__main__':
    app.run()
