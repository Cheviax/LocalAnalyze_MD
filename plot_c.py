import matplotlib.pyplot as mat

with open('plot.txt','r') as f:
    the = f.readlines()
with open('pl_c.txt','r') as g:
    thf = g.readlines()
with open('pl_i.txt','r') as h:
    thg = h.readlines()
with open('pl_p.txt','r') as i:
    thh = i.readlines()

mt1 = []
mt2 = []
ct1 = []
ct2 = []
it1 = []
it2 = []
pt1 = []
pt2 = []

for th in the:
    t = th.split()
    t_1 = float(t[0])
    t_2 = float(t[1])/0.69
    mt1.append(t_1)
    mt2.append(t_2)
for th in thf:
    t = th.split()
    t_1 = float(t[0])
    t_2 = float(t[1])
    ct1.append(t_1)
    ct2.append(t_2)
for th in thg:
    t = th.split()
    t_1 = float(t[0])
    t_2 = float(t[1])
    it1.append(t_1)
    it2.append(t_2)
for th in thh:
    t = th.split()
    t_1 = float(t[0])
    t_2 = float(t[1])
    pt1.append(t_1)
    pt2.append(t_2)

mat.plot(mt1,mt2)
mat.plot(ct1,ct2)
mat.plot(it1,it2)
mat.plot(pt1,pt2)

mat.scatter(ct1,ct2)
mat.xlim(-0.5,0.5)
mat.ylim(-2,12)
mat.xlabel('Vg')
mat.ylabel('Flux(nor)')
ax = mat.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
mat.show()