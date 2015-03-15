import logging
import os.path
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from pymongo import MongoClient
from tornado.options import define, options

from route import routers
from settings import settings

logger = logging.getLogger(__name__)


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, routers, **settings)
        self.mongo_test = MongoClient(options.mongo_host)[options.mongo_test]
        self.settings = settings


def main():
    tornado.options.parse_command_line()
    tornado.locale.load_translations(options.translation_path)
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
