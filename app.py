from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/sl4237')
def about():
    return render_template('sl4237.html')

if __name__ == '__main__':
    app.run()
