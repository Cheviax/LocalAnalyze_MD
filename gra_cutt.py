red = open('gro_1.txt', 'r')
# del brfore use
wrt = open('gro_re.txt', 'w')

lines = red.readlines()

num = 71
if3 = -1
num_a = 636

for line in lines:
    ls = line.split()
    mole = line[0:9]
    mole2 = mole[5:8]
    nam_m = mole2

    nam_a = ls[1]

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
    zzz = zzz + 0

    if (zzz > 0.5) and (zzz < 8.8):
        if3 += 1
        num_a = int(num_a)
        num_a += 1
        num_a = str(num_a)
        num = int(num)
        if if3 == 3:
            num += 1
            if3 = 0
        num = str(num)
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


