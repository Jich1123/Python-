from flask import Flask , url_for, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!你好"

@app.route('/user/<username>')
def show_user_profile(username):
    return "user name is : %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post is : %s" % post_id

@app.route('/url')
def show_url():
    return url_for('static', filename="css/style.css")
    # return url_for("show_post", post_id=post_id)

@app.route('/login', methods=['POST','GET','PUT'])
def login():
    if request.method == "GET":
        return "This is GET funtion"
    elif request.method == "GET":
        pass
    else:
        pass

if __name__=="__main__":
    app.run(debug=True)