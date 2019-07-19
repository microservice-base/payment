from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    json = ['test1', 'test2', 'test3']
    return jsonify(json)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8004)
