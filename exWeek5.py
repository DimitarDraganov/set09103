from flask import Flask, request, url_for
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/hallo/")
def hallo():
    name = request.args.get('name', '')

    if name == '':
        return "no param supplied"
    else:
        return "Hallo %s" % name


@app.route("/hello/<name>")
def hello(name):
    return "Hello %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first+second)

@app.route("/account/", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        print request.form
        name = request.form['name']
        return "Hello %s" % name
    else:
        page ='''
        <html><body >
            <form action="" method="post" name="form">
                <label for="name">Name:</label >
                <input type="text" name="name" id="name"/>
                <input type="submit" name="submit" id="submit"/>
            </form >
            </body><html'''

        return page


@app.route("/display/")
def display():
    return '<img src="' + url_for('static', filename='uploads/upload.jpg')+'"/>'


@app.route("/uploaded/", methods=['POST', 'GET'])
def uploaded():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/upload.jpg')
        return "File Uploaded"

    else:
        page='''
         <html>
         <body>
         <form action="" method="post" name="form" enctype="multipart/form-data">
         <input type="file" name="datafile" />
         <input type="submit" name="submit" id="submit"/>
         </form>
         </body>
         </html> 
        '''
        return page, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
