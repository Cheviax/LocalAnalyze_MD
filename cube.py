names = locals()

drct = 'H:/GMX_OUT/tube/new_22/tube_new'
name = '/cl_'
wrt_l = open('H:/GMX_OUT/tube/cl_22_la.txt', 'w')
wrt_u = open('H:/GMX_OUT/tube/cl_22_ua.txt', 'w')

zhen = 5000
z1l = 2.05
z1u = 3.89
z2l = 9.05
z2u = 10.89
rr1 = [2.5, 2.5]
rr2 = [2.5, 2.5]
d = 2.5
count_l = 0
count_u = 0

for i in range(100):
    names['d_' + str(i+1)] = (d / 100) * (i + 1)
    names['n_l_' + str(i+1)] = 0
    names['n_u_' + str(i + 1)] = 0

for z in range(zhen):
    print(z)
    red = open(drct + name + str(z+1) + '.gro', 'r')
    lines = red.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]

    for line in lines:

        ls_5 = line[21:28]
        ls_6 = line[29:36]
        ls_7 = line[37:44]

        li_x = float(ls_5)
        li_y = float(ls_6)
        li_z = float(ls_7)

        if (li_z >= z1l) and (li_z <= z1u):
            r2 = (li_x - rr1[0]) ** 2 + (li_y - rr1[1]) ** 2
            r = r2 ** 0.5
            for j in range(100):
                if r <= names['d_' + str(j + 1)]:
                    names['n_l_' + str(j + 1)] += 1
                    count_l += 1
                    break

        if (li_z >= z2l) and (li_z <= z2u):
            r2 = (li_x - rr2[0]) ** 2 + (li_y - rr2[1]) ** 2
            r = r2 ** 0.5
            for j in range(100):
                if r <= names['d_' + str(j + 1)]:
                    names['n_u_' + str(j + 1)] += 1
                    count_u += 1
                    break

for i in range(100):
    names['n_l_' + str(i + 1)] = names['n_l_' + str(i + 1)] / zhen
    wrt_l.write(str(names['n_l_' + str(i + 1)]))
    wrt_l.write('\n')

    names['n_u_' + str(i + 1)] = names['n_u_' + str(i + 1)] / zhen
    wrt_u.write(str(names['n_u_' + str(i + 1)]))
    wrt_u.write('\n')
