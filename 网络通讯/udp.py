class Foo(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item)
        return self


print(Foo().think.different.itcast)
