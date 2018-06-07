r1 = "eNB"
r2 = "MME"
r3 = "HSS"
r4 = "SGW"
lines = 0
print ("{0:-<15}{1:-<15}{2:-<15}{3}".format(r1,r2,r3,r4))

while lines < 5:
    print ("{0:<15}{0:<15}{0:<15}{0}".format('|'))
    lines +=1
print ("{0:-<15}{0:-<15}{0:-<15}{0}".format('+'))
