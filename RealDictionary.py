from typing import Any
import numpy as np
import math
from math import radians, cos, sin, asin, sqrt
class ListDict(dict):
    """ Dictionary who's values are lists. """
    def __missing__(self, key):
        value = self[key] = []
        return value

filename1 = 'C:\\Users\\thesg\\unique_inventors.txt' #ALGORITHM OUTPUT LIST OF ALL PATENT INVENTORS
filename4 = 'C:\\Users\\thesg\\unique_assignees.txt' #ALGORITHM OUTPUT LIST OF ALL PATENT ASSIGNEES

filename2 = 'C:\\Users\\thesg\\pedersen.txt' #LIST OF ALL LOCATIONS OF ONE GOLD STANDARD INVENTOR
filename3 = 'C:\\Users\\thesg\\pedersenco.txt' #LIST OF ALL COINVENTORS OF GOLD STANDARD INVENTOR (THEY SHARE A PATENT ID)

filename5 = 'C:\\Users\\thesg\\output.txt' #OUTPUT FILE CREATED BY ME TO IDENTIFY PROBLEM AREAS IN ALGORITHM
filename6 = 'C:\\Users\\thesg\\outputcleaned.txt' #ORGANIZED OUTPUT FILE TO BE EASIER TO READ
output = open(filename5, 'w+', encoding='UTF-8')


#print ('ID | Shared Coinventor With | Shared Coassignee With | Is Nearby (High Resolution) | Is Nearby (Low Resolution)', file=output) #FORMATING GOAL FOR FINAL FILE


#Step 1 Creating dictionaries
invdct = ListDict() #Dictionary of Inventors in Pedersen File
coinvdct = ListDict() #Dictionary of Coinventors in Pedersen File

with open(filename2, 'r', encoding='UTF-8') as f:
    for line in f:
        try:
            row = line.split('|')
            id = row[0]
            pats1 = row[11];
            plist = pats1.strip('*').split('~*');
            for p in plist:
                    invdct[id].append(p)
                    coinvdct[p].append(id)
        except:
            print('pass')
#invdct currently has problemID's: the ID's patents
#Coinvdct has ProblemIDPatents: their corresponding ID's
#Goal here: coinvdct1 having problemID's:Coinventors

coinvdct1 = ListDict() #Dictionary of Coinventors (Full output)
coassigneedct1 = ListDict() #Dictionary of Coassignees (Full output

with open(filename1, 'r', encoding='UTF-8') as g:
    for line in g:
        #print(line);
        row = line.split('|')
        ids = row[0]
        pats2 = row[10];
        plist2 = pats2.strip('\n').split('~*');
        # print(plist2);
        for p in plist2:
            # print(p)
            if p in coinvdct:
                problem = coinvdct[p]
                for x in problem:
                    v = coassigneedct1[x]
                    if ids not in v:
                        coassigneedct1[x].append(ids)
        pats2 = row[11];
        plist2 = pats2.strip('\n').split('~*');
        #print(plist2);
        for p in plist2:
            #print(p)
            if p in coinvdct:
                problem = coinvdct[p]
                #print(problem)
                for x in problem:
                        v = coinvdct1[x]
                        if ids not in v:
                                coinvdct1[x].append(ids)
        pats2 = row[12];
        plist2 = pats2.strip('\n').split('~*');
        for p in plist2:
            #print(p)
            if p in coinvdct:
                problem = coinvdct[p]
                for x in problem:
                        v = coinvdct1[x]
                        if ids not in v:
                                coinvdct1[x].append(ids)

