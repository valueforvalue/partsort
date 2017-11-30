#!/usr/bin/python3

from string import Template
from parts import *
from fun import *
import csv
import sys
import markdown
import os
import datetime
import glob
import time
import random

print(LOGO)
random.shuffle(PHRASE)
print("\n" + random.choice(PHRASE) + "\n")
time.sleep(3)

with open('items.dat', mode='r') as infile:
    reader = csv.reader(infile)
    items_list = {rows[0]:rows[1] for rows in reader}
        
files = glob.glob('*.tsv')

for filename in files:
    data = open(filename, "r")
    csv_file = csv.reader(data, delimiter="\t")
    
    output = []
    
    def find(file, plist):# Find and reorder parts 
        for row in file:
            if str(plist) == row[1]:
                output.append('**' + row[1] + '**' + parse(row[1]) + '..........' + '*'+row[2]+'*  ')
                data.seek(0)
                return
    
        data.seek(0)

    
    def parse(itemid):
        return items_list[itemid.strip()]   
    
    
    def go(partslist, stext):# Setup headers and reset data pointer
        output.append('\n')  # newline
        output.append(stext)
        data.seek(0)
        for item in partslist:
            find(csv_file, item)
    
        data.seek(0)
    
    next(csv_file)
    van = next(csv_file)
    
    output.append('#'+ van[0] + ' ' + str(datetime.date.today()))
    
    go(RECIEVERS, '##RECEIVERS')
    
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
    
    
    with open('out.tmp', 'w') as of: #Write temp file
        for lines in output:
            of.write("%s\n" % str(lines))
    
    with open('out.tmp', 'r') as f:#Read temp file for markdown
        txt = f.read()
        md_html = markdown.markdown(txt)
    
    html_template = Template(skeleton)
    
    complete_html = html_template.substitute(markdown=md_html)
    
    
    
    with open(filename[:-3] + 'html', 'w') as o:#Write markdown html
        o.write(complete_html)
    
    
    os.remove('out.tmp')
    
print("So much fun!!!")
print('\n')
print('\n')
print("Version 0.4.2 Simpler Edition")
time.sleep(3)







