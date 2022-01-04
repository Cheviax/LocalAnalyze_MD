with open('pdb_1.txt','r') as f:
    dogs = f.readlines()

for dog in dogs:
    doge = dog.split()
    out  = ''

#dogs.old
    cat_01 = '2N12'
    cat_02 = doge[2]
    cat_03 = doge[1]
    cat_04 = float(doge[6]) / 10
    cat_05 = float(doge[7]) / 10
    cat_06 = float(doge[8]) / 10

# assignment
    line_1 = cat_01        # residue name
    line_2 = cat_02        # atom
    line_3 = cat_03        # atom number
    line_4 = str("%.3f" % cat_04)        # x
    line_5 = str("%.3f" % cat_05)        # y
    line_6 = str("%.3f" % cat_06)        # z

# length of line
    le_1 = len(line_1)
    le_2 = len(line_2)
    le_3 = len(line_3)
    le_4 = len(line_4)
    le_5 = len(line_5)
    le_6 = len(line_6)

# write
    k = 0
    while k < 8 - le_1:
        out += ' '
        k = k + 1
    out += line_1
    k = 0
    while k < 7 - le_2:
        out += ' '
        k = k + 1
    out += line_2
    k = 0
    while k < 5 - le_3:
        out += ' '
        k = k + 1
    out += line_3
    k = 0
    while k < 8 - le_4:
        out += ' '
        k = k + 1
    out += line_4
    k = 0
    while k < 8 - le_5:
        out += ' '
        k = k + 1
    out += line_5
    k = 0
    while k < 8 - le_6:
        out += ' '
        k = k + 1
    out += line_6

    print(out)