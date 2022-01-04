names = locals()

drct = 'H:/GMX_OUT/tube/new_22/tube_new'
name1 = '/sol_'
name2 = '/ion_'
wrt_l = open(drct+'/aqua_l.txt', 'w')
wrt_u = open(drct+'/aqua_u.txt', 'w')

zhen = 50
z1l = 2.05
z1u = 3.89
z2l = 9.05
z2u = 10.89
rr1 = [2.5, 2.5]
rr2 = [2.5, 2.5]
d = 3
count_l = 0
count_u = 0
drif = 0.2
aqua_l = 0
aqua_u = 0

count_cl_li = 0
count_cl_ui = 0
count_cl_lo = 0
count_cl_uo = 0
count_sl_li = 0
count_sl_ui = 0
count_sl_lo = 0
count_sl_uo = 0



for z in range(zhen):
    print(z)

    sols_l = []
    sols_u = []
    nasl = []
    nasu = []
    clsl = []
    clsu = []

    cl_countl = 0
    cl_countu = 0
    cl_aqual = 0
    cl_aquau = 0

    red1 = open(drct + name1 + str(z+1) + '.gro', 'r')
    lines1 = red1.readlines()
    del lines1[0]
    del lines1[0]
    del lines1[-1]

    red2 = open(drct + name2 + str(z+1) + '.gro', 'r')
    lines2 = red2.readlines()
    del lines2[0]
    del lines2[0]
    del lines2[-1]

    for line1 in lines1:

        ls_name = line1[12:14]
        ls_5 = line1[21:28]
        ls_6 = line1[29:36]
        ls_7 = line1[37:44]

        li_x = float(ls_5)
        li_y = float(ls_6)
        li_z = float(ls_7)

        if ls_name == 'HW':
            if (li_z >= z1l) and (li_z <= z1u):
                r2 = (li_x - rr1[0]) ** 2 + (li_y - rr1[1]) ** 2
                r = r2 ** 0.5
                if r <= d / 2:
                    count_sl_li += 1
                    line_new = ls_5 + ' ' + ls_6 + ' ' + ls_7
                    sols_l.append(line_new)
                else:
                    count_sl_lo += 1

            if (li_z >= z2l) and (li_z <= z2u):
                r2 = (li_x - rr2[0]) ** 2 + (li_y - rr2[1]) ** 2
                r = r2 ** 0.5
                if r <= d / 2:
                    count_sl_ui += 1
                    line_new = ls_5 + ' ' + ls_6 + ' ' + ls_7
                    sols_u.append(line_new)
                else:
                    count_sl_uo += 1

    for line2 in lines2:

        ls_name = line2[13:15]
        ls_5 = line2[21:28]
        ls_6 = line2[29:36]
        ls_7 = line2[37:44]

        li_x = float(ls_5)
        li_y = float(ls_6)
        li_z = float(ls_7)

        if ls_name == 'CL':
            if (li_z >= z1l) and (li_z <= z1u):
                cl_countl += 1
                r2 = (li_x - rr1[0]) ** 2 + (li_y - rr1[1]) ** 2
                r = r2 ** 0.5
                if r <= d / 2:
                    count_cl_li += 1
                    for soli in sols_l:
                        solis = soli.split()
                        solx = float(solis[0])
                        soly = float(solis[1])
                        solz = float(solis[2])
                        dr2 = (li_x - solx) ** 2 + (li_y - soly) ** 2 + (li_z - solz) ** 2
                        if dr2 <= drif:
                            cl_aqual += 1
                else:
                    count_cl_lo += 1

            if (li_z >= z2l) and (li_z <= z2u):
                cl_countu += 1
                r2 = (li_x - rr1[0]) ** 2 + (li_y - rr1[1]) ** 2
                r = r2 ** 0.5
                if r <= d / 2:
                    count_cl_ui += 1
                    for soli in sols_u:
                        solis = soli.split()
                        solx = float(solis[0])
                        soly = float(solis[1])
                        solz = float(solis[2])
                        dr2 = (li_x - solx) ** 2 + (li_y - soly) ** 2 + (li_z - solz) ** 2
                        if dr2 <= drif:
                                cl_aquau += 1
                else:
                    count_cl_uo += 1

    aqual = cl_aqual/cl_countl/2
    aquau = cl_aquau/cl_countu/2
    aqua_l += aqual
    aqua_u += aquau

aqua_l = aqua_l / zhen
aqua_u = aqua_u / zhen
print(aqua_l)
print(aqua_u)

count_cl_li = count_cl_li / zhen
count_cl_ui = count_cl_ui / zhen
count_cl_lo = count_cl_lo / zhen
count_cl_uo = count_cl_uo / zhen
count_sl_li = count_sl_li / zhen
count_sl_ui = count_sl_ui / zhen
count_sl_lo = count_sl_lo / zhen
count_sl_uo = count_sl_uo / zhen
print(count_cl_li)
print(count_cl_ui)
print(count_cl_lo)
print(count_cl_uo)
print(count_sl_li)
print(count_sl_ui)
print(count_sl_lo)
print(count_sl_uo)

