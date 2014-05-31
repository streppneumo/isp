
from BeautifulSoup import BeautifulSoup


soup = BeautifulSoup(open('comp-genomics.html'))

order = ["bsu", "eco", "pao", "spn"]
print ",".join([x+"_id,"+x+"_desc" for x in order])

table = soup('table')[27]
for row in table.findAll('tr')[1:]:
    cells = row.findAll('td')
    s = ""
    for i in range(len(order)):
        if cells[i+1].a:
            s += '"' + cells[i+1].contents[1].string + '",'
            s += ('"' +
                  cells[i+1].contents[2].strip()[1:-1].replace('"', "'") +
                  '",')
        else:
            s += "NA,NA,"
    print s[0:-1].encode("utf8")





