from flask import request
from flask_restful import Resource

from controllers import user


class Index(Resource):
    def get(self):
        return user.Controller.list()


class Store(Resource):
    def post(self):
        data = request.get_json(force=True)
        return user.Controller.create(data)


class Show(Resource):
    def get(self, id):
        return user.Controller.read(id)


class Update(Resource):
    def put(self, id):
        data = request.get_json(force=True)
        return user.Controller.update(id, data)


class Destroy(Resource):
    def delete(self, id):
        return user.Controller.delete(id)
