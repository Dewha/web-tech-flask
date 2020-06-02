from flask import Flask, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Jerry')

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/')
def http_404_handler():
    return make_response("<h2>404 Error</h2>", 400)


@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue", 60*60*24*15)
    res.set_cookie("favorite-font", "sans-serif", 60*60*24*15)
    return res

@app.route('/')
def http_500_handler():
    return "<h2>500 Error</h2>", 500

@app.route('/')
def render_markdown():
    return "## Heading", 200, {'Content-Type': 'text/markdown'}

@app.route('/transfer')
def transfer():
    return redirect("https://localhost:5000/login", code=301)

if __name__ == "__main__":
    app.run()