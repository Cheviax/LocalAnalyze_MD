names = locals()

drct_1 = 'H:\GMX_OUT\JIANG\er_done\er'
name = '\co2.xvg'
num = 0
wrt = open('dens2tot.txt', 'w')
mole_all = 1220

for i in range(1000):
    names['lan_' + str(i+1)] = ''
    names['len_' + str(i+1)] = ''
    names['max_' + str(i+1)] = 0

for i in ['0', '1', '8', '00', '05', '08', '11', '15', '20']:

    drct_2 = i

    f = open(drct_1 + drct_2 + name, 'r')
    lines = f.readlines()
    lines = lines[24:]

    count = 0
    if num == 0:
        ct_0 = 0
        for line in lines:
            ls = line.split()
            ct_0 += 1
            zzz = (8.825 - float(ls[0])) * 10
            names['lan_' + str(ct_0)] += ' ' + str(zzz)
        num = 1

    num_wat = 0
    ct_1 = 0
    for line in lines:
        ls = line.split()
        ct_1 += 1
        num_wat += float(ls[1])
        names['lan_' + str(ct_1)] += ' ' + ls[1]
        names['len_' + str(ct_1)] += ' ' + str(num_wat)




for i in range(1000):
    line_new = names['lan_' + str(i+1)] + '  ' + names['len_' + str(i+1)]
    wrt.write(line_new)
    wrt.write('\n')
    print(line_new)


'''
drct = 'H:\GMX_OUT\GONG\done\er14\wat_'
name = 'dens.xvg'
f = open(drct + name, 'r')
lines = f.readlines()
lines = lines[24:]

vol_begin = 0

for line in lines:
    ls = line.split()
    vol_begin += float(ls[1])
    line_new = ls[0] + '  ' + str(vol_begin)
    print(line_new)
'''