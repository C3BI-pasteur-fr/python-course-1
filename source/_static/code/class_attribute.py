class MyClass(object):

    class_attr = 'foo'

    def __init__(self, val):
        self.inst_attr = val




a = MyClass(1)
b = MyClass(2)

print a.inst_attr
?
print b.inst_attr
?

print a.class_attr == b.class_attr
?
print a.class_attr is b.class_attr
?

b.class_attr = 4

print a.class_attr
?
