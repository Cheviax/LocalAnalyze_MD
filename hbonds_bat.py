drct = 'H:/GMX_OUT/JIANG/CO2_NEW/none/00/'
name = 'hbd.bat'
red = open(drct+name, 'w')

zhen = 1000
for i in range(zhen):
    print(i)
    line = 'gmx hbond -f gro_'+str(i+3000)+'.gro -s nvt -n idx_'\
           +str(i+3000)+'.ndx -num num'+str(i+3000)\
           +' -dist dist'+str(i+3000)\
           +' -ang ang'+str(i+3000)
    red.write(line)
    red.write('\n')