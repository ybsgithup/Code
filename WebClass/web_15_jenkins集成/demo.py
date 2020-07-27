"""装饰器。

装饰器主要作用是为了修饰和扩展某个函数或者是类的功能。

测试一个函数的运行时间。
"""

def before(func):
    """装饰器"""
    def decorator():
        print("执行准备工作")
        func()
        print("后置清理工作")
    return decorator


@before
def run():
    import time
    time.sleep(1.2)
    print("hello world")


if __name__ == '__main__':
    # dec = before(run)
    # dec()

    run()







