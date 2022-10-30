
"""#Минимализация
print("Минимализация")
print("x1x2x3y")
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            y = ((not x1) and x3) or (x1 and x2)
            print(x1, x2, x3, y)"""

"""#СДНФ
print("СДНФ")
print("x1x2x3y")
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            y = ((not x1) and (not x2) and x3) or ((not x1) and x2 and x3) or (x1 and x2 and (not x3)) or (x1 and x2 and x3)
            print(x1,x2,x3,y)"""

"""#СКНФ
print("СКНФ")
print("x1x2x3y")
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            y = (x1 or x2 or x3) and (x1 or (not x2) or x3) and ((not x1) or x2 or x3) and ((not x1) or x2 or (not x3))
            print(x1,x2,x3,y)"""

"""#Защита
print("ЗАЩИТА")
print("x1 x2 x3 x4 y1 y2")
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                y1 = ((not x1) and (not x2) and (not x3) and (not x4)) or ((not x1) and (not x2) and (not x3) and x4) or (x1 and (not x2) and (not x3) and x4) or (x1 and (not x2) and x3 and (not x4)) or (x1 and (not x2) and x3 and x4)
                y2 = (x1 or x2 or x3 or x4) and (x1 or (not x2) or (not x3) or (not x4)) and ((not x1) or (not x2) or (not x3) or x4)
                print(x1,"",x2,"",x3,"",x4,"",int(y1),"",int(y2))"""

