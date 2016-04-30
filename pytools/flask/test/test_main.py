import unittest
from pytools import flask


class FlaskTestCase(unittest.TestCase):

    def test_create_app(self):
        app = flask.CustomFlask(__name__)
        self.assertIsNotNone(app)
