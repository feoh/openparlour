from flask import Flask

app = Flask(__name__)

@app.route('/myplace/post/get/<int:post_number>')
def get_post(post_number):
    pass
