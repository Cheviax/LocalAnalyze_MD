#for .top file

charge_or     = 2           # change: 1
cgnr_or       = 1           # change: 1

charge_change = 0
cgnr_change   = 0
charge_set    = 0.00625
cgnr_set      = 0

a = 0

with open('top.txt','r') as f:
    dogs = f.readlines()

for dog in dogs:
    doge = dog.split()
    out = ''

#dogs.old
    line_1 = doge[0]        #atom number
    line_2 = doge[1]        #atom type
    line_3 = doge[2]        #residue number
    line_4 = doge[3]        #residue name
    line_5 = doge[4]        #atom
    cat_6  = doge[5]
    cat_7  = doge[6]
    line_8 = doge[7]        #mass

#assignment
    if cgnr_or == 1:
        line_6 = str('%.0f' % (float(cat_6) + charge_change))
    else:
        line_6 = str(charge_set)

    if charge_or   == 1:
        line_7 = str('%.3f' % (float(cat_7) + cgnr_change))
    else :
        line_7 = str(cgnr_set)

    line_7 = str(0.00625)


#length of line
    le_1 = len(line_1)
    le_2 = len(line_2)
    le_3 = len(line_3)
    le_4 = len(line_4)
    le_5 = len(line_5)
    le_6 = len(line_6)
    le_7 = len(line_7)
    le_8 = len(line_8)

#write
    k = 0
    while k < 6 - le_1:
        out += ' '
        k = k + 1
    out += line_1

    k = 0
    while k < 11 - le_2:
        out += ' '
        k = k + 1
    out += line_2

    k = 0
    while k < 7 - le_3:
        out += ' '
        k = k + 1
    out += line_3

    k = 0
    while k < 7 - le_4:
        out += ' '
        k = k + 1
    out += line_4

    k = 0
    while k < 7 - le_5:
        out += ' '
        k = k + 1
    out += line_5

    k = 0
    while k < 7 - le_6:
        out += ' '
        k = k + 1
    out += line_6

    k = 0
    while k < 11 - le_7:
        out += ' '
        k = k + 1
    out += line_7

    k = 0
    while k < 11 - le_8:
        out += ' '
        k = k + 1
    out += line_8

#print
    print(out)

print(a)