from flask import Flask, render_template
app = Flask(__name__)
app.config['SERVER_NAME'] = 'Blackbottle.net'
app.config.from_pyfile('config.cfg')
@app.route("/")
def index():
    return render_template('home.html')

if __name__ == '__main__' :
    app.run(host='0.0.0.0', debug=True)