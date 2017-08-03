#!/usr/bin/python


from parts import *
import csv
import sys
import markdown
import os



#read csv, and split on "," the line
data = open(sys.argv[1], "rb")
csv_file = csv.reader(data, delimiter=",")

output = []

def find(file, plist):
    for row in file:
        if str(plist) == row[3]:
            output.append(row[3] + row[4].split(",")[2]+ '..........' + '**'+row[6]+'**  ')
            data.seek(0)
            return

    data.seek(0)


def go(partslist, stext):
    output.append('\n')  # newline
    output.append(stext)
    data.seek(0)
    for item in partslist:
        find(csv_file, item)

    data.seek(0)

csv_file.next() #print sub
van = csv_file.next()

output.append('#'+ van[5])

go(RECIEVERS, '##RECIEVERS')

go(DISHNET, '##DISHNET')

go(LNBFS,"##LNBFS/SWITCHES")

go(CONN, "##CONNECTIVITY")

go(XIP, "##XIP COMPONENTS")

go(HXIP, "##HYBRID XIP COMPONENTS")

go(REMOTES, "##REMOTES")

go(OTA, "##OTA")

go(SHS, "##SHS")

go(MOUNTS, "##MOUNTS")

go(DNMETALS, "##DISHNET METALS")

go(BRP, "##BRP")

go(SWMR, "##SWMR")


outfile = open('out.tmp', 'w')



for lines in output:
    outfile.write("%s\n" % str(lines))

outfile.close()

with open('out.tmp', 'rb') as f:
    txt = f.read()
    html = markdown.markdown(txt)

with open(sys.argv[1][:-3] + 'html', 'wb') as o:
    o.write(html)


os.remove('out.tmp')







