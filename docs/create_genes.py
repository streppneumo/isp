
import csv
import sys

with open(sys.argv[1], 'r') as infile:
   for _ in range(3):
      infile.next()
   reader = csv.reader(infile, delimiter="\t")
   for row in reader:
      print '{g} = Gene("{g}")'.format(g=row[5])
      if row[4] != '-':
         print '{abbrev} = {g}'.format(abbrev=row[4], g=row[5])




