import tornado.httpserver
import tornado.web

from .index import IndexClient

class ApiHandler(tornado.web.RequestHandler):
    def get(self, key):
        self.write("you wanted to get %s"%key)

    def post(self, key):
        self.write('you posted to %s'%key)
    
    def delete(self, key):
        self.write('you wanted to delete %s'%key)


application = tornado.web.Application([
    (r"/api/index/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})", ApiHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
