from flask_restful import Api

from resources import user

api = Api(prefix="/api")

# Users Resources
api.add_resource(user.Index, '/users')
api.add_resource(user.Store, '/users')
api.add_resource(user.Show, '/users/<int:id>')
api.add_resource(user.Update, '/users/<int:id>')
api.add_resource(user.Destroy, '/users/<int:id>')
