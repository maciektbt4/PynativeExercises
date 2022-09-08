def outer(x, y):
    def inner():
        return x + y
    return inner() + "Developers"

print(outer(x= "Emma", y= "Kelly"))