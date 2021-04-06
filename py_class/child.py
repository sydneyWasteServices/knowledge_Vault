from parent import Parent
# only inheritance has bracket wrap parent
class Child(Parent):
    def __init__(self):
        super().__init__()
        pass

    def child_function():
        mynum = super().parent_function()
        print(mynum)
        return mynum 


