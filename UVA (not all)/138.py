vl = 10
x = 8
while vl:
    nv = ((x * x + x) / 2) ** .5  # [ as , 2(n**2) = (x**2)+x , gauss formula ]
    if nv == int(nv):
        vl -= 1
        print(nv, x)
    x += 1

for i in range(0, 20, 2):
    ls = [6, 8, 35, 49, 204, 288, 1189, 1681, 6930, 9800, 40391, 57121, 235416, 332928, 1372105, 1940449, 7997214,
          11309768, 46611179, 65918161]
    print("%10d" % ls[i], "%9d" % ls[i + 1])
