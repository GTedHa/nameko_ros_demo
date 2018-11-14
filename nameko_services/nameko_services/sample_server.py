#!/usr/bin/env python3


from nameko.rpc import rpc


class SampleServer:
    name = "sample_server"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
