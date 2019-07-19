from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    json = ['test1','test2','test3']
    return jsonify(json)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8004)
