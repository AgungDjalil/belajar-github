# diamond problem

class A:
    def show(self):
        print("ini adlah show A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

objek = D()

objek.show()