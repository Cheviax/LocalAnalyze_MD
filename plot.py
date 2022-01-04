import matplotlib.pyplot as mat

with open('plt_l.txt','r') as f:
    the = f.readlines()

t1 = []
t2 = []

for th in the:
    t = th.split()
    t_1 = float(t[0])
    t_2 = float(t[1])/0.497
    t1.append(t_1)
    t2.append(t_2)

mat.plot(t1,t2)
mat.show()