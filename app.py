"""
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from devicemodel import DeviceModel
from security import authenticate, identity

from endpoint import AddDevice
from alchemy import alchemy
from testpop import db_load_example_data

app = Flask(__name__)
#app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#avoid complains
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
alchemy.init_app(app)
api = Api(app)

@app.before_first_request
def create_tables():
    alchemy.create_all()
    db_load_example_data(app,alchemy)

#jwt = JWT(app, authenticate, identity)

api.add_resource(AddDevice, '/device/add-device')

"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from alchemy import alchemy

from Device.endpoint import AddDevice, At
from Utils.security import authenticate, identity
from User.user_resource import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite' #mudar nome
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
alchemy.init_app(app)
app.secret_key = 'api_key'
api = Api(app)


@app.before_first_request
def create_tables():
    alchemy.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserRegister, '/register')
api.add_resource(AddDevice, '/device')
api.add_resource(At, '/at')

if __name__ == '__main__':
    app.run(debug=True)