#print (coinvdct)
with open(filename4, 'r', encoding='UTF-8') as g:
    for line in g:
        #print(line);
        row = line.split('|')
        ids = row[0]
        pats2 = row[10];
        plist2 =  pats2.strip('\n').split('~');
        for p in plist2:
            # print(p)
            if p in coinvdct:
                problem = coinvdct[p]
                for x in problem:
                    v = coassigneedct1[x]
                    if ids not in v:
                        coassigneedct1[x].append(ids)
        pats2 = row[11];
        plist2 = pats2.strip('\n').split('~');
        for p in plist2:
            #print(p)
            if p in coinvdct:
                #for p in coinvdct:
                problem = coinvdct[p]
                #print(problem)
                for x in problem:
                    #print(ids)
                    v = coassigneedct1[x]
                    #print(v)
                    if ids not in v:
                        coassigneedct1[x].append(ids)
        plist2 = pats2.strip('\n').split('~');
        for p in plist2:
            # print(p)
            if p in coinvdct:
                problem = coinvdct[p]
                for x in problem:
                    v = coassigneedct1[x]
                    if ids not in v:
                            coassigneedct1[x].append(ids)

with open(filename4, 'r', encoding='UTF-8') as g:
    for line in g:
        #print(line);
        row = line.split('|')
        ids = row[0]
        pats2 = row[10];
        plist2 =  pats2.strip('\n').split('~*');
        for p in plist2:
            # print(p)
            if p in coinvdct:
                problem = coinvdct[p]
                for x in problem:
                    v = coassigneedct1[x]
                    if ids not in v:
                        coassigneedct1[x].append(ids)
        pats2 = row[11];
        plist2 = pats2.strip('\n').split('~*');
        for p in plist2:
            #print(p)
            if p in coinvdct:
                problem = coinvdct[p]
                #print(problem)
                for x in problem:
                    #print(ids)
                    v = coassigneedct1[x]
                    #print(v)
                    if ids not in v:
                        coassigneedct1[x].append(ids)
        plist2 = pats2.strip('\n').split('~*');
        for p in plist2:
            # print(p)
            if p in coinvdct:
                problem = coinvdct[p]
                for x in problem:
                    v = coassigneedct1[x]
                    if ids not in v:
                            coassigneedct1[x].append(ids)
#print(coinvdct1)
#print(coassigneedct1)

#print('********IDs that Share a Coinventor********', file = output)
#Checking if any ID's share coinventors
for id1 in coinvdct1:
    for id2 in coinvdct1:
        id1coi = coinvdct1[id1]
        id2coi = coinvdct1[id2]
        id1id2coi = any(check in id1coi for check in id2coi)
        if id1id2coi:
            if id1 != id2:
                print(id1, 'shares a coinventor with', id2, file = output)

#print('********IDs that Share a Coassignee********', file = output)
#Checking if any ID's share coassignees
for id1 in coinvdct1:
    for id2 in coinvdct1:
        id1coa = coassigneedct1[id1]
        id2coa = coassigneedct1[id2]
        id1id2coa = any(check in id1coa for check in id2coa)
        if id1id2coa:
            if id1 != id2:
                print(id1, 'shares a coassignee with', id2, file = output)

#High resolution location comparisons
idToLocationshigh = {}
#print('********High Resolution Location Comparisons********', file=output)
with open(filename2, 'r', encoding='UTF-8') as f:
    for line in f:
        row = line.split('|')
        highresloc = row[7]
        h = highresloc.strip('*').strip('"').strip('.').split('~')
        try:
            idToLocationshigh[row[0]].append(h)
        except:
            idToLocationshigh[row[0]]=h;
#print(idToLocationshigh)
for id1 in idToLocationshigh:
    for id2 in idToLocationshigh:
        try:
            id1lat = [loc.split(',', 1)[0] for loc in idToLocationshigh[id1]]
            id1lon = [loc.split(',', 1)[1] for loc in idToLocationshigh[id1]]
            id2lat = [loc.split(',', 1)[0] for loc in idToLocationshigh[id2]]
            id2lon = [loc.split(',', 1)[1] for loc in idToLocationshigh[id2]]
        except:
            continue
        for x in id1lat:
            for y in id2lat:
                dlat = (float(x) - float(y))
                for a in id1lon:
                    for b in id2lon:
                        dlon = (float(a)-float(b))
                        # Haversine formula
                        z = sin(radians(dlat) / 2) ** 2 + cos(radians(float(x))) * cos(radians(float(y))) * sin(
                            radians(dlon) / 2) ** 2
                        c = 2 * asin(sqrt(z))
                        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
                        distance = c*r
                        distanceset = set()
                        distanceset.add(c*r)
        if min(distanceset) < 20:
            #print('Comparing', id1, 'with', id2)
            #print('The coordinates are nearby')
            if id1 != id2:
                print(id1, 'and', id2, 'are nearby (high resolution)', file = output)

