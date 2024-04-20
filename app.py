from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return redirect('/sayHello', code=302)

@app.route('/sayHello', methods=['GET'])
def say_hello():
    return jsonify("Hello User.")

if __name__ == '__main__':
    app.run(port=80)