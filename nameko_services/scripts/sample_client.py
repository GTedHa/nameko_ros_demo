#!/usr/bin/env python3

from nameko.standalone.rpc import ClusterRpcProxy


AMQP_URI = "pyamqp://guest:guest@localhost"


config = {
    'AMQP_URI': AMQP_URI
}


if __name__ == '__main__':
    with ClusterRpcProxy(config) as cluster_rpc:
        res = cluster_rpc.sample_server.hello("G.Ted")
        print(res)
