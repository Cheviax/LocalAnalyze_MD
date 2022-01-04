# for .top file
names = locals()

with open('fenlie.txt', 'r') as f:
    dogs = f.readlines()


for dog in dogs:
    doge = dog.split()
    out = ''

    # dogs.old
    for i in range(8):
        names['line_' + str(i+1)] = doge[i]

    print(doge[6])
