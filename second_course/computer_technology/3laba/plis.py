print("X1 X2  X3  X4  Y0  Y1")
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                y0=(((not x1) and (not x2) and x3 and (not x4)) or ((not x1) and (not x2) and (not x3) and x4))
                y1=(((not x1) and (not x2) and (not x3) and x4) or ((not x1) and x2 and (not x3) and (not x4)))
                print(x1," ",x2," ",x3," ",x4," ",int(y0)," ",int(y1))