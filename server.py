import tornado.ioloop
import tornado.web
import logging
from handler import HealthCheckHandler
import motor

PORT = 33001
MAX_BUFFER_SIZE = 50 * 1024**2

DB_ADDRESS = 'mongodb://localhost:27017'
DB_NAME = 'test'

logging.basicConfig(
    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
    filename='log/server.log',
    level=logging.DEBUG
)

# mongodb = motor.MotorClient(DB_ADDRESS)

context = dict(
    logger=logging.getLogger('HealthCheck'),
    # database=mongodb[DB_NAME]
)

app = tornado.web.Application([
    (r"/", HealthCheckHandler, context),
], autoreload=True)

app.listen(PORT)

if __name__ == "__main__":
    ioLoop = tornado.ioloop.IOLoop.current()
    try:
        logging.info("Starting HTTP proxy on port %d" % PORT)
        ioLoop.start()
    except KeyboardInterrupt:
        logging.info("Shutting down server HTTP proxy on port %d" % PORT)
        ioLoop.stop()
