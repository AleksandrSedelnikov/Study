"""for x0 in range(2):
    for x1 in range(2):
        y0=((not x0) and (not x1))
        y1=((not x1) and x0)
        y2=((not x0) and x1)
        y3=(x0 and x1)
        print(x1," " ,x0, " " ,int(y0), " " ,int(y1), " " ,int(y2), " " ,int(y3))
"""
print("X0  X1  X2  X3")
for x0 in range(2):
    for x1 in range(2):
        for x2 in range(2):
            for x3 in range(2):
                print(x0," ", x1, " ", x2," ", x3)