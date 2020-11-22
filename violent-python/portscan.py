import socket
from optparse import OptionParser

def scan_ports(ip, start = 1, end = 1024):
    for port in range(start, end):
        try:
            s = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
            s.settimeout(1000)
            s.connect((127.0.0.1, port))
            print('%d:OPEN' % (port))
            s.close
        except:
            continue

 def main():
    parser = OptionParser()
    parser.add_option("-d", "--start", dest="start",
                  help="the dictionary file to use")
    parser.add_option("-e", "--end", dest="end",
                  help="the end port")

if __name__ == '__main__':
    main()