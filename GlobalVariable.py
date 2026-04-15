def test1():
    global y
    y=20
    global x
    x=10
    print("X : ",x)
    print("Y : ",y)
    x=x+20
def test2():
    print("X : ",x)
    print("Y : ",y)

test1()
test2()
print("X : ",x)
print("Y : ",y)
