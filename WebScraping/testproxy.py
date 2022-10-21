import urllib.request
import socket
import urllib.error

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Chrome')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://httpbin.org/ip')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False

def main():
    socket.setdefaulttimeout(120)

    # proxy IPs
    #proxyList = ['45.79.90.143:44554',
#'139.162.182.54:49165',
#'100.20.156.53:80',
#'45.56.75.90:5344',
#'100.20.122.18:80',
#'47.91.44.217:8000',
#'198.69.13.254:9090',
#'45.171.109.1:999']

proxylist = set("C:/Users/19053/OneDrive - NC/Desktop/proxylist.txt")
with open("proxylist.txt", "r") as f:
    file_lines1 = f.readlines()
    with open('proxylist.txt') as f:
        for line in f:
       # For Python3, use print(line)
            print()
            if 'str' in line:
                break
    #for line1 in file_lines1:
     #   proxylist.add(line1.strip())
        
    proxies = {
        'http': 'http://'+line
        }   
    for currentProxy in proxylist:
        if is_bad_proxy(currentProxy):
            print("Bad Proxy %s" % (currentProxy))
    else:
        print("%s is working" % (currentProxy))

if __name__ == '__main__':
    main() 