import inspect
def foo():
    print(inspect.stack()[0][3])
    print('My name is', __name__)
    print('STACK[0]:')
    print(inspect.stack()[0])
    print('STACK[1]:')
    print(inspect.stack()[1])
def boo():
    print(inspect.stack()[0][3])
    print('my name is', __name__)

boo()
foo()