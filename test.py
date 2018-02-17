import urllib3

server = 'http://httpbin.org/anything'


def urllook(server):
    server = str(server)
    print(server)
    http = urllib3.PoolManager()  # Init Pool object
    r = http.request('GET', server)
    print(r.data)
    print(server)


urllook(server)
