try:
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs

    print("All imports are ok............")
except Exception as e:
    print("Error: {} ".format(e))


class HeathController(MethodResource, Resource):

    @doc(description='This is health Endpoint', tags=['Health Endpoint'])
    def get(self):

        '''
        Get method represents a GET API method
        '''
        return {'message': 'APi are working fine'}, 200