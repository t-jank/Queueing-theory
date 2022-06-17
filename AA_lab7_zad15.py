import random

p = 0.2
q = 0.4
qsize = 0 #liczba osob w kolejce
steps = 10000
stany = [0]*10
teoria = []
for i in range(0,100):
    teoria.append((p/q)**len(teoria)*(1-p/q)*steps)

for step in range(1,steps):
    x = random.random()
    if x < q:
        krok = -1  # cofamy się (liczebność kolejki maleje)
    elif x >= q and x < p+q:
        krok = 1  # idziemy naprzód (kolejka się zwiększa)
    else:
        krok = 0  # nic, kolejka nie zmienia się
    qsize += krok
    if qsize < 0:
        qsize = 0
    if qsize > len(stany)-1:
        stany.append(0)
    stany[qsize] += 1

if len(stany) > 150:
    print(stany[0:150])
else:
    print(stany)
print('Największy stan kolejki:', len(stany))
print('Teoria(+3):\n', teoria[0:len(stany)+3])
