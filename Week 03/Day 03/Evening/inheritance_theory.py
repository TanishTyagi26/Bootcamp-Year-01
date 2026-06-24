#  Inheritance  theory by Feroz sir

class A:
    def __init__(self):
        print("A Constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B Constructor")

class C(B):
    def __init__(self):
        super().__init__()
        print("C Constructor")

c = C()