with open('gro_1.txt','r') as f:
    dogs = f.readlines()

line_num = 0
x = 0
y = 0
z = 0
count = 0
sol = 2

for i in range(4):
    for dog in dogs:
        ds = dog.split()
        orr = ds[0]
        l2 = ds[1]
        l4 = ds[3]
        l5 = ds[4]
        l6 = ds[5]

        if orr == str(i+1)+'AG':
            count += 1
            print('    '+orr+'      '+l2+'  '+str(count)+'   '+l4+'   '+l5+'   '+l6)



