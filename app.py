import os

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
from tornado_sqlalchemy import make_session_factory, SessionMixin

from settings import settings
from urls import url_patterns

class TornadoWebApp(tornado.web.Application):
    def __init__(self):
        database_url = os.environ['DATABASE_URL']
        tornado.web.Application.__init__(
            self, url_patterns, session_factory=make_session_factory(database_url), **settings)

def build_app():
    return TornadoWebApp()

def main():
    app = build_app()
    http_server = tornado.httpserver.HTTPServer(app)
    print("Port running in", options.port)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
