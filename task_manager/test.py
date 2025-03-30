class A:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class B(A):
    def __init__(self, age, name):
        super().__init__(name)
        self.age = age

    def __call__(self, *args, **kwargs):
        return self.name


b = B(12, "nitish")
print(b())
