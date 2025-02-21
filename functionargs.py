def addNum(*args):
    return sum(*args)

tp = (1,2,3,4,5,6,7,8,9,10)
a = addNum(tp)
print(a)


def student_detail(**kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print(f"{key}:{val}")

dict = {'name':'milan','age':28}
student_detail(name="Jayesh",age=21,city="bvn")