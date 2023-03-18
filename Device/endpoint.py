from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from Device.devicemodel import DeviceModel

class AddDevice(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'device_name',
        type=str,
        required=True
        )


    def post(self):
        data = AddDevice.parser.parse_args()
        name = data["device_name"]

        if DeviceModel.find_by_name(name):
            return {'message': f"A device with name '{name}' already exists."}, 400

        new_device = DeviceModel(
            device_name=name,
            user_id=id(current_identity)
        )
        new_device.save_to_db()

        return  {"api_key": new_device.device_key}, 201

    def get(self):
        devices = DeviceModel.query.all()
        result = []
        for d in devices:
            result.append(d.json())
        return result, 201

class At(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'device_key',
        type=str,
        required=True
        )
        
    def get(self):
        data = At.parser.parse_args()
        if DeviceModel.find_by_device_key(data['device_key']):
            import browser
            return {'message': "Launch bot"}, 201
        else:
            return {'message': "nada"}, 201