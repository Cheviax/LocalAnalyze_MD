# for .top file
names = locals()

with open('top.txt', 'r') as f:
    dogs = f.readlines()

a = 0
le_set_1 = 6
le_set_2 = 11
le_set_3 = 7
le_set_4 = 7
le_set_5 = 7
le_set_6 = 7
le_set_7 = 11
le_set_8 = 11

num_count = 0

for dog in dogs:
    doge = dog.split()
    out = ''
    num_count += 1

    # dogs.old
    for i in range(8):
        names['line_' + str(i+1)] = doge[i]

    # assignment
    if num_count == 1:
        line_7 = float(line_7)
        line_7 += 0.2
     #   print('add')

    if num_count == 4:
        line_7 = float(line_7)
        line_7 += 0.2
      # print('add')

   # print(num_count)

    if num_count == 8:
        num_count = 0

# length of line
    for i in range(8):
        names['le_' + str(i+1)] = len(str(names['line_' + str(i+1)]))

# write
    for i in range(8):
        k = 0
        while k < names['le_set_' + str(i+1)] - names['le_' + str(i+1)]:
            out += ' '
            k   += 1
        out += str(names['line_' + str(i+1)])

# print
    print(out)
