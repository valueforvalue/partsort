#!/usr/bin/python

import csv
import sys

recievers = [191779, 191772, 169748, 162694, 163089, 190477, 192239, 190514,
             "DN002708", 'DN005254', 207406, 'DN007362', 'DN003316', 'DN007416',
             190560, 200349, 'DN005139', 207000, 'DN008438', 207971, 203904, 'DN004866',
             'DN009402', 208381, 'DN009734', 'DN010160']

dishnet = ['DN008191', 'DN008194', 197736, 'DN003269', 'DN001958', 'DN005595', 'DN005596',
           'DN001955', 'DN008593', 'DN008594']

lnbfs = [112614, 139873, 145511, 151027, 201499, 'DN007060', 148746, 176597, 163060, 184187, 201700,
         173405, 145578, 174627, 209925]

conn = ['DN000010', 'DN006086', 190149, 209783, 179081]

xip = [192092, 192093]

hxip = [203951, 204861]

remotes = [189753, 189754, 186214, 'DN008710',192091,  205284, 212314, 207793]

ota = [194858, 'DN000336', 'DN007589']

shs = ['DN000128', 'DN004340', 'DN006347', 'DN005439', 'DN005440', 'DN005441', 'DN006554',
       'DN007966', 'DN007967', 'DN007968', 'DN007969', 'DN009293', 'DN000731', 191411, 191412,
       'DN006691', 191414, 191416, 191417, 191418, 'DN003965', 'DN000732', 'DN008528', 'DN008621',
       'DN008622', 'DN008970', 'DN008971', 'DN007575', 'DN005317', 205900, 'DN003966', 'DN006692',
       204689, 'DN004115', 'DN006348', 'DN006349', 'DN004833', 'DN006283', 'DN009367', 'DN009740']

mounts = [198051, 192920, 185811, 185781, 181760, 198158, 198153, 198727, 189856]

dnmetals = [206133, 209983, 206129, 206116, 206118, 206120, 210026, 210032]

brp = [186933, 188454]

swmr = ['DN009340', 'DN009341', 'DN009436']




#read csv, and split on "," the line
data = open(sys.argv[1], "rb")
csv_file = csv.reader(data, delimiter=",")


def find(file, plist):
    for row in file:
        if str(plist) == row[3]:
            print row[3], row[4].split(",")[2],'.....', row[6]
            data.seek(0)
            return

    data.seek(0)



def shsfind(file, plist):
    for row in file:
        if str(plist) == row[3]:
            print row[3], row[4],'.....', row[6]
            data.seek(0)
            return

    data.seek(0)
#.split(",")[1]

line = csv_file.next() #print sub
line = csv_file.next()

print line[5]
print
print 'RECIEVERS'

for reciever in recievers:
    find(csv_file, reciever)

print #newline
print "DISHNET"
data.seek(0)

for dish in dishnet:
    find(csv_file, dish)

print #newline
print "LNBFS/SWITCHES"
data.seek(0)

for lnbf in lnbfs:
    find(csv_file, lnbf)

print #newline
print "CONNECTIVITY"
data.seek(0)

for item in conn:
    find(csv_file, item)

print #newline
print "XiP COMPONENTS"
data.seek(0)

for item in xip:
    find(csv_file, item)

print #newline
print "HYBRID XiP COMPONENTS"
data.seek(0)

for item in hxip:
    find(csv_file, item)

print #newline
print "REMOTES"
data.seek(0)

for remote in remotes:
    find(csv_file, remote)

print #newline
print "OTA"
data.seek(0)

for item in ota:
    find(csv_file, item)

print #newline
print "SHS"
data.seek(0)

for item in shs:
    shsfind(csv_file, item)


print #newline
print "MOUNTS"
data.seek(0)

for item in mounts:
    find(csv_file, item)

print #newline
print "DISHNET METALS"
data.seek(0)

for item in dnmetals:
    find(csv_file, item)



print #newline
print "BRP"
data.seek(0)

for item in brp:
    find(csv_file, item)

print #newline
print "SWMR"
data.seek(0)

for item in swmr:
    find(csv_file, item)





