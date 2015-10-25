import tornado
import json


class HealthCheckHandler(tornado.web.RequestHandler):
    def initialize(self, logger, mongodb):
        self.logger = logger
        self.mongodb = mongodb

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request to health check')

        # noinspection PyDictCreation
        components = {
            'mongodb': None
        }

        components['mongodb'] = yield self.mongodb.alive()

        for key in components:
            if components[key] is None:
                components[key] = False

        result = json.dumps({
            'status': False not in components.values(),
            'components': components
        })

        self.logger.info('Response for health check: %s' % result)
        self.write(result)
