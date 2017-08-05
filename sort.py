#!/usr/bin/python3


from parts import *
import csv
import sys
import markdown
import os



data = open(sys.argv[1], "r")
csv_file = csv.reader(data, delimiter=",")

output = []

def find(file, plist):
    for row in file:
        if str(plist) == row[1]:
            output.append('**' + row[1] + '**' + parse(row[3]) + '..........' + '**'+row[2]+'**  ')
            data.seek(0)
            return

    data.seek(0)
#row[3].split(",")[-1]

def parse(query):
    yeswords = ['VIP211Z', 'VIP222K', 'VIP622', 'VIP612', 'VIP722K', 'HOPPER WITH SLING CR','HOPPER', 'REMAN',
                'SLING', 'HOPPER3', 'JOEY 2.0', 'JOEY', '4K JOEY', 'SUPER JOEY', 'WALLY', 'DPP TRIPLE',
                'HYBRID TRIPLE LNBF', 'W/129 BRKT', 'DPP 500 PLUS', 'DPP TWIN', 'EASTERN ARC',
                'DPP44 MKII', 'SWITCH', '(DPH42) DISH PRO HYBRID 42', 'ADAPTER', 'WIFI', 'ROUTER', 'HYBRID DUO HUB',
                'INTERNET CONNECTOR', 'WIRELESS JOEY ACCESS POINT 2', 'SLINGBOX', 'HOPPER/JOEY SOLO', 'HOPPER/JOEY DUO', 'NODE',
                'HYBRID SOLO HUB', 'REMOTE', '20.1', 'RMTE', '21.1', '40.0', '40.0.0', '52.0 REMOTE', '50.0', 'FL5500 FLATWAVE',
                'DIGINOVA BOSS PLUS PSU  120V', 'DIGITAL DONGLE', 'SURGE PROTECTOR', '2 OUTLET', 'SKIN', 'BLUE', 'RED', 'PINK', 'GREEN', 'YELLOW',
                'HDMI', 'BRAIDED', "8'", "15'", "30'", 'OPTICAL CABLE', 'AUDIOQUEST PEARL', '8FT', 'TOSLINK', "12'",
                'FULL', 'MOTION', 'LESS THAN 32" SM', 'MEDIUM 32" - 55" MD', 'TILT', '24- 40" MD', 'SOUNDBAR', 'SUBWOOFER', 'DEMO', 'DSB1', 'DSB2',
                'BOOM SWIMMER DUO','HDMI 90 DEGREE ADAPTER - AUDIOQUEST', 'HOPPERGO', 'BLUETOOTH', 'USB', 'BLACK', 'WHITE',
                'ECHO DOT', '2TB EXTERNAL', 'D-LINK DIR-868L-ES', 'POLE', '1.66"OD', '41" - 80" LG',
                'FASCIA/GABLE', 'ANGLED', 'FASCIA', 'RAILING', 'CORNER', 'NONPEN' , 'POWER ADAPTER', 'UNDER EAVE',
                'DISH 1000.2 DISHPRO HYBRID TRIPLE LNBF', 'HYBRID TWIN EASTERN ARC', 'TV FULL MOTION', 'SCREEN CLEANER KIT', 'WIRELESS JOEY',
                'HT1100', 'HUGHES', 'MODEM', 'TRIA', 'JR1WKA', 'VS1100', 'ETRIA', 'JUPITER 2', 'HT2000W', 'HA200', 'DP SINGLE', 'STAND',
                'S HOOK', 'BOLT PACK', 'SAMSUNG', 'MID-CONTROL', 'REFLECTOR', '74CM ANTENNA', '2.35"', 'MAST/FOOT/STRUT', 'BACKING STRUCTURE',
                'BRACKET', 'SURFBEAM II', 'JUPITER', '2" TO 2.375" SLEEVE ADAPTER', 'NON PENETRATING PATIO MOUNT ADAPTER KIT', 'HOPPER 3']
    querywords = query.strip().split(',')
    resultwords = [word for word in querywords if word.strip() in yeswords]
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

output.append('#'+ van[0])

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


with open('out.tmp', 'w') as of:
    for lines in output:
        of.write("%s\n" % str(lines))

with open('out.tmp', 'r') as f:
    txt = f.read()
    html = markdown.markdown(txt)

with open(sys.argv[1][:-3] + 'html', 'w') as o:
    o.write(html)


os.remove('out.tmp')







