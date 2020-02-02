from flask import request
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/openparlour/post/get/<int:post_number>')
def get_post(post_number):
    return jsonify("{}")

@app.route('/openparlour/post', methods=['POST'])
def post():
    req_json = request.get_json
    db = init_db_if_needed()
    return jsonify(db.insert(req_json))

if __name__ == "__main__":
    app.run()
