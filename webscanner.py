#!/usr/bin/env python
# Created buy Shiva @ CPH:SEC / Cyberium White Hacker Team
# Respects to Violent Python & Offensive Python
# vs 0.11

try:
    from bs4 import BeautifulSoup
    import sys, optparse, socket, os
    from colorama import Fore, Back, Style
    import urllib3
    import certifi
    import threading
    # import time
    # import logging
except ModuleNotFoundError:
    print('Make sure modules are installed correctly! ', ModuleNotFoundError)
except RuntimeError:
    print('Something went wrong! Module Import Runtime Error ', RuntimeError)


def webreq(server):
    print(Fore.GREEN + '[+] ', server)
    http = urllib3.PoolManager()  # Init Pool object
    r = http.request('GET', server)
    print(r.data)
    # print(server)


def main():
    # Creates CLI switches and stores in variables
    parser = optparse.OptionParser(sys.argv[0] + ' ' + '-u <single url> -i <file_with URLs> ')
    # parser.add_option('-i', dest='servers', type='string', help='specify target file with URLs')
    parser.add_option('-u', dest='singleurl', type='string', help='specify single URL in format http(s)://url:port')
    (options, args) = parser.parse_args()
    # servers = options.servers
    singleurl = options.singleurl

    if singleurl is None:  # Checks to make sure proper CLI switches were given
        print(parser.usage)  # if not print usage
        sys.exit(0)

    # if (servers is None) & (singleurl is None):  # Checks to make sure proper CLI switches were given
    #     print(parser.usage)  # if not print usage
    #     sys.exit(0)

    if singleurl is not None:
        # print(singleurl)
        # server = singleurl
        webreq(singleurl)


if __name__ == '__main__':
    main()
