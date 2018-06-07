class A:
    def __init__(self):
        print ("This method is called from class A")

class B(A):
    def __init__(self):
        print ("this mehod is called from class B")

class C(A):
    def __init__(self):
        print ("this mehod is called from class C")

class D(C,B):
    pass

d = D()
