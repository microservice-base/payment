from flask import Flask
from flask_restplus import Api,Resource

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8004)