import math

with open('pab.txt','r') as f:
    dogs = f.readlines()


xx = []
yy = []
zz = []

for dog in dogs:
    doge = dog.split()

    cat_02 = doge[2]
    cat_03 = doge[1]
    cat_04 = float(doge[5]) / 10
    cat_05 = float(doge[6]) / 10
    cat_06 = float(doge[7]) / 10

    xx.append(float(cat_04))
    yy.append(float(cat_05))
    zz.append(float(cat_06))


for i in range(9):
    x = xx[i]
    y = yy[i]
    z = zz[i]
    list = []
    for j in range(9):
        dx = x - xx[j]
        dy = y - yy[j]
        dz = z - zz[j]
        d2 = dx*dx + dy*dy + dz*dz
        d  = math.sqrt(d2)
        list.append('%.3f' % d)
    list_up = sorted(list)
    print(list_up)

