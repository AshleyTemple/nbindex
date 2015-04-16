from tornado.httpclient import AsyncHTTPClient
import tornado.gen
from tornado.ioloop import IOLoop

class IndexClient(object):
    # Abstraction around Elasticsearch so that this is the only
    # code to change should a different document store become more appealing
    
    def __init__(self, url='http://localhost:9200', ioloop=None):
        self.url = url
        self.ioloop = ioloop or IOLoop.instance()
        self._http_client = AsyncHTTPClient(self.ioloop)

    def get(self, key):
        pass

    def post(self, key):
        pass

    def delete(self, key):
        pass    

    @tornado.gen.coroutine
    def _request(self, method, url, data=None):
        request = httpclient.HTTPRequest(url,
                                         method=method,
                                         body=data)

        response = yield self._http.fetch(request)
        raise tornado.gen.Return(response)
