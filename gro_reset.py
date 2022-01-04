red = open('gro_1.txt', 'r')
# del brfore use
wrt = open('gro_re.txt', 'w')

lines = red.readlines()

atom = 784
molee = 1
orr = -1

for line in lines:
    atom += 1
    orr += 1

    ls = line.split()
    mole = line[0:9]
    mole1 = mole[0:5]
    num = int(mole1)
    num += molee
    num = str(num)
    mole2 = mole[5:8]
    nam_m = mole2

    nam_a = ls[1]



    num_a = str(atom)

    xxx = ls[3]
    xxx = float(xxx)
    xxx = xxx + 0
    xxx = str('%.3f' % xxx)

    yyy = ls[4]
    yyy = float(yyy)
    yyy = yyy + 0
    yyy = str('%.3f' % yyy)

    zzz = ls[5]
    zzz = float(zzz)
    zzz = 12 - zzz
    zzz = str('%.3f' % zzz)

    name_a = ''

    spc1 = 5 - len(num)
    spc2 = 7 - len(nam_a)
    spc3 = 5 - len(num_a)
    spc4 = 8 - len(xxx)
    spc5 = 8 - len(yyy)
    spc6 = 8 - len(zzz)

    line_new = ''
    for i in range(spc1):
        line_new += ' '
    line_new += num
    line_new += nam_m
    for i in range(spc2):
        line_new += ' '
    line_new += nam_a
    for i in range(spc3):
        line_new += ' '
    line_new += num_a
    for i in range(spc4):
        line_new += ' '
    line_new += xxx
    for i in range(spc5):
        line_new += ' '
    line_new += yyy
    for i in range(spc6):
        line_new += ' '
    line_new += zzz

    line_new += name_a
    print(line_new)
    wrt.write(line_new)
    wrt.write('\n')