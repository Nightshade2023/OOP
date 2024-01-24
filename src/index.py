import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="/quote">Get a quote</a><br>')
        self.write('<a href="/alice">Im Alice</a><br>')
        self.write('<a href="/bob">Im Bob</a><br>')
        self.write('<a href="/carol">Im Carol</a><br>')
        self.write('<a href="/dave">Im Dave</a><br>')
        self.write('<a href="./roullete">Play Roullete</a><br>')