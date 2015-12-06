# coding=utf-8


import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymysql


# from tornado.options import define, options
#
# define("port", default=9999, help="run on the given port", type=int)


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")


class DashBoardHandler(BaseHandler):
    def get(self):
        """

        :type self: object
        """

        a = self.get_secure_cookie("username")
        if a:
            self.render("Dashboard.html")
            return

        self.render("Login.html")


class HelpHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('help.html')


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Register.html')

    def post(self):
        sql = "INSERT INTO user(name,family,username,user_type,picture,email,password)VALUES(%s, %s,%s, %s, %s, %s, %s)"

        name = self.get_argument("name")
        family = self.get_argument("family")
        username = self.get_argument("username")
        user_type = self.get_argument("user-type")
        picture = self.get_argument("flpicture")
        email = self.get_argument("email")
        password = self.get_argument("password")
        rep_pass = self.get_argument("password")
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="linkbook")
        cur = conn.cursor()
        cur.execute(sql, (name, family, username, user_type, picture, email, password))
        self.render("Login.html")
        cur.close()
        conn.commit()
        conn.close()


class LoginHandler(BaseHandler):
    def get(self):
        self.render('Login.html')

    def post(self):
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="linkbook")
        cur = conn.cursor()
        a = self.get_argument("username")
        b = self.get_argument("password")
        s = cur.execute("select user_id from user where username = %s and password = %s", (a, b))

        if s:
            self.set_secure_cookie("username", self.get_argument("username"))
            self.write("<script>alert('کوکی ست شد... خوش آمدید ')</script>")
            self.render("Dashboard.html")

        else:
            self.write("<script>alert('همچین کاربری نداریم ')</script>")
            self.render('Login.html')
        cur.close()
        conn.commit()
        conn.close()


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_all_cookies()
        self.redirect("/")


class WebpagesHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Webpages.html', n=1)


class WebshowHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('webshow.html')


class Ahandler(tornado.web.RequestHandler):
    def post(self):
        sql = "INSERT INTO festival(Logoname_fest, url,Title,Body)VALUES(%s, %s,%s, %s)"

        Title = self.get_argument("fest-title")
        Body = self.get_argument("fest-text")
        Logoname_fest = self.get_argument("fest-logo")
        url = self.get_argument("fest-url")
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="linkbook")
        cur = conn.cursor()
        cur.execute(sql, (Logoname_fest, url, Title, Body))
        self.redirect("/")
        cur.close()
        conn.commit()
        conn.close()


class Mhandler(tornado.web.RequestHandler):
    def post(self):
        sql = "INSERT INTO webpageregister(vision,mision)VALUES(%s, %s)"
        vision = self.get_argument("vision")
        mision = self.get_argument("mision")
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="linkbook")
        cur = conn.cursor()
        cur.execute(sql, (vision, mision))

        self.write("<script>alert('اطلاعات ثبت شد')</script>")
        self.redirect("/")
        cur.close()
        conn.commit()
        conn.close()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class UploadHandler(tornado.web.RequestHandler):
    def post(self):

        try:
            file1 = self.request.files['file1'][0]
        except:
            file1 = None
        original_fname = file1['filename']
        m = original_fname.split('.')
        n = '1.' + m[1]

        output_file = open("static/uploads/1/" + n, 'wb')
        output_file.write(file1['body'])

        self.render('Webpages.html', n=n)


class Upload2Handler(tornado.web.RequestHandler):
    def post(self):

        try:
            file2 = self.request.files['file2'][0]
        except:
            file2 = None
        original_fname = file2['filename']
        m = original_fname.split('.')
        n = '1.' + m[1]

        output_file = open("static/uploads/2/" + n, 'wb')
        output_file.write(file2['body'])

        self.render('Webpages.html', n=n)


class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')


class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Contact.html')

    def post(self):
        sql = "INSERT INTO contact(cname, cemail, cmessage)VALUES(%s, %s,%s)"

        cname = self.get_argument("namec")
        cemail = self.get_argument("email")
        cmessage = self.get_argument("messege")
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="linkbook")
        cur = conn.cursor()
        cur.execute(sql, (cname, cemail, cmessage))
        self.redirect("/")
        cur.close()
        conn.commit()
        conn.close()
