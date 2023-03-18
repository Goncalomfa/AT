from Device.devicemodel import DeviceModel

def db_load_example_data(app, db):
    admin = DeviceModel('admin', 'test')
    guest = DeviceModel('guest', 'test')
    with app.app_context():
        DeviceModel.save_to_db(admin)
        DeviceModel.save_to_db(guest)
