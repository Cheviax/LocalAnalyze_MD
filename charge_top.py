# for .top file
names = locals()

with open('top.txt', 'r') as f:
    dogs = f.readlines()

a = 0
le_set_1 = 6
le_set_2 = 11
le_set_3 = 7
le_set_4 = 7
le_set_5 = 7
le_set_6 = 7
le_set_7 = 11
le_set_8 = 11

line_count = 0
chargee    = 0
for dog in dogs:
    doge = dog.split()
    out = ''
    line_count += 1

    if line_count == 4:
        line_count = 0
    # dogs.old
    for i in range(8):
        names['line_' + str(i+1)] = doge[i]

    # assignment
    if float(line_3) == 2:
        line_7 = -0.015
        chargee += 1

    if float(chargee) == 24:
        line_7 = -0.005
        chargee = 0
# length of line
    for i in range(8):
        names['le_' + str(i+1)] = len(str(names['line_' + str(i+1)]))

# write
    for i in range(8):
        k = 0
        while k < names['le_set_' + str(i+1)] - names['le_' + str(i+1)]:
            out += ' '
            k   += 1
        out += str(names['line_' + str(i+1)])

# print
    print(out)
