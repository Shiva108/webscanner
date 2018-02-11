#!/usr/bin/env python
# Created buy Shiva @ CPH:SEC / Cyberium White Hacker Team
# Respects to Primalsecurity, Violent Python & Offensive Python

try:
    from bs4 import BeautifulSoup
    import sys, optparse, socket, os
    from urllib.request import urlopen
except ModuleNotFoundError:
    print('Make sure modules are installed correctly! ', ModuleNotFoundError)
except RuntimeError:
    print('Something went wrong! Module Import Runtime Error ', RuntimeError)


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'


def webreq(server, resources):  # Function takes in URL, and resources variable which contains the requests
    try:
        resource = []
        for item in open(resources, 'r'):  # Loop through the resource file
            resource.append(item.strip())  # Append each item in the file to the array
        for item in resource:  # Loop through the array and create a request for each item in the array
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)  # set a timeout on the socket connection
            url = server.strip() + item.strip()  # Format the url variable to store the request: /
            # ie "http://www.site.com/CFIDE/administrator/enter.cfm"
            request = urlopen(url)  # Make the request
            if search:  # If the "search" variable is true (-s)
                parsed = BeautifulSoup(request.read(), "lxml")  # Parse the output with BeautifulSoup
                if search in str(parsed):  # If the search string is in the output print the next line
                    print(Colors.GREEN + "[+] URL: " + url + " [" + str(
                        request.getcode()) + "] Found: '" + search + "' in ouput")
            elif request.getcode() == 404:  # If we got an HTTP status code
                print(Colors.RED + "[+] URL: " + url + " [" + str(
                    request.getcode()) + "]")  # Print the URL and status code
        if request.getcode():
            print(Colors.GREEN + "[+] URL: " + url + " [" + str(request.getcode()) + "]")

    except RuntimeError:
        print('This should\'nt happen: ', RuntimeError)


def main():
    # Creates CLI switches and stores in variables
    parser = optparse.OptionParser(sys.argv[0] + ' ' + '-i <file_with URLs> -r  -s [optional]')
    parser.add_option('-i', dest='servers', type='string', help='specify target file with URLs')
    parser.add_option('-r', dest='resources', type='string', help='specify a file with resources to request')
    parser.add_option('-s', dest='search', type='string', help='[optional] Specify a search string -s ')
    (options, args) = parser.parse_args()
    servers = options.servers
    resources = options.resources
    global search;
    search = options.search

    if (servers is None) and (resources is None):  # Checks to make sure proper CLI switches were given
        print(parser.usage)  # if not print usage
        sys.exit(0)

    if servers:
        for server in open(servers, 'r'):  # loop through each URL in the file
            webreq(server, resources)  # Invoke the webreq function


if __name__ == '__main__':
    main()
