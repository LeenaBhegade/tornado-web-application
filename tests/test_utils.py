import urllib.parse
import os

from tornado.testing import AsyncHTTPTestCase
from tornado_sqlalchemy import declarative_base, make_session_factory

from app import build_app

sqlite_url = os.environ['DATABASE_URL']

Base = declarative_base()

class UtilsTestCase(AsyncHTTPTestCase):
    def __init__(self, *args, **kwargs):
            super(RequestHandlersTestCase, self).__init__(*args, **kwargs)
            self._factory = make_session_factory(sqlite_url)
            self._application = build_app()

    def setUp(self, *args, **kwargs):
        super(RequestHandlersTestCase, self).setUp(*args, **kwargs)
        Base.metadata.create_all(self._factory.engine)

    def tearDown(self, *args, **kwargs):    
        Base.metadata.drop_all(self._factory.engine)
        super(RequestHandlersTestCase, self).tearDown(*args, **kwargs)

    def get_app(self):
        return self._application

    def test_get_key_encrypt_data(self):

    def test_get_key_encrypt_data(self):

        
        