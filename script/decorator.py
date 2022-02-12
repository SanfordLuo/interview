def func1(fun):
    def func2():
        print("验证")
        fun()
    return func2

@func1
def man():
    print("通过")

man()
