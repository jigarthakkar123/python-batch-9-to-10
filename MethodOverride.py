class Base:
    def show(self):
        print("Show From Base")
class Derived(Base):
    def show(self):
        super().show()
        print("Show From Derived")
class SubDerived(Derived):
    def show(self):
        super().show()
        print("Show From SubDerived")


s1=SubDerived()
s1.show()
