import os

from flask import (
    Flask,
    render_template,
    send_from_directory,
)


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', None)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/yes')
def yes():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon',
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
