#!/usr/bin/env python

import tornado.httpserver, tornado.ioloop, tornado.web

from api import settings
from api.greet_handler import GreetHandler


def main():
    if settings.DEBUG:
        from tornado.log import enable_pretty_logging
        enable_pretty_logging()

    application = tornado.web.Application(
        [
            (r'/greet', GreetHandler),
        ],
    )

    # Spawn multiple process as necessary
    server = tornado.httpserver.HTTPServer(application)
    server.bind(settings.TORNADO_PORT_API)
    server.start(settings.TORNADO_PROCESSES)  # Forks multiple sub-processes
    tornado.ioloop.IOLoop().current().start()


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        pass
