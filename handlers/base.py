import logging
import tornado.web

logger = logging.getLogger(__name__)


class BaseHandler(tornado.web.RequestHandler):

    @property
    def mongo_test(self):
        return self.application.mongo_test

    def get_user_locale(self):
    	cuser = self.current_user or {}
    	user_locale = cuser.get('locale', 'zh_ZH')
        return tornado.locale.get(user_locale)

    def get_current_user(self):
        username = self.get_secure_cookie('username')
        result = self.mongo_test.tornado.find_one({'username': username})
    	return result

    def prepare(self):
        if self.request.headers.get(
                "Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None
