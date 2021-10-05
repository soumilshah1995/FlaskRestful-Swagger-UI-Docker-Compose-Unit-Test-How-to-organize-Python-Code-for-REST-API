try:
    import os
    import unittest
    import app
    import json
    import requests
    from API import app
    import os

except Exception as e:
    print(e)

class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # code that is executed before all tests in one test run
        pass

    @classmethod
    def tearDownClass(cls):
        # code that is executed after all tests in one test run
        pass

    def setUp(self):
        # creates a test client
        # code that is executed before each test
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        # code that is executed after each test
        pass

    def test_health_endpoint(self):
        """
        Check Whether Response is 200

        """
        tester = app.test_client(self)
        response = tester.get("/health_check")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)