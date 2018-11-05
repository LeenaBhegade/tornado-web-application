import urllib.parse
import os

from tornado.testing import AsyncHTTPTestCase
from tornado_sqlalchemy import declarative_base, make_session_factory

from app import build_app

sqlite_url = os.environ['DATABASE_URL']

Base = declarative_base()

class RequestHandlersTestCase(AsyncHTTPTestCase):
    def __init__(self, *args, **kwargs):
            super(RequestHandlersTestCase, self).__init__(*args, **kwargs)
            self._factory = make_session_factory(sqlite_url)
            self._application = build_app()

    def setUp(self, *args, **kwargs):
        print("in setup")
        super(RequestHandlersTestCase, self).setUp(*args, **kwargs)
        Base.metadata.create_all(self._factory.engine)

    def tearDown(self, *args, **kwargs):    
        Base.metadata.drop_all(self._factory.engine)
        super(RequestHandlersTestCase, self).tearDown(*args, **kwargs)

    def get_app(self):
        return self._application

    def test_home_page_get(self):
        response = self.fetch('/', method='GET')
        self.assertEqual(response.code, 200)

    def test_home_page_post(self):
        post_body = urllib.parse.urlencode({"url":"https://www.bbc.co.uk/news/technology-35343091"})
        response = self.fetch('/', method='POST', body=post_body)
        self.assertEqual(response.code, 200)

    def test_admin_page_get(self):
        response = self.fetch('/', method='GET')
        self.assertEqual(response.code, 200)