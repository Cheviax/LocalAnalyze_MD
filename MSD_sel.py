# for .gro file
# gmx trjconv -f nvt -s nvt -o gro_.gro -b 30000 -e 40000 -tu ps -sep -timestep 1 -pbc whole
from hanshu import msd_xyz, sel_z, sel_num

names = locals()

direction = 'Z'
frame_num = 3890
file_name = '\co2_b_'
file_type = '.gro'
drct = 'H:/GMX_OUT/JIANG/CO2_NEW/e16/e11'
wrt = open('F:/PyProject/gmx/MSD/jiang/msd_co2_16_11', 'w')
name = '  C1'

x_min = 0
x_max = 0
y_min = 0
y_max = 0
z_min = 0.41
z_max = 5.41

B_NUM = []
B_ZZZ = []
E_NUM = []
E_ZZZ = []
msdi = 0
MSD_ALL = []



for i in range(frame_num):
    frame_b = i + 0
    frame_e = i + 1
    red_b = open(drct + file_name + str(frame_b) + file_type, 'r')
    red_e = open(drct + file_name + str(frame_e) + file_type, 'r')
    lines_b = red_b.readlines()
    lines_e = red_e.readlines()

    del lines_b[0]
    del lines_b[0]
    del lines_b[-1]
    del lines_e[0]
    del lines_e[0]
    del lines_e[-1]

    BBB = sel_z(lines_b, z_min, z_max, name)
    B_NUM = BBB[0]
    B_XXX = BBB[1]
    B_YYY = BBB[2]
    B_ZZZ = BBB[3]
    EEE = sel_num(lines_e, B_NUM)
    E_XXX = EEE[0]
    E_YYY = EEE[1]
    E_ZZZ = EEE[2]

    msd = 0
    count = 0
    for li in range(len(B_NUM)):
        xb = B_XXX[li]
        yb = B_YYY[li]
        zb = B_ZZZ[li]
        xe = E_XXX[li]
        ye = E_YYY[li]
        ze = E_ZZZ[li]
        msd += msd_xyz(xb, yb, zb, xe, ye, ze)
        count += 1
    msd = msd /count
    msdi += msd
    MSD_ALL.append(msdi)
    print(str(i+1))


for msdi in MSD_ALL:
    wrt.write(str(msdi))
    wrt.write('\n')




