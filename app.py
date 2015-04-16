import tornado.httpserver
import tornado.web

class ApiHandler(tornado.web.RequestHandler):
    def get(self, uuid):
        self.write("you wanted to get %s"%uuid)

    def post(self, uuid):
        self.write('you posted to %s'%uuid)
    
    def delete(self, uuid):
        self.write('you wanted to delete %s'%uuid)


application = tornado.web.Application([
    (r"/api/index/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})", ApiHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
