import tornado.web
import random

user_accounts = {
    "/account/alice": {
        "RealName": 'Alice Smith',
        "DOB": 'Jan. 1',
        "Email": 'alice@example.com'
    },
    "/account/bob": {
        "RealName": 'Bob Jones',
        "DOB": 'Dec. 31',
        "Email": 'bob@bob.xyz'
    },
    "/account/carol": {
        "RealName": 'Carol Ling',
        "DOB": 'Jul. 17',
        "Email": 'carol@example.com'
    },
    "/account/dave": {
        "RealName": 'Dave N. Port',
        "DOB": 'Mar. 14',
        "Email": 'dave@dave.dave'
    },
}

class Handler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path
        if p in user_accounts:
            account_info = user_accounts[p]
            real_name = account_info["RealName"]
            dob = account_info["DOB"]
            email = account_info["Email"]

            self.render("account.html", RealName=real_name, DOB=dob, Email=email)
        else:
            self.send_error(404, reason="User not found")
