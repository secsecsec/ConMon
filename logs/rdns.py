# -*- coding: utf-8 -*-
#$ python rdns.py pkt_list_ip_test.txt 
# creates rdns_pkt_list_ip_test.txt

import sys
import csv
import socket

#defines
DNS_TIMEOUT = 5

def reverseDNSlookup(addr):
    try:
        if hasattr(socket, 'setdefaulttimeout'):
            #timeout = 5s
            socket.setdefaulttimeout(DNS_TIMEOUT) 
        reverse_DNS=socket.gethostbyaddr(addr)
        return reverse_DNS[0]
    except socket.herror:
        #print "reverse DNS lookup failed for ",addr
        return "None"


def main(argv):
    if(len(argv)==0):
        sys.exit("insufficient arguments")
    fn = argv[0]
    logfile  = open(fn, "rb")
    rows = csv.reader(logfile, delimiter='\t')
    rdnslog = open('rdns_'+fn, 'w')

    for col in rows:
        if(col[5]=="INC"):
            #serverip
            dns=reverseDNSlookup(col[9])
            key = dns
            
        elif(col[5]=="OUT"):
            #serverip
            dns=reverseDNSlookup(col[10])
            key = dns
        col.append(dns)
        
        line=""
        for c in col:
            line = line+c+"\t"
        line = line+"\n"
        rdnslog.write(line)
    #end of file
    rdnslog.close()
    logfile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
