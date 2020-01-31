from flask import request
from flask import app
from flask import Flask
from pprint import pprint

app = Flask(__name__)

@app.route('/openparlour/post/get/<int:post_number>')
def get_post(post_number):
    pass

@app.route('/openparlour/post', methods=['POST'])
def post():
    if request.is_json:
        req_json = request.get_json
        pprint(req_json)



