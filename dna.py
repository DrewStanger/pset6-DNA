from sys import argv, exit
import itertools
import csv
import re
# STR count to count number of consec repeats
# check if there are 2 CMA
if len(argv) != 3:
    print(f"Error there should be 2 argv, you have {argv}")
    exit(1)
# Open CSV and read to mem
with open(argv[1],"r") as inputfile:
    #reader = csv.DictReader(inputfile)
    reader = list(csv.reader(inputfile))
    reader[0].remove("name")
    i = reader[0]
#Open Sequence TXT
with open(argv[2],"r") as sequence:
    data = sequence.read()
#need to comapre CSV and DNA with while loops?
# i is a list of AGATC, AATG, TATC (or any other sequence)
# for each sequence
valuelist = []
for q in range(len(i)): #i = 3
    maxcounter = 0
    counter = 0
    position = 0
    previouspos = 0
    # while the dna sequence has not been fully worked through do the following.
    while position < len(data):
        # this gives the position at which the sequence is found
        position = data.find(i[q], position)
        if position == -1: # i.e not found...
            counter = 0
            break
        # if not -1 then it has been found and if position - the length of the sequence is also equal to - 1, it is a consequtive value?
        elif (position != -1) and previouspos == 0:
            counter += 1
            maxcounter = counter
            previouspos = position
        elif (position != -1) and ((position - len(i[q])) == previouspos):
            counter += 1
            previouspos = position
            if maxcounter < counter:
                maxcounter = counter
        elif (position != -1) and ((position - len(i[q])) != previouspos):
            counter = 1
            previouspos = position
            if maxcounter < counter:
                maxcounter = counter
        position += 1
    valuelist.append(maxcounter)
#now to figure out how to store them and compare to people.
#update the list to bea list of strings to enable comparison.
valuelist = list(map(str, valuelist))
#make a new list to preserve reader
cleaned = list(reader)
cleaned.pop(0)
#compare valuelist to reader
for person in cleaned:
    if person[1:] == valuelist:
        print(f"{person[0]}")
        break
    elif person == cleaned[-1]:
        print("No match")