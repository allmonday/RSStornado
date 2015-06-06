import logging
import tornado.web

logger = logging.getLogger(__name__)


class BlogHandler(tornado.web.RequestHandler):

    def get(self):
        logger.debug("get blog")
        data = [
            {'name': 'kikodo', 'title': 'welcome bagging', 'date': '2014'},
            {'name': 'kikodo', 'title': 'welcome bagging', 'date': '2014'},
            {'name': 'kikodo', 'title': 'welcome bagging', 'date': '2014'},
        ]
        self.write({
            "data": data
            })

    def post(self):
        print self.request.body
        self.write({
            "status": 0,
            "message": "ok"
            })
