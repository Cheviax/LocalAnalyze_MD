names = locals()

drct_1 = 'H:\GMX_OUT\JIANG\er_done\er'
name = '\co2.xvg'
num = 0
wrt = open('densin1.txt', 'w')
for i in range(1000):
    names['lan_' + str(i+1)] = ''

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
            zzz = (float(ls[0]) - 0.559) * 10
            names['lan_' + str(ct_0)] += ' ' + str(zzz)
        num = 1

    ct_1 = 0
    for line in lines:.

        ls = line.split()
        ct_1 += 1
        names['lan_' + str(ct_1)] += ' ' + ls[1]

for i in range(1000):
    wrt.write(names['lan_' + str(i+1)])
    wrt.write('\n')
    print(names['lan_' + str(i+1)])
