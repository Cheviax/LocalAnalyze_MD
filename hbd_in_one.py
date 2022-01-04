drct = 'H:/GMX_OUT/JIANG/CO2_NEW/none/00/'

zhen = 1000
num_all = 0
for i in range(zhen):
    red = open(drct+'num'+str(3000+i)+'.xvg', 'r')
    lines = red.readlines()
    line = lines[-1]
    ls = line.split()
    num = int(ls[1])
    print(str(i)+'  '+str(num))
    num_all += num

num_all = num_all / zhen
print(num_all)