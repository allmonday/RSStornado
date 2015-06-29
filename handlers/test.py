import logging
import tornado.web

from handlers.base import BaseHandler

logger = logging.getLogger(__name__)


class TestHandler(BaseHandler):

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
        print self.get_argument('filename')
        self.write("hi")
