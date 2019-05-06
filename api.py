import tornado.ioloop
import tornado.web
from data import Data
from gethandler import GetHandler

datas = Data()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("CFD Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/getdatas", GetHandler, dict(datas = datas)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
