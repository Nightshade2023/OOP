import asyncio
import os, os.path
import tornado.web
import index, quote, account, Roullete, TemplateTest
import os

HTMLDIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 "..","html"
    )
)

def makeApp():
    endpoints=[
        ("/",index.Handler),
        ("/quote",quote.Handler),
        ("/fancy",TemplateTest.Handler),
        ("/account/.*",account.Handler),
        ("/roullete", Roullete.Handler)
    ]
    app = tornado.web.Application(endpoints,
        static_path=HTMLDIR
    )
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()