from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('conditional.html', name=name)

@app.route('/users/')
def users():
    names = ['simon', 'Ivan', 'Gina', 'Mitko', 'Alex']
    return render_template('loops.html', names=names)


@app.route("/account/", methods=['POST','GET'])
def account():
    if request.method == 'POST':
        print request.form
        name = request.form['name']
        return "Hello %s" % name
    else:
        page ='''
        <html><body>
            <form action="" method="post" name="form">
            <label for="name">Name:</label>
            <input type="text" name="name" id="name"/>
            <input type="submit" name="submit" id="submit"/>
            </form>
            </body><html>'''

        return page

@app.route('/inherits/')
def inherits():
    return render_template('base.html')

@app.route('/inherits/one')
def inherits_one():
    return render_template('inherits1.html')

@app.route('/inherits/two')
def inherits_two():
    return render_template('inherits2.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


