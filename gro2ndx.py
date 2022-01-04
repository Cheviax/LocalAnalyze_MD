import os
names = locals()

os.remove('ndx.txt')
os.remove('ndx_new.txt')
with open('sol.txt','r') as f:
    dogs = f.readlines()
wrt = open('ndx.txt', 'a')

for i in range(88):
    names['select' + str(i + 1)] = []
    names['Z' + str(i + 1)] = []
    names['Z_o' + str(i + 1)] = []

for dog in dogs:
    dog_1 = dog[0:15]
    dog_2 = dog[15:]
    doge  = dog_1.split() + dog_2.split()
    out   = ''

#dogs.old
    cat_01 = doge[0]
    cat_02 = doge[1]
    cat_03 = doge[2]
    cat_04 = doge[3]
    cat_05 = doge[4]
    cat_06 = doge[5]

    if len(cat_02) == 2:
        for i in range(88):
            zl_l = 0.525 + i * 0.05
            zr_l = 0.625 + i * 0.05
            zl_u = 9.375 - i * 0.05
            zr_u = 9.475 - i * 0.05
            if (float(cat_06) >= zl_l and float(cat_06) < zr_l) \
                    or (float(cat_06) > zl_u and float(cat_06) <= zr_u):
                names['select' + str(i + 1)].append(cat_01)

for dog in dogs:
    dog_1 = dog[0:15]
    dog_2 = dog[15:]
    doge = dog_1.split() + dog_2.split()
    out = ''

    # dogs.old
    cat_01 = doge[0]
    cat_02 = doge[1]
    cat_03 = doge[2]
    cat_04 = doge[3]
    cat_05 = doge[4]
    cat_06 = doge[5]

    for i in range(88):
        if cat_01 in names['select' + str(i + 1)]:
            names['Z' + str(i + 1)].append(cat_03)
        else:
            names['Z_o' + str(i + 1)].append(cat_03)

num = []

for i in range(88):
   # print('[ WT' + str(i+1) + ' ]')
 #   for i in names['Z' + str(i + 1)]:
    print(len(names['Z' + str(i + 1)]))
    num.append(len(names['Z' + str(i + 1)]))
   # print(len(names['Z_o' + str(i + 1)]))


    count = 0
    wrt.write('\n[ WT' + str(i+1) + ' ]\n')

    for j in names['Z' + str(i + 1)]:
        count += 1
        wrt.write(str(int(j)) + ' ')
        if count == 15:
            wrt.write('\n')
            count = 0

    count = 0
    wrt.write('\n[ WC' + str(i + 1) + ' ]\n')

    for j in names['Z_o' + str(i + 1)]:
        count += 1
        wrt.write(str(int(j)) + ' ')
        if count == 15:
            wrt.write('\n')
            count = 0

rrr = open('ndx.txt','r')
www = open('ndx_new.txt','w')
rls = rrr.readlines()
for i in rls:
    if len(i) < 3:
        nothing = 0
    else:
        www.write(i)
print(num)