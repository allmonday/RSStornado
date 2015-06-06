import logging
import tornado
import tornado.web

from utils import _hash
from handlers.base import BaseHandler

logger = logging.getLogger(__name__)


class RegisterHandler(BaseHandler):

    def get(self):
        self.render('register.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        locale = self.get_argument('locale')
        password = _hash(password)

        is_exist = self.mongo_test.tornado.find({'username': username}).count()
        logger.debug(is_exist)

        # if exist
        if is_exist:
            logger.info('{} have been registered'.format(username))
            self.render('login.html',
                        message='you have already register\
                         an account, please log in')

        else:
            self.mongo_test.tornado.insert({
                'username': username,
                'password': password,
                'locale': locale
            })
            logger.info('new user registered, {}'.format(username))
            self.render('login.html', message='please login')


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html', message='welcome')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        password = _hash(password)
        result = self.mongo_test.tornado.find_one({
            'username': username,
            'password': password
        })
        if result:
            self.set_secure_cookie('username',
                                   self.get_argument('username'),
                                   expires_days=None)
            self.redirect('/')
        else:
            self.render('login.html',
                        message='password error, please try again.')


class WelcomeHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.render('index.html', user=self.current_user)


class LogoutHandler(BaseHandler):

    def get(self):
        if (self.get_argument("logout", None)):
            self.clear_cookie('username')
            self.redirect('/')
