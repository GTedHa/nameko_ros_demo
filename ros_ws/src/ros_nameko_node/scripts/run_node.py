#!/usr/bin/env python

import time

import eventlet
eventlet.monkey_patch()

import rospy
from nameko.containers import ServiceContainer
from nameko.rpc import rpc

import std_msgs


class SampleServer:
    name = "sample_server"
    publisher = rospy.Publisher("/greeting", std_msgs.msg.String, queue_size=5)

    @rpc
    def hello(self, name):
        greeting = "Hello, {}!".format(name)
        SampleServer.publisher.publish(greeting)
        return greeting


AMQP_URI = "pyamqp://guest:guest@localhost"


if __name__ == '__main__':
    rospy.init_node('ros_nameko_node', )
    container = ServiceContainer(SampleServer, config={'AMQP_URI': AMQP_URI})
    service_extensions = list(container.extensions)
    print("before-start")
    container.start()
    print("started")
    while True:
        try:
            time.sleep(1)
        except Exception:
            print("Keyboard interrupt occurred")
            break
    container.stop()
