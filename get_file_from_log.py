#!/usr/bin/python
#
import os
import sys


def hex_to_ascii(input):
    return input.decode('hex')

def readfile(infile):
    f = open(infile,"r")
    return f.read()

if __name__ == '__main__':
    infile = sys.argv[1]
    instr = sys.argv[2]
    tld = instr.split(".",1)[1]

    print "[*] Starting to parse file from DNS logs with mark " + instr + ", from file " + infile + ", TLD " + tld
    f = open(infile,"r")
    parsef = None
    filedata=""
    for fline in f.readlines():
        if instr in fline:
            parsef = True
            continue

        if parsef == True:
            if tld in fline:
                filedata+=fline.split("(")[1].split(")")[0].split(".")[0]

    print ""
    print "[*] File data: "
    print hex_to_ascii(filedata)

