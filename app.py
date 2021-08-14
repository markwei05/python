"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return test homepage."""
    json_data = {'Hello': 'World Christine wei!'}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
