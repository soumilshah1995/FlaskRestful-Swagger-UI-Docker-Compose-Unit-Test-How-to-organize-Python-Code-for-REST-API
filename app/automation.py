try:
    import os
    import json
    import abc
    import string
    from enum import Enum
except Exception as e:
    print("Error some module are missing :{} ".format(e))


class Parameters(object):

    def __init__(self):

        self.data = {

            "ApiName":"DownloadJobsProcess",
            "tag":"Jobs Download",
            "ApiDescription":"Download jobs based on process id",
            "DataBaseRequired":True,
            "field":[
                {
                    "name":"process_id",
                    "type":"String",
                    "required":True,
                    "description":"Based on process ID it will download job "
                },
            ],

        }

class CRUDEnum(Enum):
    GET_REQUEST = 1
    POST_REQUEST = 2
    DELETE_REQUEST = 3

class CodeGenerator(object):

    def __init__(self, instance):
        self.instance = instance
        self.code = """"""

    def run(self):

        """Main Controller  class"""

        self.step1_generate_imports()
        self.step2_generate_schemas()
        self.step3_generate_controller()
        self.step4_save_package()

    def step1_generate_imports(self):
        if self.instance.data.get("DataBaseRequired"):
            self.code += """
try:
    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse
    import json
    import os
    from marshmallow import Schema, fields
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs
    from API.common.dbclass  import Database
    print("All Modules are loaded ...")
except Exception as e:
    print("some modules are Missing ")
            """
        else:
            self.code += """
try:
    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse
    import json
    import os
    from marshmallow import Schema, fields
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs
    print("All Modules are loaded ...")
except Exception as e:
    print("some modules are Missing ")
            """

    def step2_generate_schemas(self):

        controller_name = self.instance.data.get("ApiName")
        controller_schema_name = ""

        for x in CRUDEnum:
            if x.value == 2:
                controller_schema_name = controller_name+"Put"+"Schema"
                if self.instance.data.get("field") is not None:
                    if len(self.instance.data.get("field")):
                        class_name = """
class {}(Schema):
            """.format(controller_schema_name)
                        self.code += class_name

                        for feild in self.instance.data.get("field"):
                            if feild.get("type") == "String":
                                _ = """
    {} = fields.String(required={}, description= "{}" )""".format(feild.get("name"),
                                                                  feild.get("required"),
                                                                  feild.get("description"),
                                                                  )
                                self.code += _
                        self.code += "\n"

            if x.value == 3:
                controller_schema_name = controller_name+"Delete"+"Schema"
                if self.instance.data.get("field") is not None:
                    if len(self.instance.data.get("field")):
                        class_name = """
class {}(Schema):
            """.format(controller_schema_name)
                        self.code += class_name

                        for feild in self.instance.data.get("field"):
                            if feild.get("type") == "String":
                                _ = """
    {} = fields.String(required={}, description= "{}" )""".format(feild.get("name"),
                                                                  feild.get("required"),
                                                                  feild.get("description"),
                                                                  )
                                self.code += _

                        self.code += "\n"

    def step3_generate_controller(self):

        self.code += """
class {}Controller(MethodResource, Resource):
        """.format(self.instance.data.get("ApiName"))

        controller_schema_name = ""

        for x in CRUDEnum:

            if x.value == 1:

                self.code += """ 
    @doc(description='Add Documentation ', tags=[ "{}" ] )""".format(self.instance.data.get("tag"))

                if self.instance.data.get("DataBaseRequired"):
                    function_name = """      
    def get(self, **kwargs):
        try:
            'Developer writes the code here '
            
            JSON = kwargs
            helper = Database()
            
            query = "QUERY GOES HERE"
            response = helper.get(query=query)
            
            data = {"data":response}
            return data
            
        except Exception as e:
            print(e)
            return {
                "status":-1,
                "error":{
                            "message":str(e)
                        }
            }
\n"""

                else:
                    function_name = """      
    def get(self, **kwargs):
        try:
            'Developer writes the code here '
            pass
        except Exception as e:
            print(e)
            return {
                "status":-1,
                "error":{
                            "message":str(e)
                        }
            }
        \n"""

            if x.value == 2:

                self.code += """ 
    @doc(description='Add Documentation ', tags=[ "{}" ] )""".format(self.instance.data.get("tag"))

                if self.instance.data.get("field") is not None:
                    if len(self.instance.data.get("field")):
                        self.code += """
    @use_kwargs({}, location=('json'))
                        """.format(self.instance.data.get("ApiName")+"Put"+"Schema")

                if self.instance.data.get("DataBaseRequired"):
                    function_name = """            

    def post (self, **kwargs):
        try:
            'Developer writes the code here '
                        
            JSON = kwargs
            helper = Database()
            
            query = "QUERY GOES HERE"
            response = helper.get(query=query)
            
            data = {"data":response}
            return data
            
        except Exception as e:
            print(e)
            return {
                "status":-1,
                "error":{
                    "message":str(e)
            }
            }
            """

                else:
                    function_name = """    
                            
    def post (self, **kwargs):
        try:
            'Developer writes the code here '
            pass
        except Exception as e:
            print(e)
            return {
                "status":-1,
                "error":{
                    "message":str(e)
            }
            }
            """

            if x.value == 3:

                self.code += """ 
    @doc(description='Add Documentation ', tags=[ "{}" ] )""".format(self.instance.data.get("tag"))
                if self.instance.data.get("field") is not None:
                    if len(self.instance.data.get("field")):
                        self.code += """
    @use_kwargs({}, location=('json'))
                        """.format(self.instance.data.get("ApiName")+"Delete"+"Schema")

                if self.instance.data.get("DataBaseRequired"):
                    function_name = """

    def delete (self, **kwargs):
        try:
            'Developer writes the code here '

            JSON = kwargs
            helper = Database()
            
            query = "QUERY GOES HERE"
            response = helper.get(query=query)
            
            data = {"data":response}
            return data
            
        except Exception as e:
            print(e)
            return {
                "status":-1,
                "error":{
                    "message":str(e)
            }
            }
            """
                else:
                    function_name = """
    def delete (self, **kwargs):
        try:
            'Developer writes the code here '
            pass
        except Exception as e:
            print(e)
            return {
                "status":-1,
                "error":{
                    "message":str(e)
            }
            }
            """

            self.code += function_name

    def step4_save_package(self):
        try:
            viewName = """{}Views""".format(self.instance.data.get("ApiName"))

            os.mkdir(
                os.path.join(
                    os.getcwd(),
                    "API/{}".format(viewName)
                )
            )
            path = os.path.join(os.getcwd(),"API/{}/views.py".format(viewName))
            with open(path, "w") as f:
                f.write(self.code)

        except Exception as e:
            print("Directory exists ")


def main():
    helper = Parameters()
    code_instance  = CodeGenerator(instance=helper)
    code_instance.run()


if __name__ == "__main__":
    main()