import tornado.web
import random

user_accounts = {
    "/alice":{
            "RealName": 'Alice Smith',
            "DOB": 'Jan. 1',
            "Email": 'alice@example.com'
            },
    "/bob":  {
            "RealName": 'Bob Jones',
            "DOB": 'Dec. 31',
            "Email": 'bob@bob.xyz'
            },
    "/carol":{
            "RealName": 'Carol Ling',
            "DOB": 'Jul. 17',
            "Email": 'carol@example.com'
            },
    "/dave": {
            "RealName": 'Dave N. Port',
            "DOB": 'Mar. 14',
            "Email": 'dave@dave.dave'
            },
}

class ProfileHandler(tornado.web.RequestHandler):
    def post(self):
        real_name = user_accounts(self("RealName"))
        dob = user_accounts(self("DOB"))
        email = user_accounts(self("Email"))

        self.render("account.html", RealName=real_name, DOB=dob, Email=email)
