from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_json():
                                           
    response = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(response)

if __name__ == '__main__':
                                                  
    app.run(debug=True)
