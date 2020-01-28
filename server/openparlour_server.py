from flask import Flask

app = Flask(__name__)

@app.route('/openparlour/post/get/<int:post_number>')
def get_post(post_number):
    pass

@app.route('/openparlour/post/', methods=['POST'])
def post():
    pass
