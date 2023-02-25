

x =10
def fun(): # function defination - outer


    y = 5
    x = 4

    def add(): # function defination - inner

        y = 15

        print(f" The value of x = {x}, y = {y},\ sum = {x+y}")

    add()

fun()
