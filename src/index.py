import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="/quote">Get a quote</a><br>')
        self.write('<a href="/account/alice">Im Alice</a><br>')
        self.write('<a href="/account/bob">Im Bob</a><br>')
        self.write('<a href="/account/carol">Im Carol</a><br>')
        self.write('<a href="/account/dave">Im Dave</a><br>')
        self.write('<a href="/roullete">Play Roullete</a><br>')