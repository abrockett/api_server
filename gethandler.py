import tornado.web
import data
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, datas):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.datas = datas
        
    def get(self):
        self.write(self.datas.json_list())
