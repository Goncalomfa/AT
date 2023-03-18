import uuid
from alchemy import alchemy
from User.usermodel import UserModel

class DeviceModel(alchemy.Model):
    __tablename__ = 'devices'

    id = alchemy.Column(alchemy.Integer, primary_key=True)
    device_name = alchemy.Column(alchemy.String(80))
    device_key = alchemy.Column(alchemy.String(80))
    user_id = alchemy.Column(alchemy.Integer, alchemy.ForeignKey('users.id'))
    user = alchemy.relationship('UserModel', back_populates="devices")

    def __init__(self, device_name, user_id, device_key=None):
        self.device_name = device_name
        self.user_id = user_id
        self.device_key = device_key or uuid.uuid4().hex

    def json(self):
        return {
            'device_name': self.device_name, 
            'device_key': self.device_key, 
            'user_id': self.user_id
        }

    @classmethod
    def find_by_name(cls, device_name):
        return cls.query.filter_by(device_name=device_name).first()

    @classmethod
    def find_by_device_key(cls, device_key):
        return cls.query.filter_by(device_key=device_key).first()

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()

"""
class Users(Resource):
    def get(self):
        data = pd.read_csv('dataset.csv')  # read local CSV
        data = data.to_dict()  # convert dataframe to dict
        return {'data': data}, 200  # return data and 200 OK

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('other1', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('dataset.csv')

        if args['id'] in list(data['id']):
            return {
                'message': f"'{args['id']}' already exists."
            }, 409
        else:
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'id': [args['id']],
                'name': [args['name']],
                'other1': [args['other1']],
                'other2': [[]]
            })
            # add the newly provided values
            data = pd.concat([data, new_data], ignore_index=True)
            data.to_csv('dataset.csv', index=False)  # save back to CSV
            return {'data': data.to_dict()}, 200  # return data with 200 OK

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add args
        parser.add_argument('other2', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('dataset.csv')
        
        if args['id'] in list(data['id']):
            # evaluate strings of lists to lists !!! never put something like this in prod
            data['other2'] = data['other2'].apply(
                lambda x: ast.literal_eval(x)
            )
            # select our user
            user_data = data[data['id'] == args['id']]

            # update user's locations
            user_data['other2'] = pd.concat([user_data['other2'].values[0], args['other2']])
            
            # save back to CSV
            data.to_csv('dataset.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the userId does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404

    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add userId arg
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('users.csv')
        
        if args['id'] in list(data['id']):
            # remove data entry matching given userId
            data = data[data['id'] != args['id']]
            
            # save back to CSV
            data.to_csv('dataset.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        else:
            # otherwise we return 404 because userId does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404


api.add_resource(Users, '/users')  # add endpoints

if __name__ == '__main__':
    app.run()
"""
