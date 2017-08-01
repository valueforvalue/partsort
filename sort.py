#!/usr/bin/python


from parts import *
import csv
import sys



#read csv, and split on "," the line
data = open(sys.argv[1], "rb")
csv_file = csv.reader(data, delimiter=",")

output = []

def find(file, plist):
    for row in file:
        if str(plist) == row[3]:
            output.append(row[3] + row[4].split(",")[2]+ '.....' + '**'+row[6]+'**  ')
            data.seek(0)
            return

    data.seek(0)



def shsfind(file, plist):
    for row in file:
        if str(plist) == row[3]:
            output.append(row[3]+ row[4].split(",")[2] + '.....' + '**'+row[6]+'**  ')
            data.seek(0)
            return

    data.seek(0)
#.split(",")[1]

csv_file.next() #print sub
van = csv_file.next()

output.append('#'+ van[5])
output.append('\n')
output.append('##RECIEVERS')

for reciever in RECIEVERS:
    find(csv_file, reciever)

output.append('\n')#newline
output.append("##DISHNET")
data.seek(0)

for dish in DISHNET:
    find(csv_file, dish)


output.append('\n')#newline
output.append("##LNBFS/SWITCHES")
data.seek(0)

for lnbf in LNBFS:
    find(csv_file, lnbf)


output.append('\n')#newline
output.append("##CONNECTIVITY")
data.seek(0)

for item in CONN:
    find(csv_file, item)


output.append('\n')#newline
output.append("##XIP COMPONENTS")
data.seek(0)

for item in XIP:
    find(csv_file, item)

output.append('\n')#newline
output.append("##HYBRID XIP COMPONENTS")
data.seek(0)

for item in HXIP:
    find(csv_file, item)

output.append('\n')#newline
output.append("##REMOTES")
data.seek(0)

for remote in REMOTES:
    find(csv_file, remote)

output.append('\n')#newline
output.append("##OTA")
data.seek(0)

for item in OTA:
    find(csv_file, item)

output.append('\n')#newline
output.append("##SHS")
data.seek(0)

for item in SHS:
    shsfind(csv_file, item)


output.append('\n')#newline
output.append("##MOUNTS")
data.seek(0)

for item in MOUNTS:
    find(csv_file, item)

output.append('\n')#newline
output.append("##DISHNET METALS")
data.seek(0)

for item in DNMETALS:
    find(csv_file, item)



output.append('\n')#newline
output.append("##BRP")
data.seek(0)

for item in BRP:
    find(csv_file, item)

output.append('\n')#newline
output.append("##SWMR")
data.seek(0)

for item in SWMR:
    find(csv_file, item)


outfile = open(sys.argv[2], 'w')

for lines in output:
    outfile.write("%s\n" % str(lines))






