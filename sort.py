#!/usr/bin/python3


from parts import *
import csv
import sys
import markdown
import os
import datetime
import glob

files = glob.glob('*.csv')

for filename in files:
    data = open(filename, "r")
    csv_file = csv.reader(data, delimiter=",")
    
    output = []
    
    def find(file, plist):
        for row in file:
            if str(plist) == row[1]:
                output.append('**' + row[1] + '**' + parse(row[3]) + '..........' + '**'+row[2]+'**  ')
                data.seek(0)
                return
    
        data.seek(0)

    
    def parse(query):
        
        querywords = query.strip().split(',')
        resultwords = [word for word in querywords if word.strip() in YESWORDS]
        result = ' '.join(resultwords)
        return result
    
    
    def go(partslist, stext):
        output.append('\n')  # newline
        output.append(stext)
        data.seek(0)
        for item in partslist:
            find(csv_file, item)
    
        data.seek(0)
    
    next(csv_file)
    van = next(csv_file)
    
    output.append('#'+ van[0] + ' *' + str(datetime.date.today()) + '*')
    
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
    
    go(ISSUEOFF, "##ISSUE OFF")
    
    
    with open('out.tmp', 'w') as of:
        for lines in output:
            of.write("%s\n" % str(lines))
    
    with open('out.tmp', 'r') as f:
        txt = f.read()
        html = markdown.markdown(txt)
    
    with open(filename[:-3] + 'html', 'w') as o:
        o.write(html)
    
    
    os.remove('out.tmp')







