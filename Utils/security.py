from User.usermodel import UserModel
from hmac import compare_digest
import functools
from Device.devicemodel import DeviceModel
from flask import request

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

def is_valid(api_key):
    device = DeviceModel.find_by_device_key(api_key)
    if device and compare_digest(device.device_key, api_key):
        return True


def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if request.json:
            api_key = request.json.get("api_key")
        else:
            return {"message": "Please provide an API key"}, 400
        # Check if API key is correct and valid
        if request.method == "GET" and is_valid(api_key):
            return func(*args, **kwargs)
        else:
            return {"message": "The provided API key is not valid"}, 403
    return decorator

"""
import functools
from hmac import compare_digest
from flask import request
from devicemodel import DeviceModel

def authenticate(name, id):
    device = DeviceModel.find_by_name(name)
    if device and compare_digest(device.user_id, id):
        return device

def identity(payload):
    device_key = payload['identity']
    return DeviceModel.find_by_device_key(device_key)

def is_valid(api_key):
    device = DeviceModel.find_by_device_key(api_key)
    if device and compare_digest(device.device_key, api_key):
        return True

def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        #if request.json:
        #    api_key = request.json.get("api_key")
        #else:
        #    return {"message": "Please provide a valid API key"}, 400

        #check if the key is correct and valid
        if request.method == "POST":# and is_valid(api_key):
            return func(*args, **kwargs)
        else:
            return{"message": "The provided API key is not valid"}, 403
    return decorator


#elif request.method == "POST":
#            return func(*args, **kwargs)

#if valid, vais ao site da at com o bot e retorna o html da pagina da at
"""