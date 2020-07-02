# can return values
def sum(a, b):
    return a + b

print(sum(2, 5))

# default arguments
def greet(name, age=81):
    print('Hello ' + name + ', I am ' + age)
    
greet('Rich') # Traceback (most recent call last):
                # File "c:/Users/pgold/MatsonHub/Python-Pratical-Guide/py/apt.py", line 11, in <module>
                #     greet('Rich')
                # File "c:/Users/pgold/MatsonHub/Python-Pratical-Guide/py/apt.py", line 9, in greet                            ython.exe c:/Users/pgold/MatsonHub/P
                #     print('Hello ' + name + ', I am ' + age)
                # TypeError: can only concatenate str (not "int") to str
                # PS C:\Users\pgold\MatsonHub\Python-Pratical-Guide>