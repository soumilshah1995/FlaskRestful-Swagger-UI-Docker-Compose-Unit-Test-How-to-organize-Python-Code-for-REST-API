from dotenv import load_dotenv
load_dotenv()

try:
    from API import (app,
                     api,
                     HeathController,docs,

                     )
except Exception as e:
    print("Modules are Missing : {} ".format(e))

api.add_resource(HeathController, '/health_check')
docs.register(HeathController)

