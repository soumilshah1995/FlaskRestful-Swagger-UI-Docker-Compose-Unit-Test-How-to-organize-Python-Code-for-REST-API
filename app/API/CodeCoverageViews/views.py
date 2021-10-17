try:
    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse
    import json
    import os
    from marshmallow import Schema, fields
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs
    import os
    from enum import Enum
    print("All Modules are loaded ...")
except Exception as e:
    print("some modules are Missing ")


class CodeCoverageController(MethodResource, Resource):
    @doc(description='Add Documentation ', tags=[ "Code Coverage" ] )      
    def get(self, **kwargs):
        try:
            import subprocess
            p = subprocess.run(["coverage", "json"], capture_output=True, text=True)
            with open("coverage.json", "r") as f:data = json.loads(f.read())
            _data = data
            return _data
        except Exception as e:
            print(e)
            return {
                "status":-1,
                "error":{
                            "message":str(e)
                        }
            }
        
