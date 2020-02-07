from flask import request
from flask import Flask
from flask import jsonify
from db.data_access import initialize_orm, get_all_posts, get_all_rooms, create_post

app = Flask(__name__)

@app.route('/openparlour/post/get/<int:post_number>')
def get_post(post_number):
    return jsonify("{}")

@app.route('/openparlour/post', methods=['POST'])
def post():
    db = initialize_orm()
    req_json = request.get_json
    # Create a post and jsonify it.
if __name__ == "__main__":
    app.run()
