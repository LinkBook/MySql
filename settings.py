# coding: utf-8
import os

TORNADO_SETTINGS = dict(
    debug=True,
    login_url='/login',
    post_login_redirect_url='/',
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    autoescape=None,
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    **{
        'pycket': {
            'engine': 'redis',
            'storage': {
                'host': 'localhost',
                'port': 6379,
                'db_sessions': 10,
                'db_notifications': 11,
                'max_connections': 2 ** 31,
            },

        },
    }
)
