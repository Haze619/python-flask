from flask import Flask
from flask import redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'rvce.edu.in'


@app.route('/rv')
def rvce():
    return 'RVCE ROCKS'


@app.route('/hello')
def hello():
    return redirect("https://www.rvitm.edu.in", code=302)


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


@app.route('/rev/<float:revno>')
def revision(revno):
    return 'Revision number %f' % revno


if __name__ == '__main__':
    app.run(debug=True)
