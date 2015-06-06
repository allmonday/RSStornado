import os
from tornado.options import define, options

BASE_PATH = os.path.dirname(__file__)
# these will be executed before return variable: settings
define('port', default=8888, help='run on the given port', type=int)
define('mongo_host', default="localhost", help="mongo host")
define('mongo_test', default="test", help="mongo host")
define('translation_path', default=os.path.join(BASE_PATH, 'translates'))

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'cookie_secret': 'bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=',
    # 'xsrf_cookies': True,
    'login_url': '/login',
    'debug': True
}
