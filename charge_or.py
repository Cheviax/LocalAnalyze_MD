#for .gro file

x_or = 1                   # change: 1
y_or = 1                   # change: 1
z_or = 1                   # change: 1

num_add  = 0
x_change = 0
y_change = 0
z_change = 0
x_set    = 0
y_set    = 0
z_set    = 3.485

ornot    = 0

with open('gro.txt','r') as f:
    dogs = f.readlines()

for dog in dogs:
    doge = dog.split()
    out  = ''
    num_add += 1

#dogs.old
    cat_01 = doge[0]
    cat_02 = doge[1]
    cat_03 = doge[2]
    cat_04 = doge[3]
    cat_05 = doge[4]
    cat_06 = doge[5]

#dogs.change
    cat_11 = '2GRA'
    cat_12 = 'C'
    cat_13 = str(num_add)
    if x_or == 1:
        cat_14 = str('%.3f' % (float(cat_04) + x_change))
    else:
        cat_14 = str('%.3f' % x_set)
    if y_or == 1:
        cat_15 = str('%.3f' % (float(cat_05) + y_change))
    else:
        cat_15 = str(y_set)
    if z_or == 1:
        cat_16 = str('%.3f' % (float(cat_06) + z_change))
    else:
        cat_16 = str(z_set)

# assignment
    line_1 = cat_11        # residue name
    line_2 = cat_02        # atom
    line_3 = cat_13        # atom number
    line_4 = cat_14        # x
    line_5 = cat_15        # y
    line_6 = cat_16        # z

# length of line
    le_1 = len(line_1)
    le_2 = len(line_2)
    le_3 = len(line_3)
    le_4 = len(line_4)
    le_5 = len(line_5)
    le_6 = len(line_6)

# write
    if float(line_4) > 6.9:
        if float(line_4) < 8.19:
            out += line_3
            print(out)


