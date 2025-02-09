from os import environ

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


if __name__ == '__main__':
    PORT = environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=PORT)
