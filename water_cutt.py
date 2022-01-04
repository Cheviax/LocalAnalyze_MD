#for .gro file

x_or = 1                   # change: 1
y_or = 1                   # change: 1
z_or = 1                   # change: 1

num_add  = 5760
x_change = 0
y_change = 0
z_change = 0
x_set    = 0
y_set    = 0
z_set    = 3

js       = 3
sol      = 6
with open('gro_water.txt','r') as f:
    dogs = f.readlines()

for dog in dogs:
    dog_1 = dog[0:15]
    dog_2 = dog[15:]
    doge  = dog_1.split() + dog_2.split()
    out   = ''
    if js == 3 :
        sol += 1
        js   = 0

#dogs.old
    cat_01 = doge[0]
    cat_02 = doge[1]
    cat_03 = doge[2]
    cat_04 = doge[3]
    cat_05 = doge[4]
    cat_06 = doge[5]

# assignment
    line_1 = str(sol) + 'SOL'        # residue name
    line_2 = cat_02         # atom
     # atom number
    line_4 = cat_04        # x
    line_5 = cat_05        # y
    line_6 = cat_06        # z

# length of line
    le_1 = len(line_1)
    le_2 = len(line_2)

    le_4 = len(line_4)
    le_5 = len(line_5)
    le_6 = len(line_6)

# write
    if float(line_6) < 5.88:
        num_add += 1
        line_3 = str(num_add)
        le_3 = len(line_3)
        k = 0
        js += 1
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
        with open('gro_write.txt','a') as f:
            f.write(out)
            f.write('\n')
'''
    elif float(line_4) > 10.09:
        num_add += 1
        line_3 = str(num_add)
        le_3 = len(line_3)
        k = 0
        js += 1
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
        with open('gro_write.txt','a') as f:
            f.write(out)
            f.write('\n')

    elif float(line_6) > 1.495:
        if float(line_6) < 2.495:
            num_add += 1
            line_3 = str(num_add)
            le_3 = len(line_3)
            k = 0
            js += 1
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
            with open('gro_write.txt','a') as f:
                f.write(out)
                f.write('\n')
'''