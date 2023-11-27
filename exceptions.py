

#%%

try:
    with open("sometext.txt") as file:
        for line in file:
            print(line)
except:
    print('the file doesn\'t exist')


# %%

def say_hello_to_student():
    name = input("tell me your name: ")

    if name == "Pepe":
        raise ValueError("name should be a student's name, Pepe")

    print("hello " + name)

try:
    say_hello_to_student()
except:
    print("try again with a student's name")

#%%
def func3():
    open("potato.txt")

def func2():
    func3()

def func1():
    try:
        func2()
    except:
        print("something failed")

func1()
print("Hey Paula")

# %%
