import math
from hanshu import water_angle
names = locals()

zb = 0.41
ze = 1.91
zd = ze - zb
zhen = 5000
drct = 'H:/GMX_OUT/JIANG/CO2_NEW/none/11/gro_'

for i in range(100):
    names['h_' + str(i + 1)] = 0
    names['o_' + str(i + 1)] = 0
    names['or_' + str(i + 1)] = zb + zd / 100 * (i + 1)

  #  print(names['ag_or_' + str(i+1)])


for i in range(zhen):
    print(str(i+1))

    name = drct + str(i+1) + '.gro'
    f = open(name, 'r')
    f_l = f.readlines()
    del f_l[0]
    del f_l[0]
    del f_l[-1]

    for line in f_l:
        ls_1 = line[0:5]
        ls_2 = line[5:10]
        ls_3 = line[11:15]
        ls_4 = line[15:20]
        ls_5 = line[21:28]
        ls_6 = line[29:36]
        ls_7 = line[37:44]

        if float(ls_7) <= ze:
            for j in range(100):
                if float(ls_7) <= names['or_' + str(j + 1)]:
                    if ls_3 == ' HW1' or ls_3 == ' HW2':
                        names['h_' + str(j + 1)] += 1
                    elif ls_3 == '  OW':
                        names['o_' + str(j + 1)] += 1
                    break

wrt_h = open(drct + 'o.txt', 'w')
wrt_o = open(drct + 'h.txt', 'w')

for i in range(100):
    names['h_' + str(i + 1)] = names['h_' + str(i + 1)] / zhen
    names['o_' + str(i + 1)] = names['o_' + str(i + 1)] / zhen
    wrt_h.write(str(names['h_' + str(i + 1)]))
    wrt_h.write('\n')
    wrt_o.write(str(names['o_' + str(i + 1)]))
    wrt_o.write('\n')




