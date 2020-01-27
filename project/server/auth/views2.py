# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from flask import Flask, render_template_string
from project.server import bcrypt, db
from project.server.models import User

auth_blueprint2 = Blueprint('list', __name__)


class ReturnAPI(MethodView):
    """
    User Registration Resource
    """

    # def get(self):
    # 	responseObject = {
    # 		'status': 'success',
    # 		'message': 'Heres a list of users.'
    # 	}
    #     user= Users.query.order_by(User.email).all()
    # 	return make_response(jsonify(responseObject)), 201
    def get(self):
        user= User.query.all()
        responseObject={
            'status': 'success',
            'message': 'LIST SENT'
        }
        return str(user)
    # def post(self):
    #     # get the post data
    #     post_data = request.get_json(); print(request)
    #     # check if user already exists
    #     user = User.query.filter_by(email=post_data.get('email')).first()
    #     if not user:
    #         try:
    #             user = User(
    #                 email=post_data.get('email'),
    #                 password=post_data.get('password')
    #             )

    #             # insert the user
    #             db.session.add(user)
    #             db.session.commit()
    #             # generate the auth token
    #             auth_token = user.encode_auth_token(user.id)
    #             responseObject = {
    #                 'status': 'success',
    #                 'message': 'Successfully registered.',
    #                 'auth_token': auth_token.decode()
    #             }
    #             return make_response(jsonify(responseObject)), 201
    #         except Exception as e:
    #             responseObject = {
    #                 'status': 'fail',
    #                 'message': 'Some error occurred. Please try again.'
    #             }
    #             return make_response(jsonify(responseObject)), 401
    #     else:
    #         responseObject = {
    #             'status': 'fail',
    #             'message': 'User already exists. Please Log in.',
    #         }
    #         return make_response(jsonify(responseObject)), 202


# define the API resources
return_view = ReturnAPI.as_view('return_api')

# add Rules for API Endpoints
auth_blueprint2.add_url_rule(
    '/users/index',
    view_func=return_view,
    methods=['GET']
)
