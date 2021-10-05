

try:
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs
    from pydantic import BaseModel
    print("All imports are ok............")
except Exception as e:
    print("Error: {} ".format(e))

class NameInfoDto(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    message:str

class  NameControllerSchema(Schema):
    name: str = fields.String(required=True, description="nameis requried ")

class NameController(MethodResource, Resource):

    @doc(description='This API takes names and will greet you', tags=['Name'])
    @use_kwargs(NameControllerSchema, location=('json'))
    def post(self, **kwargs):
        _message = kwargs.get("name", "default")
        response  = NameInfoDto(message = _message).dict
        return response
