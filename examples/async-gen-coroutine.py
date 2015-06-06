# coding: utf-8
import urllib
import tornado.web
import tornado.ioloop
import tornado.httpclient
from tornado import gen


class MainHandler(tornado.web.RequestHandler):
    """
    通过异步调用后端服务器的数据, 防止阻塞
    """

    @gen.coroutine
    def get(self):
        data = yield self.das_get()
        print data.body
        self.write(data.body)

    @gen.coroutine
    def post(self):
        data = yield self.das_post(self.request.headers, self.request.body)
        self.write(data.body)

    def das_get(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        return http_client.fetch("http://0.0.0.0:8888/api/blog")

    def das_post(self, headers, body):
        http_client = tornado.httpclient.AsyncHTTPClient()
        return http_client.fetch("http://0.0.0.0:8888/api/blog", method="POST", headers=headers, body=body)


application = tornado.web.Application([
    (r"/", MainHandler),
], debug=True)

if __name__ == "__main__":

    application.listen(8889)    
    tornado.ioloop.IOLoop.instance().start()
