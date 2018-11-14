#!/usr/bin/env python3

import time

import eventlet
eventlet.monkey_patch()
from nameko.containers import ServiceContainer
from nameko_services.sample_server import SampleServer


AMQP_URI = "pyamqp://guest:guest@localhost"


if __name__ == '__main__':
    container = ServiceContainer(SampleServer, config={'AMQP_URI': AMQP_URI})
    service_extensions = list(container.extensions)
    container.start()
    print("started")
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("Keyboard interrupt occurred")
            break
    container.stop()
