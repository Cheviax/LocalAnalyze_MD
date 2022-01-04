import math
from hanshu import water_angle
names = locals()

orr = 0
orrr = 0
orrrr = 0
count = 0
angle_1 = 0
ang_1_all = 0
angle_2 = 0
ang_2_all = 0
angle_3 = 0
ang_3_all = 0
ang_1 = 0
ang_2 = 0
ang_3 = 0

for i in range(360):
    names['ag_1_' + str(i + 1)] = 0
    names['ag_2_' + str(i + 1)] = 0
    names['ag_3_' + str(i + 1)] = 0
    names['ag_or_' + str(i+1)] = (i - 179.5) / 180 * math.pi
  #  print(names['ag_or_' + str(i+1)])


for i in range(5000):
    print(str(i+1))

    orr = 0
    orrr = 0
    orrrr = 0

    angle_1 = 0
    ang_1_all = 0
    angle_2 = 0
    ang_2_all = 0
    angle_3 = 0
    ang_3_all = 0

    o = []
    m = []
    oo = []
    ww = []
    ooo = []
    www = []

    drct = 'H:/GMX_OUT/JIANG/CO2_NEW/e16/13/gro_'
    name = drct + str(i+1) + '.gro'
    f = open(name, 'r')
    f_l = f.readlines()
    del f_l[0]
    del f_l[0]
    del f_l[-1]
    for line in f_l:

        ls = line.split()
        if ls[1] == 'OW':
            if float(ls[5]) >= 0.41:
                if float(ls[5]) <= 1.41:
                    orr = 1
                    orrr = 1
                    orrrr = 1
                    o.append(float(ls[3]))
                    o.append(float(ls[4]))
                    o.append(float(ls[5]))

        if ls[1] == 'MW':
            if orr == 1:
                m.append(float(ls[3]))
                m.append(float(ls[4]))
                m.append(float(ls[5]))
                orr = 0
                count += 1
                tant = water_angle(o, m)
                angle_1 = math.atan(tant)
     #           ang_1_all += angle_1
                o = []
                m = []
                for j in range(360):
                    if angle_1 <= names['ag_or_' + str(j+1)]:
                        names['ag_1_' + str(j + 1)] += 1
                        break


        if ls[1] == 'HW1':
            if orrr == 1:
                ww.append(float(ls[3]))
                ww.append(float(ls[4]))
                ww.append(float(ls[5]))
                orrr = 0
                tant = water_angle(o, ww)
                angle_2 = math.atan(tant)
       #         ang_2_all += angle_2
                ww = []

        if ls[1] == 'HW2':
            if orrrr == 1:
                www.append(float(ls[3]))
                www.append(float(ls[4]))
                www.append(float(ls[5]))
                orrrr = 0
                tant = water_angle(o, www)
                angle_3 = math.atan(tant)
       #         ang_3_all += angle_3
                www = []

                if angle_2 > angle_3:
                    for j in range(360):
                        if angle_3 <= names['ag_or_' + str(j + 1)]:
                            names['ag_3_' + str(j + 1)] += 1
                            break
                    for j in range(360):
                        if angle_2 <= names['ag_or_' + str(j + 1)]:
                            names['ag_2_' + str(j + 1)] += 1
                            break

                else:
                    for j in range(360):
                        if angle_2 <= names['ag_or_' + str(j + 1)]:
                            names['ag_3_' + str(j + 1)] += 1
                            break
                    for j in range(360):
                        if angle_3 <= names['ag_or_' + str(j + 1)]:
                            names['ag_2_' + str(j + 1)] += 1
                            break

print('-------')

wrt = open('wat_ang_16_13.txt', 'w')

ang_in_one_1 = 0
ang_in_one_2 = 0
ang_in_one_3 = 0

for i in range(360):
    names['ag_1_' + str(i + 1)] = names['ag_1_' + str(i + 1)] / count
    names['ag_2_' + str(i + 1)] = names['ag_2_' + str(i + 1)] / count
    names['ag_3_' + str(i + 1)] = names['ag_3_' + str(i + 1)] / count
    line_nn = str(names['ag_1_' + str(i + 1)]) + ' ' + str(names['ag_2_' + str(i + 1)]) + ' ' + str(names['ag_3_' + str(i + 1)])
    ang_in_one_1 += names['ag_1_' + str(i + 1)] * names['ag_or_' + str(i+1)] / math.pi * 180
    ang_in_one_2 += names['ag_2_' + str(i + 1)] * names['ag_or_' + str(i+1)] / math.pi * 180
    ang_in_one_3 += names['ag_3_' + str(i + 1)] * names['ag_or_' + str(i+1)] / math.pi * 180
    wrt.write(line_nn)
    wrt.write('\n')

print(ang_in_one_1)
print(ang_in_one_2)
print(ang_in_one_3)




