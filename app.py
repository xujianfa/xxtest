from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'name': '123'}


if __name__ == '__main__':
    app.run(debug=True)



