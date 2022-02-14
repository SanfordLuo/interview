class MyClass(object):
    def __init__(self):
        self.name = 'sanford'
        self.age = 27

    def is_instance_method(self):
        print('实例方法 {0}'.format(self))

    @classmethod
    def is_class_method(cls):
        print('实例方法 {0}'.format(cls))

    @staticmethod
    def is_static_method():
        print('静态方法')


if __name__ == '__main__':
    my_class = MyClass()
    my_class.is_instance_method()
    my_class.is_class_method()
    my_class.is_static_method()

    # MyClass.is_instance_method()  # 类对象不可直接调实例方法
    MyClass.is_class_method()
    MyClass.is_static_method()
