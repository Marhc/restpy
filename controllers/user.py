from flask import abort, jsonify
from flask_sqlalchemy_session import current_session
from models.user import User


class Controller(object):
    @staticmethod
    def list():
        query = current_session.query(User).all()
        all_users = [user.to_dict() for user in query]
        return jsonify(all_users)

    @staticmethod
    def create(data):
        new_user = User(
            name=data["name"],
            email=data["email"]
        )
        current_session.add(new_user)
        current_session.commit()
        return jsonify(**new_user.to_dict())

    @staticmethod
    def read(id):
        user = current_session.query(User).get(id)
        if user is None:
            abort(404)
        return jsonify(**user.to_dict())

    @staticmethod
    def update(id, data):
        user = current_session.query(User).get(id)
        if user is None:
            abort(404)
        for key in data.keys():
            setattr(user, key, data[key])
        current_session.commit()
        return jsonify(**user.to_dict())

    @staticmethod
    def delete(id):
        user = current_session.query(User).get(id)
        if user is None:
            abort(404)
        current_session.delete(user)
        current_session.commit()
        return jsonify({'message': 'deleted user ' + str(id)})
