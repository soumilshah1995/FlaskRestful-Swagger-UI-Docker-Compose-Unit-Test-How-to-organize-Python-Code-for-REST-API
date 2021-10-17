try:
    import os
    import unittest
    import app
    import json
    from API import app
    from dotenv import load_dotenv
    import os
    import subprocess

    print("test file ok...........")
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

    def test_health_response(self):
        """
        Check Whether Response is 200

        """
        tester = app.test_client(self)
        response = tester.get("/health_check")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data.get("message"), "APi are working fine")

    def test_code_coverage(self):

        """
        Check Whether Response is 200

        """
        print("\n")
        print("\n")
        import subprocess
        subprocess.run(["coverage", "report"])
        print("\n")
        print("\n")


if __name__ == "__main__":
    unittest.main()
