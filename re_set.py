with open('gro_1.txt','r') as f:
    dogs = f.readlines()

line_num = 0
x = 0
y = 0
z = 0
count = 0
sol = 2

for dog in dogs:
    out  = ''
    count += 1
    line_num += 1
    sol += 0

#dogs.old
    ds = dog.split()
    cat_01 = '1Wl'
    cat_02 = ds[1]
    cat_03 = ds[2]
    cat_04 = float(ds[3]) + 0
    cat_05 = float(ds[4]) + 2
    cat_06 = float(ds[5]) - 8

    cat_01 = str(cat_01)
    out = '    ' + str(cat_01) + '      '\
          + str(cat_02) +'  '+ str(cat_03) + '   '\
          + str('%.3f' % cat_04) + '   ' + str('%.3f' % cat_05) + '   '\
          + str('%.3f' % cat_06)
    print(out)

'''    
    if cat_07 == 0.2:
        cat_01 = 1
    if cat_07 == 0.404:
        cat_01 = 2
    if cat_07 == 9.596:
        cat_01 = 3
    if cat_07 == 9.8:
        cat_01 = 4
        '''

'''
# assignment
    line_1 = cat_01        # residue name
    line_2 = cat_02        # atom
    line_3 = str(cat_03)        # atom number
    line_4 = str('%.3f'% cat_04)        # x
    line_5 = str('%.3f'% cat_05)        # y
    line_6 = str('%.3f'% cat_06)        # z

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

    print(out)'''