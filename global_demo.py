


def func ():

    global y
    y = "Hello"
    print(f'inside{y}')
    return y

global y

y =10
x = func()
print(f'outside{y}')
print(f'x={x}')
