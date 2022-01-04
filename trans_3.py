#for .gro file

with open('gro.txt','r') as f:
    dogs = f.readlines()

num = 1464

for dog in dogs:
    doge = dog.split()
    out = ''
    num += 1

#dogs.old
    cat_1 = doge[0]
    cat_2 = doge[1]
    cat_3 = doge[2]
    cat_4 = doge[3]
    cat_5 = doge[4]
    cat_6 = doge[5]

# assignment
    line_1 = '2GRA'  # residue name
    line_2 = cat_2  # atom
    line_3 = str(num)
    line_4 = cat_4  # x
    line_5 = cat_5  # y
    line_6 = str('4.403')  # z

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
    while k < 8 - le_6:
        out += ' '
        k = k + 1
    out += line_6

    k = 0
    while k < 8 - le_5:
        out += ' '
        k = k + 1
    out += line_5

    k = 0
    while k < 8 - le_4:
        out += ' '
        k = k + 1
    out += line_4

    print(out)