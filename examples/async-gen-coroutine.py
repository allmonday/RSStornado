# coding: utf-8
import urllib
import requests
import tornado.web
import tornado.ioloop
import tornado.httpclient
from tornado import gen


class MainHandler(tornado.web.RequestHandler):
    """
    异步机制在loadrunner测试下, 10个并发, 2分钟: 57次响应每秒
    """
    # @gen.coroutine
    # def get(self):
    #     data = yield self.das_get()
    #     print data.body
    #     self.write(data.body)

    # @gen.coroutine
    # def post(self):
    #     data = yield self.das_post(self.request.headers, self.request.body)
    #     self.write(data.body)

    # def das_get(self):
    #     http_client = tornado.httpclient.AsyncHTTPClient()
    #     return http_client.fetch("http://0.0.0.0:8888/api/blog")

    # def das_post(self, headers, body):
    #     http_client = tornado.httpclient.AsyncHTTPClient()
    #     return http_client.fetch("http://0.0.0.0:8888/api/blog", method="POST", headers=headers, body=body)

    @gen.coroutine
    def get(self):
        data = yield self.das_get()
        self.write(data)

    @gen.coroutine
    def das_get(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        data = yield http_client.fetch("http://0.0.0.0:8888/api/blog")
        print data.body
        raise gen.Return(data.body)


class AHandler(tornado.web.RequestHandler):
    """
    同步机制在loadrunner测试下, 10个并发, 2分钟: 20次响应每秒
    """
    def get(self):
        data = self.das_get()
        print data
        self.write(data)

    def das_get(self):
        return requests.get('http://0.0.0.0:8888/api/blog').json()


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/a", AHandler),
], debug=True)

if __name__ == "__main__":

    application.listen(8889)    
    tornado.ioloop.IOLoop.instance().start()
