# coding=utf-8
"""
Handlers
"""
import tornado.httpserver
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from application import *
from settings import TORNADO_SETTINGS

define("port", default=8000, help="run on the given port", type=int)
""" dastoore taiin porti ke bayad az an goosh kard baraye pasokh dadane request """

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', MainHandler),
                  (r'/index', MainHandler),
                  (r'/Dashboard', DashBoardHandler),
                  (r'/about', AboutHandler),
                  (r'/Contact', ContactHandler),
                  (r'/help', HelpHandler),
                  (r'/Login', LoginHandler),
                  (r'/Logout', LogoutHandler),
                  (r'/Register', RegisterHandler),
                  (r'/Webpages', WebpagesHandler),
                  (r'/webshow', WebshowHandler),
                  (r"/upload1", UploadHandler),
                  (r"/upload2", Upload2Handler),
                  (r'/aa', Ahandler),
                  (r'/mm', Mhandler),
                  ], **TORNADO_SETTINGS
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
