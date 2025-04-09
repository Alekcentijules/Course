# Local
x = 22

def func() -> None:
    x = 2
    print("\nChange the local x to ", x)

func()
print("Global x is still the same ", x)



# Enclosing
def outer_func():
    enclosing_var = "I'm a variable in a function that spans!"

    def inner_func():
        print("\nInside a nested function: ", enclosing_var)
    
    inner_func()

outer_func()



def func_outer():
    x = 22

    def func_inner():
        nonlocal x
        x = 5
    
    func_inner()
    return x

result = func_outer()
print(F"\n{result}")



# Global
x = 22

def func():
    global x
    print("\nx is equal to ", x)
    x = 2
    print("Change the global value of x to ", x)
func()
print("The value of x is ", x)
