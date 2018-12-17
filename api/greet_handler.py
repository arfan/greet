import json
import tornado.web


class GreetHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.set_status(200)
        self.write(json.dumps(
            {
                "greet": "Hello"
            }
        ))
