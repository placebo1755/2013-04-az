import sys
import screed
filename=sys.argv[1]
print filename
for record in screed.open(filename):
    print record
    break