#Low Resolution Location Comparisons
idToLocationslow ={};
#print('********Low Resolution Location Comparisons********', file=output)
with open(filename2, 'r', encoding='UTF-8') as f:
    for line in f:
        row = line.split('|')
        lowresloc = row[8]
        l = lowresloc.strip('*').strip('"').strip('.').split('~')
        #print(l)
        #print(l1)
        try:
            idToLocationslow[row[0]].append(l)
        except:
            idToLocationslow[row[0]]=l;
#print(idToLocations)
for id1 in idToLocationslow:
    for id2 in idToLocationslow:
        id1lat = [loc.split(',', 1)[0] for loc in idToLocationslow[id1]]
        id1lon = [loc.split(',', 1)[1] for loc in idToLocationslow[id1]]
        id2lat = [loc.split(',', 1)[0] for loc in idToLocationslow[id2]]
        id2lon = [loc.split(',', 1)[1] for loc in idToLocationslow[id2]]
        for x in id1lat:
            for y in id2lat:
                dlat = (float(x) - float(y))
                for a in id1lon:
                    for b in id2lon:
                        dlon = (float(a)-float(b))
                        # Haversine formula
                        z = sin(radians(dlat) / 2) ** 2 + cos(radians(float(x))) * cos(radians(float(y))) * sin(
                            radians(dlon) / 2) ** 2
                        c = 2 * asin(sqrt(z))
                        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
                        distance = c*r
                        distanceset = set()
                        distanceset.add(c*r)
        if min(distanceset) < 20:
            #print('Comparing', id1, 'with', id2)
            #print('The coordinates are nearby')
            if id1 != id2:
                print(id1,'and', id2, 'are nearby (low resolution)', file = output)

#High Resolution Location Comparisons
highreslastnames = [];
highresfirstnamemis = []
with open(filename2, 'r', encoding='UTF-8') as f:
    for line in f:
        try:
            row = line.split('|')
            highresname = row[4]
            hrname = highresname.strip('*').strip('"').strip('.').split(',')
            hrfnmi = [''.join(hrname[1:])]
            highresfirstnamemis.append(hrfnmi)
            highreslastnames.append(hrname[0])
            #print(highresfirstnamemis)

        except:
            print('pass')
            
#Finding Matching Low Resolution Names
lowreslastnames =[]
lowresfirstnamemis = []
with open(filename2, 'r', encoding='UTF-8') as f:
    for line in f:
        try:
            row = line.split('|')
            lowresname = row[5]
            x = lowresname.strip('*').strip('"').strip('.').split('~')
            y = [i.strip('*').strip('"').split(',', 1)[0] for i in x]
            z = [i.strip('*').strip('"').split(',', 1)[1] for i in x]
            #print(z)
            lowreslastnames.append(y)
            lowresfirstnamemis.append(z)
        except:
            print('pass')

#Cleaning the output file
i = list()
with open(filename5, 'w+', encoding='UTF-8') as output:
    for line in output:
        i.append(line.strip()  )
i.sort()
with open(filename6, 'w') as outputcleaned:
    for l in i:
        outputcleaned.write(l + '\n')
    # Naming output
    print('********List of Last Names and First Name/Middle Initials for IDs********', file=outputcleaned)
    print('High Resolution Last Names', file=outputcleaned)
    print(highreslastnames, file=outputcleaned)
    print('High Resolution First Names/Middle Initials', file=outputcleaned)
    print(highresfirstnamemis, file=outputcleaned)
    print('Low Resolution Last Names', file=outputcleaned)
    print(lowreslastnames, file=outputcleaned)
    print('Low Resolution First Names/Middle Initials', file=outputcleaned)
    print(lowresfirstnamemis, file=outputcleaned)