from flask import Flask, make_response, redirect, render_template, url_for, request, flash
from flask_script import Manager, Command, Shell
from forms import ContactForm

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


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    if username == 'root' and password == 'pass':
        message = "Correct username and password"
    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)


@app.route('/contact/', methods=['get', 'post'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
        print("\nData received. Now redirecting ...")
        flash("Message Received", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)


@app.route('/')
def http_404_handler():
    return make_response("<h2>404 Error</h2>", 400)


@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue", 60 * 60 * 24 * 15)
    res.set_cookie("favorite-font", "sans-serif", 60 * 60 * 24 * 15)
    return res


@app.route('/')
def http_500_handler():
    return "<h2>500 Error</h2>", 500


@app.route('/')
def render_markdown():
    return "## Heading", 200, {'Content-Type': 'text/markdown'}


app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'

manager = Manager(app)

if __name__ == "__main__":
    app.run()
